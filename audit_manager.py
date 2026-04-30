import sqlite3
import json
import hashlib
from datetime import datetime

class AuditManager:
    def __init__(self, db_path="audit.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Inicializa la tabla de auditoría con el estándar de SHARP."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS screening_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_hash TEXT NOT NULL,
                trial_id TEXT NOT NULL,
                decision TEXT NOT NULL, -- ELEGIBLE / NO ELEGIBLE / PENDIENTE
                reasoning TEXT,         -- Explicación del LLM
                criteria_json TEXT,     -- Detalle por criterio
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def _generate_hash(self, patient_id):
        """Anonimiza el ID del paciente antes de guardarlo."""
        return hashlib.sha256(patient_id.encode()).hexdigest()[:16]

    def log_decision(self, patient_id, trial_id, decision, reasoning, criteria_map):
        """Registra la decisión final del match."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO screening_log 
                (patient_hash, trial_id, decision, reasoning, criteria_json)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                self._generate_hash(patient_id),
                trial_id,
                decision,
                reasoning,
                json.dumps(criteria_map)
            ))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error en auditoría: {e}")
            return False
        finally:
            conn.close()