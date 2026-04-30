from contextvars import ContextVar
from fastapi import Request

# Esta variable de contexto permite que cualquier parte del código acceda
# a los datos del paciente actual sin tener que pasarlos por todos los parámetros.
fhir_request_ctx: ContextVar[Request] = ContextVar("fhir_request_ctx")

class FHIRContext:
    @staticmethod
    def get_headers():
        """
        Extrae los headers estándar de SHARP inyectados por PromptOpinion.
        """
        try:
            request = fhir_request_ctx.get()
            return {
                "url": request.headers.get("X-FHIR-URL"),
                "token": request.headers.get("X-FHIR-Token"),
                "patient_id": request.headers.get("X-FHIR-PatientId")
            }
        except LookupError:
            # Si se llama fuera de una petición HTTP (ej. pruebas locales)
            return {"url": None, "token": None, "patient_id": None}  