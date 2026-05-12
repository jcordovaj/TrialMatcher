from mcp.server.fastmcp import FastMCP
# Domain 1: Matching & Core Logic
from tools.match_patient_tool import match_patient_to_trial
from tools.update_patient_tool import update_patient

# Domain 2: Data Ingestion & Persistence
from tools.ingest_asset_tool import ingest_data_asset
from tools.save_evaluation_tool import save_evaluation

# Domain 3: Audit & Administration
from tools.check_audit_tool import check_previous_evaluation
from tools.reset_history_tool import reset_screening_history


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
    description="Evaluates patient eligibility against a clinical trial protocol using MCDA scoring."
)(match_patient_to_trial)

mcp.tool(
    name="IngestClinicalAsset",
    description="Processes clinical PDF/JSON files and stores them in the persistent vector database."
)(ingest_data_asset)

mcp.tool(
    name="UpdatePatientRecord",
    description="Updates a patient's clinical profile with new findings for real-time re-evaluation."
)(update_patient)

mcp.tool(
    name="SaveEvaluation",
    description="Persists the final clinical match result and reasoning into the audit database."
)(save_evaluation)

mcp.tool(
    name="CheckEvaluationHistory",
    description="Retrieves historical screening results to ensure traceability and avoid redundancy."
)(check_previous_evaluation)

mcp.tool(
    name="AdminResetHistory",
    description="Developer tool to clear patient logs for re-testing purposes."
)(reset_screening_history)