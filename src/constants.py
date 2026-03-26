"""
Модуль констант для калькулятора автозапчастей.
"""

DELIVERY_RATES = {
    1: {
        "name": "Обычная",
        "rate_per_kg": 10.0,
        "rate_per_km": 5.0,
        "multiplier": 1.0
    },
    2: {
        "name": "Экспресс",
        "rate_per_kg": 10.0,
        "rate_per_km": 5.0,
        "multiplier": 1.5
    },
    3: {
        "name": "Самовывоз",
        "rate_per_kg": 0.0,
        "rate_per_km": 0.0,
        "multiplier": 0.0
    }
}

PROMOCODES = {
    "SALE10": 10,
    "SALE20": 20,
    "WELCOME": 5,
    "BLACKFRIDAY": 25
}

INSURANCE_PERCENT = 0.05
URGENT_FEE = 500.0
FREE_DELIVERY_THRESHOLD = 5000.0