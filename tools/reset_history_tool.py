from typing import Annotated
from mcp.server.fastmcp import Context
from pydantic import Field
from fhir_utilities import get_patient_id_if_context_exists
from mcp_utilities import create_text_response
from audit_manager import AuditManager

async def reset_screening_history(
    patientId: Annotated[str | None, Field(description="Patient ID to reset.")] = None,
    ctx: Context = None
) -> str:
    """
    Clears the internal audit history for a specific patient. 
    Use this just to re-run eligibility tests from scratch during demonstrations.
    """
    if not patientId:
        patientId = get_patient_id_if_context_exists(ctx)
        
    if not patientId:
        return create_text_response("Error: No patient context found to reset.")

    audit   = AuditManager()
    success = audit.reset_patient_history(patientId)
    
    if success:
        return create_text_response(f"Success: History for patient {patientId} has been cleared. You can now perform a fresh screening.")
    return create_text_response("Error: Could not clear history. Check server logs.")