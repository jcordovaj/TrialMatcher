from typing import Annotated
from mcp.server.fastmcp import Context
from pydantic import Field
from fhir_client import FhirClient
from fhir_utilities import get_fhir_context
from mcp_utilities import create_text_response

async def find_patient_id(
    firstName: Annotated[str, Field(description="The patient's first name")], 
    lastName: Annotated[str | None, Field(description="The patient's last name. This is optional")] = None,
    ctx: Context = None,
) -> str:
    """
    Busca el ID de un paciente. Primero intenta vía FHIR y, si falla, 
    el agente puede usar su contexto de archivos adjuntos.
    """
    # Corregimos la llamada al nombre correcto de la función interna
    patients = await _find_patient(ctx, firstName, lastName)
    
    if not patients and lastName:
        # Intento invertido por si el usuario confundió los campos
        patients = await _find_patient(ctx, lastName, firstName)

    if patients and len(patients) > 1:
        return create_text_response("Se encontró más de un paciente. Por favor, proporcione más detalles (ej. fecha de nacimiento).", is_error=True)

    if patients and patients[0].get("id"):
        return create_text_response(patients[0]["id"])

    return create_text_response("No se encontró el paciente en el servidor FHIR. Verifique en los archivos adjuntos.", is_error=True)

async def _find_patient(
    ctx: Context,
    search_first_name: str | None,
    search_last_name: str | None,
) -> list[dict] | None:
    fhir_context = get_fhir_context(ctx)
    if not fhir_context:
        # Si no hay contexto FHIR, no podemos buscar en el servidor
        return None

    fhir_client = FhirClient(base_url=fhir_context.url, token=fhir_context.token)

    search_parameters: dict[str, str] = {}
    if search_first_name:
        search_parameters["given"] = search_first_name
    if search_last_name:
        search_parameters["family"] = search_last_name

    try:
        bundle = await fhir_client.search("Patient", search_parameters)
        if bundle and "entry" in bundle:
            return [item["resource"] for item in bundle["entry"] if "resource" in item]
    except Exception:
        return None
    
    return None
