import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s",handlers=[logging.FileHandler("logs.log",encoding="utf-8"),logging.StreamHandler()])

logging.getLogger("aiogram").disabled = True

logger = logging.getLogger("app")