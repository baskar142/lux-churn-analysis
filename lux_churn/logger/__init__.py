import logging
import os
from pathlib import Path
from datetime import datetime

# ✅ Dynamically get the project root (assuming logger is inside: project_root/lux_churn/logger/)
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # Go 2 levels up from logger/__init__.py

# ✅ Define log directory and file name
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_PATH = LOG_DIR / LOG_FILE

# ✅ Create the logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# ✅ Configure the logger
logging.basicConfig(
    filename=str(LOG_PATH),
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# ✅ Optional: Show where log file is written (for verification)
print(f"✅ Logging to: {LOG_PATH}")
