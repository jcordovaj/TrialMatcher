---
name: clinical-document-ingestion
description: Extract clinical data from uploaded files (JSON, PDF, TXT, Excel). Use when the user provides patient lists, protocol criteria, or medical histories in the chat.
license: MIT
metadata:
  author: TrialMatcher
  version: "1.2"
---

# Clinical Document Ingestion

## Step-by-Step Instructions

1. [cite_start]**Context Priority**: When a file like `NCT07563218.json` or `fake_patients.json` is present in the chat, immediately extract its text content[cite: 1, 10].
2. **Data Mapping**:
   - **JSON Protocols**: Map `inclusion_rules` and `exclusion_rules` directly to the scoring engine.
   - **Patient Lists (JSON/Excel)**: Process batches of up to 50 candidates by extracting diagnoses and lab values.
   - **PDF Protocols**: Search for sections titled "Eligibility Criteria" or "Inclusion/Exclusion".
3. **No-Access Fallback**: Never report "lack of access" if the file is visible in the session context. [cite_start]Instead, parse the provided text stream[cite: 1, 16].

## Common Edge Cases

- **Heavy Protocols**: For PDFs >100 pages, focus exclusively on the Eligibility section to avoid context saturation.
- **Missing Fields**: If a JSON file lacks a specific lab value, mark it as `DATA_GAP` (multiplier 0.5) instead of failing the match.
