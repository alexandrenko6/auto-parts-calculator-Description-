"""
Модульные тесты для калькулятора.
Запуск: python -m pytest tests/test_calculator.py -v
"""

import unittest
import sys
import os

# Добавляем путь к src для импортов
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import (
    calculate_delivery_cost,
    apply_promocode,
    apply_insurance,
    apply_urgent,
    calculate_total
)


class TestCalculator(unittest.TestCase):
    """Тесты для модуля calculator.py"""

    def test_calculate_delivery_cost_regular(self):
        """Тест 1: Обычная доставка"""
        cost = calculate_delivery_cost(weight=1.5, distance=30, delivery_method=1)
        # (1.5×10) + (30×5) = 15 + 150 = 165
        self.assertEqual(cost, 165.0)

    def test_calculate_delivery_cost_express(self):
        """Тест 2: Экспресс-доставка (коэффициент 1.5)"""
        cost = calculate_delivery_cost(weight=1.5, distance=30, delivery_method=2)
        # 165 × 1.5 = 247.5
        self.assertEqual(cost, 247.5)

    def test_calculate_delivery_cost_pickup(self):
        """Тест 3: Самовывоз (стоимость 0)"""
        cost = calculate_delivery_cost(weight=10, distance=100, delivery_method=3)
        self.assertEqual(cost, 0.0)

    def test_apply_promocode_sale10(self):
        """Тест 4: Промокод SALE10 даёт скидку 10%"""
        new_total, discount, promo = apply_promocode(total=1000, promocode="SALE10")
        self.assertEqual(discount, 100.0)
        self.assertEqual(new_total, 900.0)
        self.assertEqual(promo, "SALE10")

    def test_apply_promocode_sale20(self):
        """Тест 5: Промокод SALE20 даёт скидку 20%"""
        new_total, discount, promo = apply_promocode(total=1000, promocode="SALE20")
        self.assertEqual(discount, 200.0)
        self.assertEqual(new_total, 800.0)

    def test_apply_promocode_invalid(self):
        """Тест 6: Неверный промокод — скидки нет"""
        new_total, discount, promo = apply_promocode(total=1000, promocode="INVALID")
        self.assertEqual(discount, 0.0)
        self.assertEqual(new_total, 1000.0)
        self.assertIsNone(promo)

    def test_apply_promocode_empty(self):
        """Тест 7: Пустой промокод — скидки нет"""
        new_total, discount, promo = apply_promocode(total=1000, promocode=None)
        self.assertEqual(discount, 0.0)
        self.assertEqual(new_total, 1000.0)

    def test_apply_insurance_true(self):
        """Тест 8: Страховка добавляет 5%"""
        new_total, cost = apply_insurance(total=1000, has_insurance=True)
        self.assertEqual(cost, 50.0)
        self.assertEqual(new_total, 1050.0)

    def test_apply_insurance_false(self):
        """Тест 9: Без страховки — ничего не добавляется"""
        new_total, cost = apply_insurance(total=1000, has_insurance=False)
        self.assertEqual(cost, 0.0)
        self.assertEqual(new_total, 1000.0)

    def test_apply_urgent_true(self):
        """Тест 10: Срочная доставка +500 руб"""
        new_total, fee = apply_urgent(total=1000, is_urgent=True)
        self.assertEqual(fee, 500.0)
        self.assertEqual(new_total, 1500.0)

    def test_apply_urgent_false(self):
        """Тест 11: Без срочности — ничего не добавляется"""
        new_total, fee = apply_urgent(total=1000, is_urgent=False)
        self.assertEqual(fee, 0.0)
        self.assertEqual(new_total, 1000.0)

    def test_calculate_total(self):
        """Тест 12: Итоговый расчёт"""
        total = calculate_total(
            base_price=2500,
            delivery_cost=165,
            discount_amount=100,
            insurance_cost=50,
            urgent_fee=500
        )
        # 2500 + 165 + 50 + 500 - 100 = 3115
        self.assertEqual(total, 3115.0)


if __name__ == "__main__":
    unittest.main()
