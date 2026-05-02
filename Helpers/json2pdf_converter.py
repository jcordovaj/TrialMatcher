import json
import os
import csv
from fpdf import FPDF

def extract_safe(data, path, default="MISSING"):
    """Navega por el JSON sin romperse si falta una llave."""
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def json_to_clinical_pdf(input_path, output_pdf_folder, audit_csv_path):
    # 1. Intentar abrir el archivo con manejo de errores de permiso
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except PermissionError:
        print(f"ERROR: No se puede acceder a {input_path}. Asegúrate de que el archivo no esté abierto en otro programa.")
        return
    except Exception as e:
        print(f"ERROR INESPERADO: {e}")
        return

    if not os.path.exists(output_pdf_folder):
        os.makedirs(output_pdf_folder)

    audit_log = []
    # ClinicalTrials.gov suele envolver todo en una lista o en una llave 'studies'[cite: 2]
    studies = data.get('studies', []) if isinstance(data, dict) else data

    print(f"Procesando {len(studies)} estudios...")

    for study in studies:
        protocol = study.get('protocolSection', {})
        
        # Extracción segura de datos esenciales[cite: 2]
        nct_id = extract_safe(protocol, ["identificationModule", "nctId"])
        title = extract_safe(protocol, ["identificationModule", "briefTitle"])
        gender = extract_safe(protocol, ["eligibilityModule", "sex"])
        min_age = extract_safe(protocol, ["eligibilityModule", "minimumAge"])
        max_age = extract_safe(protocol, ["eligibilityModule", "maximumAge"])
        criteria = extract_safe(protocol, ["eligibilityModule", "eligibilityCriteria"])
        
        # Auditoría de calidad médica
        has_criteria = "YES" if criteria != "MISSING" and len(criteria) > 50 else "NO"
        has_age = "YES" if min_age != "MISSING" or max_age != "MISSING" else "NO"
        status = "PASS" if has_criteria == "YES" and has_age == "YES" else "FLAG"

        audit_log.append({
            "NCT_ID": nct_id,
            "Has_Criteria": has_criteria,
            "Has_Age": has_age,
            "Gender": gender,
            "Status": status
        })

        # Crear el PDF si el estudio es válido
        if nct_id != "MISSING":
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", 'B', 14)
                pdf.multi_cell(0, 10, txt=f"{nct_id}: {title}")
                pdf.ln(5)
                pdf.set_font("Arial", '', 10)
                # Limpiamos el texto para FPDF[cite: 2]
                content = f"Gender: {gender}\nAge: {min_age} to {max_age}\n\nCriteria:\n{criteria}"
                pdf.multi_cell(0, 5, txt=content.encode('latin-1', 'ignore').decode('latin-1'))
                pdf.output(os.path.join(output_pdf_folder, f"{nct_id}.pdf"))
            except Exception as e:
                print(f"Error generando PDF para {nct_id}: {e}")

    # Guardar reporte de auditoría
    with open(audit_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["NCT_ID", "Has_Criteria", "Has_Age", "Gender", "Status"])
        writer.writeheader()
        writer.writerows(audit_log)

    print(f"Finalizado. PDFs en: {output_pdf_folder}")
    print(f"Reporte de auditoría en: {audit_csv_path}")

# --- CONFIGURACIÓN DE RUTAS ---
ruta_json  = r"C:\x360\Consultoría\OpenAI\HackatonPromptOpinion\knowledgebase\trials\raw_trials\ctg_studies_json"
ruta_pdf   = r"C:\x360\Consultoría\OpenAI\HackatonPromptOpinion\knowledgebase\trials\snapshot_trials"
ruta_audit = r"C:\x360\Consultoría\OpenAI\HackatonPromptOpinion\knowledgebase\trials\audit_report.csv"

json_to_clinical_pdf(ruta_json, ruta_pdf, ruta_audit)