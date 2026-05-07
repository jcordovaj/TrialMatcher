from typing import Annotated
from mcp.server.fastmcp import Context
from pydantic import Field
from fhir_utilities import get_patient_id_if_context_exists
from mcp_utilities import create_text_response
from audit_manager import AuditManager

async def check_previous_evaluation(
    trial_id: Annotated[str, Field(description="The ID of the trial to check in the audit logs.")],
    patientId: Annotated[str | None, Field(description="Optional patient ID.")] = None,
    ctx: Context = None
) -> str:
    """
    Checks the local audit database to see if this patient has been previously screened for a specific trial.
    Provides history of inclusion/exclusion to avoid redundant evaluations.
    """
    if not patientId:
        patientId = get_patient_id_if_context_exists(ctx)
        if not patientId:
            return create_text_response("Unable to identify patient to check audit logs.")

    audit = AuditManager()
    last = audit.get_last_evaluation(patientId, trial_id)

    if last:
        # last[0]: status, last[1]: reason, last[2]: date
        response = (
            f"Previous evaluation found (Date: {last[2]}):\n"
            f"- Status: {last[0]}\n"
            f"- Key Findings: {last[1]}"
        )
        return create_text_response(response)
    
    return create_text_response("No previous evaluation records found for this patient in this specific trial.")