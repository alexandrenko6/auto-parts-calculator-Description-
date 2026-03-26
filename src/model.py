cat > src/model.py << 'EOF'
"""
Модуль математической модели для сравнения вариантов доставки.
"""

from src.calculator import calculate_delivery_cost
from src.constants import DELIVERY_RATES


def compare_delivery_options(weight, distance):
    """
    Сравнивает все способы доставки и возвращает оптимальный.

    Аргументы:
        weight (float): вес запчасти в кг
        distance (float): расстояние доставки в км

    Возвращает:
        dict: информация о всех вариантах и оптимальном способе
    """
    results = {}

    for method_id, rates in DELIVERY_RATES.items():
        cost = calculate_delivery_cost(weight, distance, method_id)
        results[method_id] = {
            "name": rates["name"],
            "cost": cost
        }

    optimal_id = min(results.keys(), key=lambda x: results[x]["cost"])

    return {
        "all_options": results,
        "optimal": {
            "method_id": optimal_id,
            "name": results[optimal_id]["name"],
            "cost": results[optimal_id]["cost"]
        }
    }


def get_recommendation(weight, distance):
    """Возвращает рекомендацию по выбору способа доставки."""
    comparison = compare_delivery_options(weight, distance)
    optimal = comparison["optimal"]

    if optimal["cost"] == 0:
        return "Рекомендуется самовывоз — это бесплатно!"
    else:
        return f"Рекомендуется {optimal['name']} доставка. Стоимость: {optimal['cost']:.2f} руб"
EOF
