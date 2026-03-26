Главный модуль. Точка входа в программу.
"""

from src.input_handler import get_part_info, display_result
from src.calculator import (
    calculate_delivery_cost, apply_promocode, apply_insurance,
    apply_urgent, calculate_total
)
from src.logger import log_calculation
from src.input_handler import get_yes_no_input

def main():
    """Главная функция программы."""
    print("\n🔧 Добро пожаловать в калькулятор автозапчастей!")
    
    while True:
        data = get_part_info()
        
        delivery_cost = calculate_delivery_cost(
            data["weight"], data["distance"], data["delivery_method"]
        )
        
        subtotal = data["base_price"] + delivery_cost
        
        after_promo, discount, promo_used = apply_promocode(
            subtotal, data["promocode"]
        )
        
        after_insurance, insurance_cost = apply_insurance(
            after_promo, data["insurance"]
        )
        
        after_urgent, urgent_fee = apply_urgent(
            after_insurance, data["urgent"]
        )
        
        total = calculate_total(
            data["base_price"], delivery_cost, discount, 
            insurance_cost, urgent_fee
        )
        
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
        
        display_result(result)
        
        log_details = {
            "base_price": data["base_price"],
            "delivery_cost": delivery_cost,
            "discount": discount,
            "insurance": insurance_cost,
            "urgent": urgent_fee
        }
        log_calculation(data["part_name"], total, log_details)
        
        if not get_yes_no_input("\nВыполнить новый расчёт?"):
            print("\n👋 Спасибо за использование! До свидания!")
            break

if __name__ == "__main__":
    main()
