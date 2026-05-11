import sqlite3
import os
from datetime import datetime
from typing import Annotated
from pydantic import Field

DB_NAME = "audit.db"

def save_evaluation(
    patient_id: Annotated[str, Field(description="The unique FHIR ID of the patient.")],
    trial_id: Annotated[str, Field(description="The clinical trial identifier.")],
    is_eligible: Annotated[str, Field(description="Eligibility result: ELIGIBLE, POSSIBLY ELIGIBLE (Flag), INELIGIBLE, or DATA_GAP (Flag).")],
    reasoning: Annotated[str, Field(description="Structured clinical justification for the result.")]
) -> str:
    """
    Saves the clinical evaluation result into the persistent audit database.
    Ensures traceability and compliance for medical auditing.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Schema ensures we have a timestamp for each recruitment decision
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS evaluations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id TEXT NOT NULL,
                trial_id TEXT NOT NULL,
                is_eligible TEXT NOT NULL,
                reasoning TEXT,
                evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cursor.execute(
            "INSERT INTO evaluations (patient_id, trial_id, is_eligible, reasoning) VALUES (?, ?, ?, ?)",
            (patient_id, trial_id, is_eligible, reasoning)
        )
        
        conn.commit()
        conn.close()
        return f"✅ Success: Evaluation saved. Patient {patient_id} status for {trial_id} is now '{is_eligible}'."
    
    except Exception as e:
        return f"❌ Database Error: Could not save evaluation. Detail: {str(e)}"