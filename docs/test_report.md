cat > docs/test_report.md << 'EOF'
# Отчёт о тестировании

## Дата тестирования
26 марта 2026 года

## Среда тестирования
- Python 3.12.1
- ОС: Ubuntu (GitHub Codespaces)
- Фреймворк: pytest 9.0.2

## Результаты модульных тестов

| № | Название теста | Результат |
|---|----------------|----------|
| 1 | test_apply_insurance_false | ✅ PASS |
| 2 | test_apply_insurance_true | ✅ PASS |
| 3 | test_apply_promocode_empty | ✅ PASS |
| 4 | test_apply_promocode_invalid | ✅ PASS |
| 5 | test_apply_promocode_sale10 | ✅ PASS |
| 6 | test_apply_promocode_sale20 | ✅ PASS |
| 7 | test_apply_urgent_false | ✅ PASS |
| 8 | test_apply_urgent_true | ✅ PASS |
| 9 | test_calculate_delivery_cost_express | ✅ PASS |
| 10 | test_calculate_delivery_cost_pickup | ✅ PASS |
| 11 | test_calculate_delivery_cost_regular | ✅ PASS |
| 12 | test_calculate_total | ✅ PASS |

**Всего тестов:** 12
**Пройдено:** 12
**Провалено:** 0
**Успешность:** 100%

## Вывод
Все модульные тесты пройдены успешно. Программа работает корректно и соответствует требованиям.
EOF
