import os
import logging

os.makedirs("logs",exist_ok=True)

logging.basicConfig(
  level=logging.INFO,
  filename="logs/app.log",
  format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger(__name__)