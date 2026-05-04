# TrialMatcher

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

# Funcionalidades clave

## 1) Ingesta de datos multi-fuente (agnóstico real)

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

## 2) Interpretación automática del protocolo (Protocol Intelligence)

Capacidad de “leer” protocolos clínicos reales:

- extracción de criterios I/E desde PDF
- identificar condiciones temporales (“últimos 6 meses”, “≥2 líneas previas”)
- normalización de endpoints, biomarcadores, estadios, ECOG
- detectar ambigüedades y “needs clarification”

Esto es crítico porque el protocolo es el principal cuello de botella.

---

## 3) Motor de elegibilidad avanzado (no binario)

El mercado no quiere solo Eligible/Not Eligible. Quiere:

- **Eligible / Possibly Eligible / Not Eligible**
- “Missing data” explícito
- “Needs physician review”(HITL)
- elegibilidad por subcriterio
- elegibilidad dinámica en el tiempo

**El valor real está en manejar incertidumbre clínica.**

---

## 4) Ranking y priorización de candidatos

El feature más comercialmente poderoso:

- scoring por probabilidad de enrolamiento
- scoring por riesgo de screen failure
- scoring por “closeness to criteria”
- priorización por disponibilidad de datos y completitud
- priorización por geografía / site / capacidad operativa

Esto es lo que reduce semanas a días.

---

## 5) Explicabilidad y trazabilidad (Audit-ready)

Esto es requisito de compra en pharma y hospitales:

- evidencia citada (nota clínica, fecha, lab value, documento)
- reasoning estructurado (“criteria-by-criteria decision”)
- versionado de protocolos
- historial de decisiones y cambios
- logs para auditoría

Sin esto, el AI no pasa compliance.

---

## 6) Manejo robusto de datos incompletos

En clínica siempre falta algo:

- identifica “data gaps”
- sugiere qué examen/lab falta para confirmar
- genera checklist para pre-screening
- recomienda preguntas al paciente o al médico

Esto aumenta enrolamiento real.

---

## 7) Workflow operacional (site-facing)

Los sitios clínicos compran eficiencia, no IA:

- lista de candidatos por site
- asignación de casos a coordinadores
- estados: “contactado / interesado / descartado / en screening”
- tareas y recordatorios
- integración con CRM / CTMS

Un motor que solo responde preguntas no escala.

---

## 8) Cohort discovery y feasibility

Funcionalidad crítica en etapas tempranas:

- “¿Cuántos pacientes tengo para este trial?”
- estimación por hospital / región / edad / biomarcador
- simulación de cambios de criterios (“si bajamos ECOG 2→1 cuántos quedan”)

Esto es clave para sponsors y CROs.

---

## 9) Multi-trial matching (matching inverso)

No solo “paciente→trial”, sino:

- “paciente→todos los trials aplicables”
- recomendación de trial alternativo si no califica
- motor de “trial routing” para oncología especialmente

Esto es lo que diferencia un producto.

---

## 10) Normalización médica estándar

Factor de compra silencioso:

- mapeo a SNOMED CT / ICD-10 / LOINC / RxNorm
- identificación de sinónimos (“lung adenocarcinoma” = NSCLC subtype)
- biomarcadores (EGFR, ALK, PD-L1)

Sin ontologías, el matching es frágil.

---

# Funcionalidades esperadas/deseadas (pero ya casi obligatorias)

## A) Resumen clínico automático orientado a trial

- “patient profile card”
- timeline de tratamientos y progresión
- resumen de comorbilidades relevantes
- medicación activa

Esto reduce carga del coordinador.

---

## B) Timeline reasoning

Criterios temporales son el 80% del dolor:

- “No chemo en últimos 28 días”
- “progresión posterior a línea 2”
- “diagnóstico confirmado hace >6 meses”

El sistema debe construir una línea de tiempo clínica.

---

## C) Detección de conflictos y riesgos de screen failure

- labs borderline
- contraindicaciones potenciales
- comorbilidades que sugieren exclusión futura
- alertas por interacciones farmacológicas (en trials específicos)

---

## D) Recomendación de acciones

- “ordenar PD-L1 test”
- “confirmar ECOG”
- “solicitar imagen reciente”
- “pedir consentimiento para contactar”

---

## E) Reportes para sponsor/CRO

- funnel de reclutamiento
- tasa de elegibilidad por criterio
- tiempo medio por screening
- causas de no elegibilidad más frecuentes

Esto es muy demandado.

---

# Funcionalidades críticas de cumplimiento normativo (no negociables)

## 1) Privacidad y protección de datos

Debe soportar:

- minimización de datos (solo lo necesario para matching)
- cifrado en tránsito y reposo
- control de acceso por roles (RBAC/ABAC)
- segregación por site/organización (multi-tenant real)
- trazabilidad de accesos (quién vio qué y cuándo)

---

## 2) Anonimización / Pseudonimización real

Muy importante: en salud casi siempre se requiere **pseudonimización** , no “anonimización total”.

- masking de identificadores directos (nombre, RUT, teléfono)
- tokenización reversible controlada (solo bajo permisos)
- manejo de quasi-identifiers (edad exacta, dirección, fechas)

---

## 3) Consentimiento y uso secundario de datos

Debe permitir:

- registrar consentimiento del paciente
- permitir opt-out
- separar “feasibility” (conteo agregado) de “contactability”

Muchos hospitales no aceptan contacto sin consentimiento explícito.

---

## 4) Cumplimiento regulatorio por región

Dependiendo del mercado:

- GDPR (UE)
- HIPAA (EEUU)
- normativas locales LATAM (Chile, Brasil LGPD, etc.)

Debe incluir:

- data residency
- retention policies
- derecho a eliminación (“right to be forgotten” donde aplique)

---

## 5) Seguridad operacional

Requisito de compra:

- SSO (SAML/OIDC)
- MFA
- logging + SIEM integration
- controles de exportación de datos
- políticas de backup y disaster recovery

---

## 6) Validación y control de calidad del modelo

Si hay IA, deben existir mecanismos de:

- evaluación continua de performance
- detección de drift
- versionado de prompts/modelos/reglas
- reproducibilidad del resultado

Sin reproducibilidad, no pasa auditoría clínica.

---

# Diferenciadores premium (los que hacen ganar deals)

## 1) Human-in-the-loop

Workflow donde un coordinador o médico:

- revisa recomendaciones
- aprueba el contacto
- corrige datos y realimenta el sistema

Esto da confianza y mejora precisión.

---

## 2) Multi-modalidad (labs + genomics + imaging metadata)

Oncología exige:

- biomarcadores
- NGS panel results
- staging TNM
- evolución de tumor

El producto que soporta esto gana.

---

## 3) “Explainability UI” por criterio

Interfaz tipo:

- Criterio: ECOG 0–1 → **PASS**
- Evidencia: “ECOG 1” (nota, fecha, autor)
- Confianza: 0.92
- Comentario clínico

Esto es oro para coordinadores y auditores.

---

## 4) Simulación de protocolo (Protocol sandbox)

“¿Qué pasa si relajamos criterio X?”

Esto se usa para diseñar trials más reclutables.

---

# En resumen: lo que realmente compra el mercado

Un **Trial Candidate Processor** competitivo debe ofrecer:

- Ingesta universal de datos clínicos
- Comprensión automática del protocolo
- Matching no-binario con incertidumbre
- Ranking y priorización accionable
- Trazabilidad y auditabilidad completa
- Workflow operacional para sites
- Feasibility y cohort discovery
- Seguridad, pseudonimización y compliance by design

En una frase:

**TrialMatcher no es un clasificador** , es un **motor operativo basado en la aplicación de AI explicable que agiliza los procesos para el reclutamiento clínico con IA explicable y compliance integrado** .
