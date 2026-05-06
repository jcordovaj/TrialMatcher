from typing import Annotated
from mcp.server.fastmcp import Context
from pydantic import Field
from fhir_client import FhirClient
from fhir_utilities import get_fhir_context, get_patient_id_if_context_exists
from mcp_utilities import create_text_response
from scrapbook.reasoning.templates import ReasoningTemplates
from audit_manager import AuditManager

async def match_patient_to_trial(
    trial_id: Annotated[str, Field(description="The unique identifier of the clinical trial.")],
    protocol_text: Annotated[str, Field(description="The full text or criteria of the clinical trial protocol.")],
    patientId: Annotated[
        str | None, 
        Field(description="Optional patient ID. If not provided, the current UI context will be used.")
    ] = None,
    ctx: Context = None
) -> str:
    """
    Performs an agnostic screening between a specific patient's FHIR data and a clinical trial protocol.
    It retrieves real-time clinical context (Conditions, Observations, Medications) to evaluate eligibility.
    """
    # 1. Obtención de Identidad y Contexto FHIR (Patrón del ejemplo)
    if not patientId:
        patientId = get_patient_id_if_context_exists(ctx)
        if not patientId:
            raise ValueError("No patient context found in the current session.")

    fhir_context = get_fhir_context(ctx)
    if not fhir_context:
        raise ValueError("The FHIR context (URL/Token) could not be retrieved from Prompt Opinion.")

    # 2. Inicialización de Clientes con credenciales dinámicas
    # Usamos el token que PO nos inyecta en el handshake
    fhir_client = FhirClient(base_url=fhir_context.url, token=fhir_context.token)
    audit = AuditManager()

    # 3. Recolección de evidencia clínica (Aprovechando los Scopes .rs)
    # Aquí el cliente FHIR debe usar los endpoints aprobados (Patient, Observation, etc.)
    clinical_data = await fhir_client.get_full_clinical_context(patientId)

    # 4. Generación del Prompt de Razonamiento (Agnostic Matching)
    # Adaptamos el template para que el LLM de PO ejecute la decisión final
    prompt = ReasoningTemplates.get_agnostic_matching_prompt(protocol_text, clinical_data)

    # 5. Auditoría silenciosa (Uso interno)
    # Registramos que se inició una evaluación para este trial/paciente
    audit.log_evaluation_attempt(patientId, trial_id)

    return create_text_response(prompt)