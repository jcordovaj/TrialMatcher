class ReasoningTemplates:
    @staticmethod
    def get_matching_prompt(protocol, clinical_data):
        return f"""
        ACTÚA COMO UN EXPERTO EN SCREENING DE ENSAYOS CLÍNICOS.
        
        PROTOCOLO DEL TRIAL AGENT:
        {protocol}
        
        DATOS FRESCOS DEL EHR (VÍA FHIR):
        {clinical_data}
        
        TAREAS:
        1. Cruza cada criterio de inclusión/exclusión.
        2. REGLA DE ORO (Estabilidad): Si el protocolo pide estabilidad de dosis (ej. 3 meses), 
        compara la fecha de la receta más antigua de ese medicamento contra la fecha actual. 
        Si hay menos de 90 días, marca como NO ELEGIBLE.
        3. Compara resultados previos si existen.
        
        SALIDA:
        Devuelve un análisis detallado y una conclusión final: [ELEGIBLE / NO ELEGIBLE / INFORMACIÓN INSUFICIENTE].
        """