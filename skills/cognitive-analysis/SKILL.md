---
name: cognitive-analysis

description: Comprehensive clinical trial matching toolkit. Includes PDF/JSON parsing, MCDA scoring, safety hard-stops, and pseudonymization guards. Use for patient eligibility screening and protocol feasibility analysis.
license: None
metadata:
  author: TrialMatcher-Team
  version: "1.0"
---

# TrialMatcher Core Skills

This skill set enables agents to perform high-precision clinical trial orchestration by bridging the gap between raw medical data and complex protocols.

## 1. Data Processing Skills

### pdf-json-processing

- **Function**: Extracts text from PDFs and schema-based data from JSON.
- **Usage**: Activate when the user uploads protocol PDFs or clinical datasets in JSON format.

### read-txt-files-enclosed

- **Function**: Reads and extracts information from any text-based files uploaded to the chat session.

## 2. Clinical Intelligence Skills

### clinical-protocol-semantic-parsing

- **Function**: Extracts and categorizes inclusion/exclusion criteria.
- **Logic**: Assigns stratified weights: HIGH (W=3), MEDIUM (W=2), and LOW (W=1).

### multi-criteria-eligibility-scoring

- **Function**: Computes eligibility using the MCDA framework: `Score = (Σ(Wi × Ci) / ΣWi) × 100`.
- **Compliance Multipliers**: MET (1.0), DATA_GAP (0.5), NOT_MET (0.0).

### absolute-safety-hard-stop

- **Function**: Clinical guardrail. If a HIGH weight criterion is NOT_MET, the final score is automatically forced to 0%.

## 3. Advanced Analysis & Compliance

### in-context-batch-screening

- **Function**: Evaluates arrays of up to 50 candidates against 10 protocols simultaneously within the current conversation context.

### cognitive-sensitivity-simulation

- **Function**: Executes "What-If" analysis. Recalculates cohort metrics when protocol boundaries (e.g., lab thresholds) are modified in real-time.

### pseudonymized-compliance-guard

- **Function**: Masks PII (Personally Identifiable Information) by using Subject IDs (SUBJ-XXXXX). Triggers audit logs for any re-identification request.

### evidentiary-traceability-indexing

- **Function**: Anchors verdicts (ELIGIBLE, DATA_GAP) to source text using markdown footnotes ([^1]) for audit verification.

## ⚠️ Instructions for Agents

1. **Context Authority**: If data is pasted or uploaded in the chat, use these skills to process it immediately. Do not claim lack of access.
2. **Formatting**: Always output results in professional Markdown (Tables, Bold headers) and avoid raw JSON blocks unless requested.
