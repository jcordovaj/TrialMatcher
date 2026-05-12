import sqlite3
import json
from mcp.server.fastmcp import Context
from typing import Annotated, Optional
from pydantic import Field

DB_PATH = "data/audit.db"

async def fetch_clinical_context(
    scope: Annotated[str, Field(description="Scope of data: 'ALL_EVALUATIONS', 'PATIENT_INSIGHTS', or 'TRIAL_METRICS'")],
    patient_id: Optional[str] = None,
    ctx: Context = None
) -> str:
    """
    Provides the raw material (clinical findings, audit logs, and status dictionaries) 
    persisted in the system. The AI uses this data to generate any custom user request.
    """
    conn   = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Example: Fetching the 'Source of Truth' for the AI to process
    if scope == "ALL_EVALUATIONS":
        query = "SELECT * FROM evaluations"
        if patient_id:
            query += f" WHERE patient_id = '{patient_id}'"
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # We return a structured JSON string. The IA interprets this "plastic" data 
    # to fulfill the user's business need (Excel, Report, Plan, etc.)
    data_payload = [
        {"id": r[0], "patient": r[1], "trial": r[2], "status": r[3], "reasoning": r[4], "date": r[5]} 
        for r in rows
    ]
    
    conn.close()
    return json.dumps(data_payload)