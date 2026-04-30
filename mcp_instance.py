from mcp_instance import mcp
from fhir_client import FHIRClient
# Importar fhir_context si se usa el helper de extracción

@mcp.tool()
async def fetch_and_match(protocol_text: str, context: any = None):
    """
    Herramienta que utiliza el FHIR Client para obtener datos en tiempo real
    y compararlos con el protocolo del Trial Agent.
    """
    # 1. Extraer contexto de los headers (inyectados por la plataforma)
    # Nota: En FastMCP, puedes acceder a los headers del request de FastAPI
    # si el server está montado como vimos en main.py
    
    # Supongamos que extraemos estos valores del request actual:
    fhir_url   = "..." # Desde X-FHIR-URL
    token      = "..."    # Desde X-FHIR-Token
    patient_id = "..." # Desde X-FHIR-PatientId

    client = FHIRClient(fhir_url, token, patient_id)
    
    # 2. Obtener datos clave para el TrialMatcher (ej. HbA1c y Metformina)
    # Basado en el protocolo del ejemplo
    labs = await client.query_resource("Observation", {"code": "26436-6"}) # Código para HbA1c
    meds = await client.query_resource("MedicationStatement")
    
    # 3. Retornar el prompt de razonamiento con datos REALES
    return f"""
    DATOS DEL EHR RECUPERADOS:
    Laboratorios: {labs}
    Medicaciones: {meds}
    
    PROTOCOLO A EVALUAR:
    {protocol_text}
    
    Por favor, determina la elegibilidad considerando la estabilidad de 3 meses.
    """