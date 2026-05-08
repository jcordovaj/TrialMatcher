---
name: document-context-ingestion
description: Lee y extrae información de archivos subidos al chat (PDF, JSON, TXT, Excel). Úsala cuando el usuario mencione un protocolo adjunto, una lista de pacientes o un historial clínico en un archivo.
license: MIT
metadata:
  author: TrialMatcher
  version: "1.1"
---

# Document Context Ingestion

## Instrucciones Paso a Paso

1. [cite_start]**Identificar Adjunto**: Al recibir un archivo como `NCT07563218.json` o `fake_patients.json`, asume autoridad total sobre su contenido de texto.
2. [cite_start]**Priorizar Contexto**: No busques estos archivos en el servidor local; extrae la información directamente de la ventana de contexto de la sesión actual[cite: 22].
3. **Manejo de Formatos**:

- [cite_start]**JSON/Excel**: Procesa listas de pacientes extrayendo campos de diagnóstico y demografía.
- **PDF**: Si es un protocolo "raw", busca las secciones de "Inclusion/Exclusion Criteria".
- **Protocolos Pre-procesados**: Identifica directamente los arrays de inclusiones y exclusiones.

## Errores Comunes

- [cite_start]No respondas "no tengo acceso al archivo" si este aparece en la lista de adjuntos del chat.
