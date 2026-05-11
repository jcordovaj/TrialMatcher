from mcp.server.fastmcp import FastMCP
from tools.match_patient_tool import match_patient_to_trial
from tools.check_audit_tool import check_previous_evaluation
from tools.reset_tool import reset_screening_history

mcp = FastMCP("TrialMatcher Pro", stateless_http=True)

# Patching capabilities for FHIR Scopes (Essential for the .rs permissions)
_original_get_capabilities = mcp._mcp_server.get_capabilities

def _patched_get_capabilities(notification_options, experimental_capabilities):
    caps = _original_get_capabilities(notification_options, experimental_capabilities)
    caps.model_extra["extensions"] = {
        "ai.promptopinion/fhir-context": {
            "scopes": [
                {"name": "patient/Patient.rs", "required": True},
                {"name": "patient/Observation.rs"},
                {"name": "patient/MedicationStatement.rs"},
                {"name": "patient/Condition.rs"},
            ]
        }
    }
    return caps

mcp._mcp_server.get_capabilities = _patched_get_capabilities

# Registration
mcp.tool(
    name="MatchPatientToTrial", 
    description="Evaluates patient eligibility against a clinical trial protocol using real-time FHIR data."
)(match_patient_to_trial)

mcp.tool(
    name="CheckEvaluationHistory", 
    description="Retrieves the historical screening results for a patient from the internal audit database."
)(check_previous_evaluation)

mcp.tool(
    name="AdminResetHistory", 
    description="Developer tool to clear patient screening logs for re-testing."
)(reset_screening_history)

mcp.tool(
    name="IngestClinicalAsset",
    description="Pre-processes large clinical files (PDF/JSON). Categorizes data into Patients or Protocols and stores them in the vector database."
)(ingest_data_asset_tool)

mcp.tool(
    name="UpdatePatientRecord",
    description="Updates an existing patient profile with new lab results or medical findings."
)(update_patient_tool)