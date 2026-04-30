import httpx
import logging
from fhir_context import FHIRContext

class FHIRClient:
    def __init__(self):
        ctx = FHIRContext.get_headers()
        self.fhir_url = ctx.get("url")
        self.token = ctx.get("token")
        self.patient_id = ctx.get("patient_id")
        
        # Validación: Si falta algo, el cliente debe avisar
        if not all([self.fhir_url, self.token, self.patient_id]):
            logging.warning("FHIRClient iniciado con contexto incompleto.")

    async def get_patient_summary(self) -> str:
        """
        Consulta el historial clínico relevante (Medicaciones y Observaciones).
        Devuelve un string formateado para que el LLM lo procese.
        """
        if not self.fhir_url:
            return "Error: No hay conexión al servidor FHIR."

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/fhir+json"
        }

        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                # 1. Buscamos Medicaciones (para la Metformina)
                med_url  = f"{self.fhir_url}/MedicationStatement?patient={self.patient_id}"
                med_resp = await client.get(med_url, headers=headers)
                med_resp.raise_for_status()
                
                # 2. Buscamos Observaciones (para HbA1c / IMC)
                obs_url = f"{self.fhir_url}/Observation?patient={self.patient_id}"
                obs_resp = await client.get(obs_url, headers=headers)
                obs_resp.raise_for_status()

                # Retornamos una combinación simple para el razonamiento inicial
                return f"MEDS: {med_resp.text[:2000]}... \nOBS: {obs_resp.text[:2000]}..."
            
            except httpx.HTTPStatusError as e:
                logging.error(f"Error FHIR: {e.response.status_code}")
                return f"Error al consultar datos clínicos: {e.response.status_code}"
            except Exception as e:
                logging.error(f"Error inesperado: {str(e)}")
                return f"Falla en la comunicación con el EHR: {str(e)}"