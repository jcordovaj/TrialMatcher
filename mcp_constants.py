FHIR_SERVER_URL_HEADER   = "x-fhir-server-url"
FHIR_ACCESS_TOKEN_HEADER = "x-fhir-access-token"
PATIENT_ID_HEADER        = "x-patient-id"

ENTITY_KEYWORDS: dict[str, list[str]] = {
    "summary"   : ["patient_summary", "patient_profile"],
    "labs"      : ["lab_result", "lab_report", "chemistry_panel", "blood_panel", "hba1c", "glucose"],
    "imaging"   : ["chest_xray", "radiology", "ultrasound", "mri", "ct_scan"],
    "meds"      : ["medication", "prescription", "drug_admin", "dosage", "metformin"],
    "conditions": ["diagnosis", "problem_list", "active_condition", "health_issue"]
}

# Tipos de recursos FHIR que solicitaremos por defecto
DEFAULT_RESOURCES = ["Observation", "MedicationStatement", "Condition", "Patient"]