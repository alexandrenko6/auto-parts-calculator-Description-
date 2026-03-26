Модуль логирования.
"""

import logging
import os

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, "calculations.log")

def setup_logger():
    logger = logging.getLogger("AutoPartsCalculator")
    logger.setLevel(logging.INFO)
    
    if logger.handlers:
        return logger
    
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '[%(asctime)s] | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

def log_calculation(part_name, total_cost, details):
    logger = setup_logger()
    
    log_message = f"Запчасть: {part_name} | Итог: {total_cost:.2f} руб | "
    log_message += f"База: {details['base_price']:.2f} | "
    log_message += f"Доставка: {details['delivery_cost']:.2f} | "
    log_message += f"Скидка: {details['discount']:.2f} | "
    log_message += f"Страховка: {details['insurance']:.2f} | "
    log_message += f"Срочность: {details['urgent']:.2f}"
    
    logger.info(log_message)
    print(f"\n✅ Результат сохранён в лог: {LOG_FILE}")

def get_log_file_path():
    return LOG_FILE
