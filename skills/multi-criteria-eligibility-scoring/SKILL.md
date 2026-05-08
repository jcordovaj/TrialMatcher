---
name: multi-criteria-eligibility-scoring
description: Ejecuta el análisis de elegibilidad estratificado (MCDA). Úsala para calcular el score de compatibilidad (0-100%) entre un paciente y un protocolo.
license: MIT
metadata:
  author: TrialMatcher
  version: "1.0"
---

# Multi-Criteria Eligibility Scoring (MCDA)

## Lógica de Puntuación

1. **Pesos (W)**:
   - HIGH (3): Factores críticos de seguridad.
   - MEDIUM (2): Comorbilidades secundarias.
   - LOW (1): Valores de laboratorio flexibles.
2. **Multiplicadores (C)**:
   - MET (1.0) | DATA_GAP (0.5) | NOT_MET (0.0).
3. **Fórmula de cálculo**:
   - `Score = (Σ(Wi × Ci) / ΣWi) × 100`.

## Ejecución

Si falta información, marca como `DATA_GAP` en lugar de rechazar.
