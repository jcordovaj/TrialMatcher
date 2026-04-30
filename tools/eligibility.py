from mcp_instance import mcp
from fhir_client import FHIRClient
from audit_manager import AuditManager # El que hicimos antes
from reasoning.templates import ReasoningTemplates

@mcp.tool()
async def evaluate_clinical_eligibility(trial_id: str, protocol_text: str):
    """
    Herramienta principal para el match agnóstico. 
    Une la información del Trial Agent con los datos del paciente real.
    """
    client = FHIRClient()
    audit  = AuditManager()
    
    # 1. ¿Ya lo evaluamos hoy? (Memoria)
    # Por ahora traemos los datos frescos para asegurar precisión
    clinical_data = await client.get_patient_summary()
    
    # 2. Generamos el razonamiento
    prompt = ReasoningTemplates.get_matching_prompt(protocol_text, clinical_data)
    
    # 3. El MCP devuelve el prompt al Agente de PO para que el LLM lo ejecute
    # En un flujo real, aquí podríamos procesar la respuesta y luego auditar
    return prompt