import json
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# ==========================================
# CONFIGURACIÓN DE DATOS MÉDICOS
# ==========================================

conditions_list = [
    "Type 2 Diabetes Mellitus (T2DM)",
    "Hypertension",
    "Coronary Artery Disease",
    "Chronic Kidney Disease",
    "Hypothyroidism",
    "Diabetes",
    "Asthma",
    "Hyperlipidemia",
    "Obesity",
    "None"
]

medications_list = [
    {"name": "Metformin HCL", "dose": "1000 mg BID"},
    {"name": "Lisinopril", "dose": "20 mg daily"},
    {"name": "Atorvastatin", "dose": "40 mg daily"},
    {"name": "Insulin Glargine", "dose": "10 units nightly"},
    {"name": "Empagliflozin", "dose": "10 mg daily"},
    {"name": "Amlodipine", "dose": "5 mg daily"},
    {"name": "Lisinopril", "dose": "10 mg tablet nightly"},
    {"name": "Salbutamol", "dose": "40 ml daily"},
    {"name": "Budesonide", "dose": "1600 mcg daily"},
    {"name": "Atorvastatin", "dose": "10 mg daily"},
    {"name": "Rosuvastatin", "dose": "30 mg daily"},
    {"name": "Aspirin", "dose": "500 mg daily"},
    {"name": "Clopidogrel", "dose": "500 mg daily"},
    {"name": "Levothyroxine", "dose": "50 mg daily"},
    {"name": "Erythropoietin", "dose": "2,000 IU/0.5 ml injectable solution in a pre-filled syringe twice a week"},
    {"name": "Furosemide", "dose": "80 mg daily"}
]  

lab_tests = [
    {"test": "HbA1c", "unit": "%"},
    {"test": "Creatinine", "unit": "mg/dL"},
    {"test": "ALT", "unit": "U/L"}
]

# ==========================================
# FUNCIONES DE AYUDA
# ==========================================

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def generate_patient(idx):
    # basic demographics
    gender    = random.choice(['male', 'female'])
    dob       = fake.date_of_birth(minimum_age=18, maximum_age=80)
    age       = (datetime.now().date() - dob).days // 365
    height_cm = random.randint(150, 200)
    weight_kg = random.randint(50, 140)
    bmi       = calculate_bmi(weight_kg, height_cm)

    # Lógica para forzar casos de prueba (Cada 10 pacientes, forzamos un caso borde)
    case_type            = idx % 10
    is_diabetic          = False
    is_pregnant          = False
    history_pancreatitis = False
    history_thyroid_ca   = False
    metformin_start_date = None
    is_stable_metformin  = True

    # Casos de Borde forzados para probar tu MCP
    if case_type == 1: 
        # CASO: Embarazo (Exclusión típica GLP-1)
        is_pregnant = True if gender == 'female' else False
    elif case_type == 2:
        # CASO: Cáncer de Tiroides (Exclusión seguridad)
        history_thyroid_ca = True
    elif case_type == 3:
        # CASO: Pancreatitis (Exclusión seguridad)
        history_pancreatitis = True
    elif case_type == 4:
        # CASO: Metformina inestable (Exclusión protocolo)
        is_stable_metformin = False
    elif case_type == 5:
        # CASO: Metformina reciente (< 3 meses) - La trampa de fechas
        # Calculamos fecha hace menos de 90 días
        metformin_start_date = (datetime.now() - timedelta(days=random.randint(10, 80))).strftime("%Y-%m-%d")
    
    # Generar Historial Médico
    pmh = []
    if is_diabetic or random.random() > 0.3:
        is_diabetic = True
        pmh.append({
            "condition": "Type 2 Diabetes Mellitus (T2DM)",
            "diagnosisDate": (dob + timedelta(days=365*30)).strftime("%Y-%m-%d") # Diagnóstico hace tiempo
        })
    
    if random.random() > 0.5:
        pmh.append({
            "condition": "Hypertension",
            "status"   : "well-controlled" if random.random() > 0.2 else "uncontrolled"
        })

    # Generar Medicamentos
    meds = []
    if is_diabetic:
        # Si es diabético, probablemente tome Metformina
        meds.append({
            "name"     : "Metformin HCL",
            "dose"     : random.choice(["500 mg BID", "1000 mg BID"]),
            "startDate": metformin_start_date if metformin_start_date else (datetime.now() - timedelta(days=random.randint(300, 1000))).strftime("%Y-%m-%d"),
            "isStable" : is_stable_metformin
        })
        if random.random() > 0.5:
            meds.append(random.choice(medications_list))
    
    # Agregar otros meds random
    if random.random() > 0.6:
        meds.append(random.choice(medications_list))

    # Generar Labs
    labs = []
    # HbA1c (Si es diabético, tiende a ser alto)
    hba1c = round(random.uniform(5.0, 6.4), 1) if not is_diabetic else round(random.uniform(6.5, 11.0), 1)
    labs.append({
        "test" : "HbA1c",
        "value": f"{hba1c}%",
        "date" : (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d")
    })

    patient_data = {
        "patientRecord": {
            "name": fake.name(),
            "mrn" : f"{random.randint(1000, 99999)}-{chr(65+idx)}", # MRN falso pero único
            "dob" : dob.strftime("%Y-%m-%d"),
            "age" : age,
            "demographics": {
                "heightCm": height_cm,
                "weightKg": weight_kg
            },
            "bmi": bmi,
            "pastMedicalHistory": pmh,
            "medications": meds,
            "labs": labs,
            "flags": {
                "isPregnant": is_pregnant,
                "plansToConceive": random.choice([True, False]) if not is_pregnant else False,
                "isBreastfeeding": random.choice([True, False]) if is_pregnant else False,
                "historyOfPancreatitis": history_pancreatitis,
                "personalHistoryOfThyroidCarcinoma": history_thyroid_ca,
                "familyHistoryOfThyroidCarcinoma": random.choice([True, False])
            }
        }
    }
    return patient_data

# ==========================================
# EJECUCIÓN
# ==========================================

all_patients = []
for i in range(1, 51):
    all_patients.append(generate_patient(i))

# Guardar en archivo
output_filename = "fake_patients.json"
with open(output_filename, "w") as f:
    json.dump(all_patients, f, indent=2)

print(f"✅ Se han generado {len(all_patients)} pacientes en el archivo '{output_filename}'.")
print("📝 El archivo incluye casos de borde para probar la lógica de elegibilidad.")