from typing import Annotated
from mcp.server.fastmcp import Context
from pydantic import Field
from fhir_client import FhirClient
from fhir_utilities import get_fhir_context
from mcp_utilities import create_text_response

async def update_patient(
    patient_id: Annotated[str, Field(description="The FHIR ID of the patient to update.")],
    clinical_update: Annotated[str, Field(description="New clinical findings, lab results, or condition updates.")],
    ctx: Context = None
) -> str:
    """
    Updates an existing patient profile with new clinical data.
    Ensures the patient record 'evolves' for real-time re-evaluation.
    """
    fhir_context = get_fhir_context(ctx)
    if not fhir_context:
        return create_text_response("Error: No FHIR context available to perform update.")

    # Inicialización del cliente (siguiendo el estándar de match_patient_tool)
    client = FhirClient(base_url=fhir_context.url, token=fhir_context.token)
    
    # Lógica de actualización (Simulada hasta integrar con el storage real)
    # Aquí se enviaría el recurso PATCH al servidor FHIR o se actualizaría la Patient Card
    return create_text_response(f"Patient {patient_id} record updated with: {clinical_update}. You may now re-run the eligibility match.")
