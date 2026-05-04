# TrialMatcher: Bridging the $2.3B Clinical Trial enrollment Gap

**TheAI-PoweredClinicalTrialOrchestrationEngine**

[ ![MCP Compatible](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue)](https://modelcontextprotocol.io/)[ ![License](https://img.shields.io/badge/License-MIT-green.svg)](https://chat.z.ai/c/LICENSE)

---

## 🚀 TheExecutiveSummary

80% ofclinicaltrialsfailtomeetenrollmenttimelines, costingtheindustrybillionsanddelayinglife-savingtreatments.

**TrialMatcher** is an Agnostic Clinical Candidate Processor built on the Model Context Protocol (MCP). Unlike simple eligibility checkers, TrialMatcher is a fully operational AI engine that transforms heterogeneous clinical data into a prioritized, audit-ready short list of eligible patients.

By leveraging **Conversational Interoperability (COIN)**, we bridge the gap between unstructured patient data (EHRs, PDFs) and complex trial protocols, reducing screening time from weeks to hours while maintaining strict regulatory compliance.

````mermaid

flowchart TD
    subgraph User_Actor ["👤 Clinical Coordinator"]
    U1[Asks: "Is Patient X eligible?"]
    end

    subgraph PO_Platform ["📱 PromptOpinion (Host)"]
    UI[Chat Interface]
    LLM[Agentic Core / LLM]
    end

    subgraph MCP_Core ["⚡ TrialMatcher-MCP Server"]
    T1[Tool: get_trial_protocol]
    T2[Tool: prepare_fhir_evaluation]
    T3[Tool: log_eligibility_decision]
    LOGIC[Reasoning Engine & Temporal Logic]
    end

    subgraph Data_Sources ["🏥 Data Layer"]
    FHIR[EHR / FHIR Server]
    PDF[Protocol PDFs / JSON]
    DB[(SQLite Audit DB)]
    end

    %% Flow
    U1 --> UI
    UI --> LLM

    LLM --"SSE Call: Get Protocol"--> T1
    T1 --> PDF

    LLM --"SSE Call: Evaluate Patient"--> T2
    T2 --"Fetch Context"--> FHIR
    T2 --> LOGIC

    LOGIC -->|Results & Evidence| LLM

    LLM --"SSE Call: Log Decision"--> T3
    T3 --> DB

    LLM -->|Structured JSON| UI
    UI -->|Summary & Evidence| U1

    style MCP_Core fill:#1e293b,stroke:#38bdf8,color:#fff
    style Data_Sources fill:#f1f5f9,stroke:#94a3b8```

````

---

## 🎯 Why TrialMatcher?

### The Problem

- Heterogeneous data : Patient info is scattered across FHIR servers, PDFs, and free-text notes.
- Protocol complexity: Criteria involving temporal logic ("≥3 months stability") are impossible to query via SQL alone.
- Audit blindspots: AI decisions often lack the clinical evidence trail required by Pharma compliance.

### The Solution

- Agentic workflow: An AI agent retrieves patient data while another parses protocols; TrialMatcher MCP conducts the match.
- Non-Binary logic: We don't just return "Eligible/NotEligible". We are able to identify "Potential Matches", "Data Gaps", and "Missing Lab Requirements".
- Audit-Ready by design: Every match decision is backed by a "Clinical Reasoning Trace", citing specific record IDs, timestamps, and values.

---

## ✨ Key Capabilities

### 1. Universal data ingestion

Agnostic compatibility with HL7/FHIR, majorEHRs (Epic, Cerner), and unstructured sources (PDFs, ClinicalNotes).

### 2. Protocol intelligence 🧠

Automatically parses complex protocols to extract temporal criteria and biomarkers.

- Example: "Detects that 'Metformin stable' requires verifying start dates against current labs."

### 3. Advanced eligibility engine

Moves beyond binary classification:

- Eligible / Possibly Eligible / Not Eligible / Data Gap.
- Un certainty Handling: Flags casesm needing "Physician Review" (Human-in-the-loop).

#### 3.1 Flow example: Patient with incomplete data

![1777872934780](image/README/1777872934780.png)

### 4. Smart Ranking & Prioritization

Commercially powerful scoring algorithms:

- Probability of enrollment score.
- Risk of screen failure score.
- Prioritization by data completeness and geographic proximity.

### 5. Multi-Trial routing (The "Inverter")\*

Not just "Patient-> Trial," but "Patient-> All Applicable Trials." Crucial for finding alternatives when a patient fails a primary screen.

---

## 🔒 Compliance & Security (Non-Negotiable)

We are built for the highly regulated Pharma environment.

- **Data minimization:** Only necessary fields are processed formatching.
- **Pseudonymization:** SHA-256 hashing of MRNs ensures privacy while maintaining auditability.
- **Audit trails:** Immutable logs of who accessed what data and when.
- **Regional compliance:** Designed with GDPR (EU), HIPAA (US), and LGPD (LATAM) principles in mind.

---

## 🏗️ Architecture highlights

- **Core:** `FastMCP` server with `SSE`transport.
- **Backend:** Python-based processing with SQLite local persistence.
- **Interoperability:** Native FHIR context support.
- **Frontend:** Exposes tools via PromptOpinion ecosystem.

---

## 🏗️ Database model

![1777869423581](image/README/1777869423581.png)

---

## 🛠️ Installation & Usage

### Prerequisites

- Python 3.11+
- Ngrok (for local testing)

### QuickStart

```bash
# Clone the repogit clone https://github.com/your-org/trial-matcher-mcp.gitcd trial-matcher-mcp# Install dependenciespip install -r requirements.txt# Run the MCP Serverpython main.py
```

### IntegrationwithPromptOpinion

1. Run `ngrok http 8000`.
2. Add a new MCP server in PromptOpinion.
3. Transport: `StreamableHttp`.
4. Endpoint: YourNgrokURL + `/mcp`.

---

## 📈 Roadmap & FutureVision

- **Protocol sandbox :** "What if we lowered the ECOG criteria to 2?" Simulation tools.
- **GenomicsIntegration:** Support for NGS panels and Biomarkers (PD-L1, EGFR).
- **CRMIntegration :** Direct work flow to site coordinators.

---

## 💎 ForInvestors & Judges

TrialMatcher is not a classifier. It is an Operational Engine for clinical operations.
We increase the probability of trial success by providing an Explainable AI layer that sits on top of messy, real-world hospital data, ensuring that every recruitment decision is fast, safe, and scientifically justified.
