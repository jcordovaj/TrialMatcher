# TrialMatcher: Superando la brecha de USD 2.3B en el enrolamiento para ensayos clínicos

**Motor de orquestación de ensayos clínicos impulsado por IA**

[![MCP Compatible](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-blue)](https://modelcontextprotocol.io/)[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://chat.z.ai/c/LICENSE)

![Snapshot TrialMatcher](image/README/banner2.png)

---

## 🚀 Resumen Ejecutivo

El 80% de los ensayos clínicos fallan en cumplir sus plazos de inscripción, costando miles de millones a la industria y retrasando tratamientos salvavidas.

**TrialMatcher** es un **Procesador Agnóstico de Candidatos** construido sobre el **Model Context Protocol (MCP)**. A diferencia de simples verificadores de elegibilidad, TrialMatcher es un motor operativo de IA que transforma datos clínicos heterogéneos en una lista priorizada y auditable de pacientes elegibles.

Al aprovechar la _Interoperabilidad Conversacional (COIN)_, cerramos la brecha entre los datos desestructurados del paciente (historiales clínicos, PDFs) y los complejos protocolos de los estudios, reduciendo el tiempo de cribado de semanas a horas sin sacrificar el cumplimiento normativo.

---

## 🎯 ¿Por qué TrialMatcher?

### El Problema

- **Datos heterogéneos:** La información del paciente está dispersa en servidores FHIR, PDFs y notas de texto libre.
- **Complejidad de los Protocolos:** Criterios con lógica temporal ("≥3 meses de estabilidad") son imposibles de consultar solo con SQL.
- **Puntos ciegos de Auditoría:** Las decisiones de IA a menudo carecen del rastro de evidencia clínica requerido por el cumplimiento farmacéutico.

### La Solución

- **Flujo Agentico:** Un agente de IA recupera los datos del paciente mientras otro analiza el protocolo; el MCP TrialMatcher realiza el cruce (match) proveyendo un conjunto de herramientas poderosas.
- **Lógica No Binaria:** No devolvemos solo "Apto / No Apto". Identificamos _Coincidencias Potenciales_, _Faltantes de Datos_ y _Requisitos de Laboratorios Faltantes_.
- **Auditable por Diseño:** Cada decisión de cruce está respaldada por un "Rastro de Razonamiento Clínico", citando IDs de registro específicos, fechas y valores trazables.

---

## ✨ Capacidades Clave

### 1. Ingesta de Datos Universal

Compatibilidad agnóstica con HL7/FHIR, principales EHRs (Epic, Cerner) y fuentes no estructuradas (PDFs, Notas Clínicas, JSON).

### 2. Inteligencia de Protocolo 🧠

Analiza automáticamente protocolos complejos para extraer criterios temporales y biomarcadores.

- _Ejemplo:_ "Detecta que la 'Estabilidad de Metformina' requiere verificar las fechas de inicio contra los laboratorios actuales.", "Sugiere cuando un examen de laboratorio está próximo a vencer y el científico toma la decisión si requiere revalidarlo."

### 3. Motor de Elegibilidad Avanzado

Superamos la clasificación binaria:

- **Elegible / Posiblemente Elegible / No Elegible / Falta de Datos.**
- **Manejo de Incertidumbre:** Marca casos que requieren "Revisión Médica" (Humano en el bucle).

### 4. Ranking y Priorización Inteligente

Algoritmos de puntuación comercialmente poderosos:

- Puntuación de probabilidad de inscripción.
- Puntuación de riesgo de fracaso en el cribado (screen failure).
- Priorización por completitud de datos y proximidad geográfica.

### 5. Enrutamiento Multi-Estudio (El "Inversor")\*

No solo "Paciente -> Estudio", sino "Paciente -> Todos los Estudios Aplicables". Crucial para encontrar alternativas cuando un paciente falla el cribado principal.

---

---

## 🔒 Gobernanza y Arquitectura

Para que el sistema sea coherente, sin redundancias y con una clara separación de responsabilidades, cada agente que ajecuta el MCP posee SKILLS específica que cumplen con el formato de skills.org.

Todo se organiza en 4 Skills maestras que agrupan las funcionalidades lógicas que debe interpretar el asistente, eliminando heurísticas que causaban ruido.

---

### Agentes y Skills

1. Agente A: Clinical Eligibility Specialist

   Este agente es el "Cerebro Clínico". Se encarga del análisis profundo, la seguridad y el cálculo matemático.
   - Skill 1: clinical-intelligence-engine: (Agrupa: Multi Criteria Scoring, Absolute Safety Hard Stop, y Protocol Semantic Parsing).
   - Skill 2: compliance-and-traceability: (Agrupa: Evidentiary Traceability, Pseudonymized Compliance Guard, y Cognitive Sensitivity Simulation).

2. Agente B: Clinical Trial Master Orchestrator

   Este agente es el "Director de Orquesta". Maneja la interacción, el flujo de datos y la gestión de archivos masivos.
   - Skill 3: clinical-asset-orchestration: (Agrupa: Coordinate Batch Trial Matching, Clinical Asset Ingestion, y In Context Batch Screening).
   - Skill 4: patient-record-evolution: (Mantiene la lógica de actualización dinámica de laboratorios/perfiles).

---

## 🔒 Cumplimiento y Seguridad (Innegociable)

Estamos construidos para el entorno farmacéutico altamente regulado.

- **Minimización de Datos:** Solo se procesan los campos necesarios para el matching.
- **Pseudonimización:** Hashing SHA-256 de MRNs garantiza la privacidad mientras mantiene la auditabilidad.
- **Trazabilidad de Auditoría:** Registros inmutables de quién accedió a qué datos y cuándo.
- **Cumplimiento Regional:** Diseñado con principios GDPR (UE), HIPAA (EEUU) y LGPD (LATAM) en mente.

---

## 🏗️ Aspectos de la Arquitectura

- **Núcleo:** Servidor `FastMCP` con transporte `SSE`.
- **Backend:** Procesamiento en Python con persistencia local SQLite.
- **Interoperabilidad:** Soporte nativo de Contexto FHIR.
- **Frontend:** Expone herramientas a través del ecosistema PromptOpinion.

---

## 🛠️ Instalación y Uso

### Prerrequisitos

- Python 3.11+
- Ngrok (para pruebas locales)

### Inicio Rápido

```bash
# Clonar el repositorio
git clone https://github.com/jcordovaj/TrialMatcher.git
cd TrialMatcher

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el Servidor MCP
python main.py
```
