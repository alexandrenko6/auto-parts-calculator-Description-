"""
Главный модуль. Точка входа в программу.
"""

from input_handler import get_part_info, display_result, get_yes_no_input
from calculator import (
    calculate_delivery_cost,
    apply_promocode,
    apply_insurance,
    apply_urgent,
    calculate_total
)
from logger import log_calculation


def main():
    """Главная функция программы."""
    print("\n🔧 Добро пожаловать в калькулятор автозапчастей!")

    while True:
        # 1. Ввод данных
        data = get_part_info()

        # 2. Расчёт стоимости доставки
        delivery_cost = calculate_delivery_cost(
            data["weight"],
            data["distance"],
            data["delivery_method"]
        )

        # 3. Промежуточная сумма
        subtotal = data["base_price"] + delivery_cost

        # 4. Применение промокода
        after_promo, discount, promo_used = apply_promocode(
            subtotal, data["promocode"]
        )

        # 5. Применение страховки
        after_insurance, insurance_cost = apply_insurance(
            after_promo, data["insurance"]
        )

        # 6. Применение срочности
        after_urgent, urgent_fee = apply_urgent(
            after_insurance, data["urgent"]
        )

        # 7. Итоговая стоимость
        total = calculate_total(
            data["base_price"],
            delivery_cost,
            discount,
            insurance_cost,
            urgent_fee
        )

        # 8. Формирование результата
        result = {
            "part_name": data["part_name"],
            "base_price": data["base_price"],
            "delivery_cost": delivery_cost,
            "discount": discount,
            "promocode_applied": promo_used,
            "insurance_cost": insurance_cost,
            "urgent_fee": urgent_fee,
            "total": total
        }

        # 9. Вывод результата
        display_result(result)

        # 10. Логирование
        log_details = {
            "base_price": data["base_price"],
            "delivery_cost": delivery_cost,
            "discount": discount,
            "insurance": insurance_cost,
            "urgent": urgent_fee
        }
        log_calculation(data["part_name"], total, log_details)

        # 11. Спросить о повторном расчёте
        if not get_yes_no_input("\nВыполнить новый расчёт?"):
            print("\n👋 Спасибо за использование! До свидания!")
            break


if __name__ == "__main__":
    main()