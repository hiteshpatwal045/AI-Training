import os
import logging

#1. make directory
os.makedirs("logs", exist_ok=True)

#2. basic config
logging.basicConfig(
  level=logging.INFO,
  filename="logs/app.log",
  format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

#3. creating logger Object
logger = logging.getLogger(__name__)