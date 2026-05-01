# audit_manager.py
import sqlite3
import logging
from datetime import datetime
from pathlib import Path

# Configuración de logs para depuración en producción
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AuditManager")

class AuditManager:
    def __init__(self, db_name: str = "mcp_audit.db"):
        # Localizamos la base de datos en el directorio del proyecto
        self.db_path = Path(__file__).parent / db_name
        self._bootstrap()

    def _bootstrap(self):
        """Inicializa la tabla de auditoría si no existe."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS evaluation_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id TEXT NOT NULL,
                        trial_id TEXT NOT NULL,
                        status TEXT,
                        reason TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                # Índice para búsquedas rápidas durante "Batch Processing"
                conn.execute("CREATE INDEX IF NOT EXISTS idx_patient_trial ON evaluation_logs (patient_id, trial_id)")
        except Exception as e:
            logger.error(f"Critical error initializing Audit DB: {e}")

    def log_evaluation_attempt(self, patient_id: str, trial_id: str, status: str = "PENDING", reason: str = ""):
        """Registra un intento de evaluación sin bloquear el flujo principal."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT INTO evaluation_logs (patient_id, trial_id, status, reason) VALUES (?, ?, ?, ?)",
                    (patient_id, trial_id, status, reason)
                )
        except Exception as e:
            logger.error(f"Failed to log evaluation: {e}")

    def reset_patient_history(self, patient_id: str):
        """Elimina el historial de auditoría de un paciente para permitir nuevas pruebas."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("DELETE FROM evaluation_logs WHERE patient_id = ?", (patient_id,))
                logger.info(f"Audit history reset for patient: {patient_id}")
                return True
        except Exception as e:
            logger.error(f"Failed to reset patient history: {e}")
            return False

    def get_last_evaluation(self, patient_id: str, trial_id: str):
        """Recupera el resultado más reciente para evitar evaluaciones duplicadas."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    "SELECT status, reason, created_at FROM evaluation_logs "
                    "WHERE patient_id = ? AND trial_id = ? "
                    "ORDER BY created_at DESC LIMIT 1",
                    (patient_id, trial_id)
                )
                return cursor.fetchone()
        except Exception as e:
            logger.error(f"Error querying Audit DB: {e}")
            return None