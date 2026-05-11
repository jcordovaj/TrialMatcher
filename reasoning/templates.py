class ReasoningTemplates:
    @staticmethod
    def get_agnostic_matching_prompt(protocol_rules, clinical_evidence):
        return f"""
        # EVALUADOR CLÍNICO AGNÓSTICO (TrialMatcher)
        
        ## 1. REGLAS DE ENTRADA (Contexto del Trial Agent):
        {protocol_rules}

        ## 2. EVIDENCIA CLÍNICA (Contexto del EHR):
        {clinical_evidence}

        ## 3. TAREA:
        Actúa como un auditor de datos. No asumas nada que no esté en la evidencia.
        - Identifica en la 'EVIDENCIA' los valores que corresponden a las variables de las 'REGLAS'.
        - Para cualquier criterio de tiempo (estabilidad, duración), usa las fechas de los registros.
        - Si una variable requerida en las REGLAS no existe en la EVIDENCIA, márcala como 'DATO FALTANTE'.

        ## 4. FORMATO DE AUDITORÍA:
        Por cada criterio analizado, indica:
        - Criterio: [Nombre del parámetro]
        - Valor Hallado: [Valor en EHR]
        - Resultado: [CUMPLE / REQUIERE REVISION / NO CUMPLE / DATOS FALTANTES]
        
        CONCLUSIÓN FINAL: [ELEGIBLE / POSSIBLY ELIGIBLE / INELEGIBLE / DATA GAP]
        
        """