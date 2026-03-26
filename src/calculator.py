"""
Модуль расчётов для калькулятора автозапчастей.
"""

from constants import (
    DELIVERY_RATES,
    PROMOCODES,
    INSURANCE_PERCENT,
    URGENT_FEE,
    FREE_DELIVERY_THRESHOLD
)


def calculate_delivery_cost(weight, distance, delivery_method):
    """Рассчитывает стоимость доставки."""
    if delivery_method not in DELIVERY_RATES:
        raise ValueError(f"Неизвестный способ доставки: {delivery_method}")

    rates = DELIVERY_RATES[delivery_method]
    base_cost = (weight * rates["rate_per_kg"]) + (distance * rates["rate_per_km"])
    final_cost = base_cost * rates["multiplier"]
    return round(final_cost, 2)


def apply_promocode(total, promocode):
    """Применяет скидку по промокоду."""
    if not promocode or promocode.strip() == "":
        return total, 0.0, None

    promocode = promocode.upper().strip()

    if promocode in PROMOCODES:
        discount_percent = PROMOCODES[promocode]
        discount_amount = total * (discount_percent / 100)
        new_total = total - discount_amount
        return round(new_total, 2), round(discount_amount, 2), promocode
    else:
        print(f"⚠️ Промокод '{promocode}' не найден.")
        return total, 0.0, None


def apply_insurance(total, has_insurance):
    """Добавляет стоимость страховки."""
    if has_insurance:
        insurance_cost = total * INSURANCE_PERCENT
        new_total = total + insurance_cost
        return round(new_total, 2), round(insurance_cost, 2)
    return total, 0.0


def apply_urgent(total, is_urgent):
    """Добавляет плату за срочную доставку."""
    if is_urgent:
        return total + URGENT_FEE, URGENT_FEE
    return total, 0.0


def calculate_total(base_price, delivery_cost, discount_amount,
                    insurance_cost, urgent_fee):
    """Вычисляет итоговую стоимость."""
    total = base_price + delivery_cost + insurance_cost + urgent_fee - discount_amount
    return round(total, 2)


def check_free_delivery(total):
    """Проверяет, положена ли бесплатная доставка."""
    return total >= FREE_DELIVERY_THRESHOLD