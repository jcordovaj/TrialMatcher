# TrialMatcher: Bridging the $2.3B Clinical Trial Enrollment Gap

The Problem: 80% of clinical trials fail to meet enrollment timelines, costing the industry billions and delaying life-saving treatments.

The Solution: TrialMatcher is an Agnostic Clinical Candidate Processor powered by MCP. It transforms heterogeneous clinical data (FHIR, PDFs, Clinical Notes) into a prioritized, audit-ready shortlist of eligible patients through Conversational Interoperability (COIN).

Why TrialMatcher?
Protocol Intelligence: It doesn't just "read"; it reasons through complex temporal criteria and biomarkers.

Audit-Ready Evidence: Every match is backed by a clinical reasoning trace, citing specific medical records.

Multi-Trial Routing: Automatically identifies the best-fit trial for a single patient among hundreds of protocols.

TrialMatcher

Es un MCP que actúa como **procesador agnóstico de candidatos para ensayos clínicos** (Trial Candidate Processor MCP), sin embargo, no es sólo un "eligibility checker”para evaluar pacientes -aptos o no aptos- para estudios clínicos. Es un MCP Server diseñado para acelerar, drásticamente, el screening, la priorización y trazabilidad en la selección de pacientes para actuaciones clínicas, que reduce tiempo sin perder eficiencia, aumenta las tasas de enrolamiento y está preparado para un compliance riguroso, resolviendo uno de los mayores cuellos de botella en la industria farmacéutica actual.

En terminos simples, TrialMatcher, a través de un proceso de "conversational interoperabilty", interactúa con múltiples agentes, razonando peticiones, para traer los datos del paciente y su historial, mientras, un segundo agente trae el contexto del estudio (protocolo), el MCP evalúa y provee tools para hacer el match individual o por lotes, auditar, analizar datos como un dashboard, alertar sobre riesgos, alineándose con las necesidades de la Industria.

## El proceso

Un motor agentico convierte **datos clínicos heterogéneos** (EHR, notas, labs, imágenes referenciadas, claims, genomics) + **protocolos complejos** en:

- cohortes candidatos
- ranking/priorización
- evidencia clínica trazable
- workflow para contactabilidad y pre-screening
- reporting operacional

---

## Funcionalidades clave

### 1) Ingesta de datos multi-fuente (agnóstico real)

Conectores y compatibilidad con:

- HL7 / FHIR
- EHR comunes (Epic, Cerner/Oracle, Meditech)
- Data warehouses hospitalarios
- PDFs, scans, eCRFs
- notas clínicas libres (NLP)
- laboratorios estructurados y semi-estructurados
- integración con CTMS / eTMF

**Diseñado para integrarse con fácilidad.**

---

### 2) Interpretación automática del protocolo (Protocol Intelligence)

Capacidad de “leer” protocolos clínicos reales:

- extracción de criterios I/E desde PDF
- identificar condiciones temporales (“últimos 6 meses”, “≥2 líneas previas”)
- normalización de endpoints, biomarcadores, estadios, ECOG
- detectar ambigüedades y “needs clarification”

Esto es crítico porque el protocolo es el principal cuello de botella.

---

### 3) Motor de elegibilidad avanzado (no binario)

El mercado no quiere solo Eligible/Not Eligible. Quiere:

- **Eligible / Possibly Eligible / Not Eligible**
- “Missing data” explícito
- “Needs physician review”(HITL)

### 📄 README.md (EnglishVersion)

# TrialMatcher: TheAI-PoweredClinicalTrialOrchestrationEngine

Bridgingthe $2.3BClinicalTrialEnrollmentGapwithAgenticIntelligence.

[![MCP Compatible](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue)](https://modelcontextprotocol.io/)[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://chat.z.ai/c/LICENSE)

---

## 🚀 TheExecutiveSummary

80% ofclinicaltrialsfailtomeetenrollmenttimelines, costingtheindustrybillionsanddelayinglife-savingtreatments.

**TrialMatcher**isanAgnosticClinicalCandidateProcessorbuiltontheModelContextProtocol (MCP). Unlikesimpleeligibilitycheckers, TrialMatcherisafullyoperationalAIenginethattransformsheterogeneousclinicaldataintoaprioritized, audit-readyshortlistofeligiblepatients.

ByleveragingConversationalInteroperability (COIN), webridgethegapbetweenunstructuredpatientdata (EHRs, PDFs) andcomplextrialprotocols, reducingscreeningtimefromweekstohourswhilemaintainingstrictregulatorycompliance.

---

## 🎯 WhyTrialMatcher?

### TheProblem

- HeterogeneousData:PatientinfoisscatteredacrossFHIRservers, PDFs, andfree-textnotes.
- ProtocolComplexity:Criteriainvolvingtemporallogic ("≥3 monthsstability") areimpossibletoqueryviaSQLalone.
- AuditBlindspots:AIdecisionsoftenlacktheclinicalevidencetrailrequiredbyPharmacompliance.

### TheSolution

- AgenticWorkflow:AnAIagentretrievespatientdatawhileanotherparsesprotocols; TrialMatcherMCPconductsthematch.
- Non-BinaryLogic:Wedon'tjustreturn "Eligible/NotEligible." WeidentifyPotentialMatches, DataGaps, andMissingLabRequirements.
- Audit-ReadybyDesign:Everymatchdecisionisbackedbya "ClinicalReasoningTrace," citingspecificrecordIDs, timestamps, andvalues.

---

## ✨ KeyCapabilities

### 1. UniversalDataIngestion

AgnosticcompatibilitywithHL7/FHIR, majorEHRs (Epic, Cerner), andunstructuredsources (PDFs, ClinicalNotes).

### 2. ProtocolIntelligence 🧠

Automaticallyparsescomplexprotocolstoextracttemporalcriteriaandbiomarkers.

- Example: "Detectsthat'Metforminstable'requiresverifyingstartdatesagainstcurrentlabs."

### 3. AdvancedEligibilityEngine

Movesbeyondbinaryclassification:

- Eligible / PossiblyEligible / NotEligible / DataGap.
- UncertaintyHandling:Flagscasesneeding "PhysicianReview" (Human-in-the-loop).

### 4. SmartRanking & Prioritization

Commerciallypowerfulscoringalgorithms:

- Probabilityofenrollmentscore.
- Riskofscreenfailurescore.
- Prioritizationbydatacompletenessandgeographicproximity.

### 5. Multi-TrialRouting (The "Inverter")\*

Notjust "Patient-> Trial," but "Patient-> AllApplicableTrials." Crucialforfindingalternativeswhenapatientfailsaprimaryscreen.

---

## 🔒 Compliance & Security (Non-Negotiable)

WearebuiltforthehighlyregulatedPharmaenvironment.

- DataMinimization:Onlynecessaryfieldsareprocessedformatching.
- **Pseudonymization:**SHA-256 hashingofMRNsensuresprivacywhilemaintainingauditability.
- AuditTrails:Immutablelogsofwhoaccessedwhatdataandwhen.
- RegionalCompliance:DesignedwithGDPR (EU), HIPAA (US), andLGPD (LATAM) principlesinmind.

---

## 🏗️ ArchitectureHighlights

- Core: `FastMCP`Serverwith `SSE`transport.
- Backend:Python-basedprocessingwithSQLitelocalpersistence.
- Interoperability:NativeFHIRContextsupport.
- Frontend:ExposestoolsviaPromptOpinionecosystem.

---

## 🛠️ Installation & Usage

### Prerequisites

- Python 3.9+
- Ngrok (forlocaltesting)

### QuickStart

```bash
# Clone the repogit clone https://github.com/your-org/trial-matcher-mcp.gitcd trial-matcher-mcp# Install dependenciespip install -r requirements.txt# Run the MCP Serverpython main.py
```

### IntegrationwithPromptOpinion

1. Run `ngrok http 8000`.
2. AddanewMCPServerinPromptOpinion.
3. Transport: `SSE`.
4. Endpoint: YourNgrokURL + `/sse`.

---

## 📈 Roadmap & FutureVision

- ProtocolSandbox: "WhatifweloweredtheECOGcriteriato 2?" Simulationtools.
- GenomicsIntegration:SupportforNGSpanelsandBiomarkers (PD-L1, EGFR).
- CRMIntegration:Directworkflowtositecoordinators.

---

## 💎 ForInvestors & Judges

TrialMatcherisnotaclassifier.ItisanOperationalEngineforclinicaloperations.
WeincreasetheprobabilityoftrialsuccessbyprovidinganExplainableAIlayerthatsitsontopofmessy, real-worldhospitaldata, ensuringthateveryrecruitmentdecisionisfast, safe, andscientificallyjustified.
