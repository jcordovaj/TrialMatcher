async def ingest_data_asset(file_content: str, file_name: str, ctx: Context):
    """
    Analyzes the file type. If it's a protocol, it extracts criteria using trial_parser.py.
    If it's a patient list (like fake_patients.json), it splits them and stores them in ChromaDB.
    """
    # 1. Logic to detect Patient vs Protocol
    if "patientRecord" in file_content or "resourceType" in file_content:
        # Batch Patient Ingestion
        patients = parse_json_patients(file_content) # Based on fake_patients.json
        for p in patients:
            # Store in ChromaDB with metadata={patient_id: p.id}
            vector_db.add_document(p.summary, metadata={"id": p.id})
        return f"Successfully ingested {len(patients)} patients into the vector store."

    elif "inclusion" in file_content.lower() or file_name.endswith(".pdf"):
        # Protocol Ingestion using trial_parser.py logic
        clean_criteria = extract_eligibility_chunk(file_content)
        vector_db.add_document(clean_criteria, metadata={"type": "protocol", "id": file_name})
        return f"Protocol {file_name} pre-processed and vectorized."
    
    return "Error: File type not recognized or clinically irrelevant."