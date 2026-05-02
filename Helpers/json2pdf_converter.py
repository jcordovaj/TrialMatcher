import json
import os
import csv
from fpdf import FPDF

def clean_medical_text(text):
    """Reemplaza símbolos problemáticos por equivalentes ASCII legibles."""
    if not text or text == "MISSING":
        return text
    
    replacements = {
        "≥": ">=",
        "≤": "<=",
        "•": "-",
        "κ": "kappa",
        "λ": "lambda",
        "α": "alpha",
        "β": "beta",
        "γ": "gamma",
        "±": "+/-",
        "°": " degrees",
        "\u03ba": "kappa", # Aseguramos el escape de unicode para kappa
    }
    
    for symbol, replacement in replacements.items():
        text = text.replace(symbol, replacement)
    
    # Eliminar cualquier otro carácter que fpdf2 no pueda renderizar en fuentes básicas
    return text.encode('ascii', 'ignore').decode('ascii')

def extract_safe(data, path, default="MISSING"):
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def process_folder_to_pdf(input_folder, output_pdf_folder, audit_csv_path):
    if not os.path.exists(output_pdf_folder):
        os.makedirs(output_pdf_folder)

    audit_log = []
    json_files = [f for f in os.listdir(input_folder) if f.endswith('.json')]
    
    print(f"Encontrados {len(json_files)} archivos JSON. Procesando con limpieza de símbolos...")

    for file_name in json_files:
        file_path = os.path.join(input_folder, file_name)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            studies = data.get('studies', [data]) if isinstance(data, dict) else data
            
            for study in studies:
                protocol = study.get('protocolSection', {})
                nct_id   = extract_safe(protocol, ["identificationModule", "nctId"])
                title    = extract_safe(protocol, ["identificationModule", "briefTitle"])
                gender   = extract_safe(protocol, ["eligibilityModule", "sex"])
                min_age  = extract_safe(protocol, ["eligibilityModule", "minimumAge"])
                max_age  = extract_safe(protocol, ["eligibilityModule", "maximumAge"])
                criteria = extract_safe(protocol, ["eligibilityModule", "eligibilityCriteria"])
                
                # Sanitización de datos para el PDF
                safe_title    = clean_medical_text(f"{nct_id}: {title}")
                safe_criteria = clean_medical_text(criteria)
                
                status = "PASS" if criteria != "MISSING" and nct_id != "MISSING" else "FLAG"

                # Generar PDF
                if nct_id != "MISSING":
                    pdf = FPDF()
                    pdf.add_page()
                    
                    pdf.set_font("helvetica", 'B', 12)
                    pdf.multi_cell(0, 10, text=safe_title) # Usamos 'text' en lugar de 'txt'
                    pdf.ln(5)
                    
                    pdf.set_font("helvetica", '', 10)
                    content = f"Gender: {gender}\nAge: {min_age} - {max_age}\n\nCriteria:\n{safe_criteria}"
                    pdf.multi_cell(0, 5, text=content)
                    
                    pdf.output(os.path.join(output_pdf_folder, f"{nct_id}.pdf"))

                audit_log.append({"File": file_name, "NCT_ID": nct_id, "Status": status})

        except Exception as e:
            print(f"Error procesando archivo {file_name}: {e}")
            audit_log.append({"File": file_name, "NCT_ID": "ERROR", "Status": "FAILED"})

    with open(audit_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["File", "NCT_ID", "Status"])
        writer.writeheader()
        writer.writerows(audit_log)

    print(f"\n--- PROCESO EXITOSO ---")
    print(f"Todos los archivos convertidos limpiamente.")

# --- RUTAS ---
ruta_raw   = r"C:\x360\Consultoría\OpenAI\HackatonPromptOpinion\knowledgebase\trials\raw_trials"
ruta_pdf   = r"C:\x360\Consultoría\OpenAI\HackatonPromptOpinion\knowledgebase\trials\snapshot_trials"
ruta_audit = r"C:\x360\Consultoría\OpenAI\HackatonPromptOpinion\knowledgebase\trials\audit_report.csv"

process_folder_to_pdf(ruta_raw, ruta_pdf, ruta_audit)