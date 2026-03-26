Модуль ввода данных.
"""

def get_string_input(prompt, allow_empty=False):
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("⚠️ Поле не может быть пустым.")

def get_number_input(prompt, min_value=0, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"⚠️ Значение должно быть >= {min_value}")
                continue
            if max_value and value > max_value:
                print(f"⚠️ Значение должно быть <= {max_value}")
                continue
            return value
        except ValueError:
            print("⚠️ Введите число.")

def get_yes_no_input(prompt):
    while True:
        answer = input(f"{prompt} (д/н): ").lower().strip()
        if answer in ['д', 'да', 'y', 'yes']:
            return True
        if answer in ['н', 'нет', 'n', 'no']:
            return False
        print("⚠️ Введите 'д' или 'н'.")

def get_delivery_method():
    print("\n--- Способы доставки ---")
    print("1. Обычная доставка")
    print("2. Экспресс-доставка")
    print("3. Самовывоз")
    
    while True:
        try:
            choice = int(input("Выберите (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            print("⚠️ Выберите 1, 2 или 3.")
        except ValueError:
            print("⚠️ Введите число.")

def get_promocode():
    if get_yes_no_input("Есть ли промокод?"):
        return get_string_input("Введите промокод: ")
    return None

def get_part_info():
    print("\n" + "="*50)
    print("    КАЛЬКУЛЯТОР СТОИМОСТИ АВТОЗАПЧАСТИ")
    print("="*50)
    
    part_name = get_string_input("\nНазвание запчасти: ")
    base_price = get_number_input("Базовая цена (руб): ", min_value=0)
    weight = get_number_input("Вес (кг): ", min_value=0)
    
    delivery_method = get_delivery_method()
    
    distance = 0
    if delivery_method != 3:
        distance = get_number_input("Расстояние (км): ", min_value=0)
    
    urgent = get_yes_no_input("Срочная доставка? (+500 руб)")
    insurance = get_yes_no_input("Страховка? (+5% от суммы)")
    promocode = get_promocode()
    
    return {
        "part_name": part_name,
        "base_price": base_price,
        "weight": weight,
        "distance": distance,
        "delivery_method": delivery_method,
        "urgent": urgent,
        "insurance": insurance,
        "promocode": promocode
    }

def display_result(result):
    print("\n" + "="*50)
    print("            РЕЗУЛЬТАТ РАСЧЁТА")
    print("="*50)
    print(f"📦 Запчасть: {result['part_name']}")
    print(f"💰 Базовая цена: {result['base_price']:.2f} руб")
    print(f"🚚 Доставка: {result['delivery_cost']:.2f} руб")
    
    if result['discount'] > 0:
        print(f"🎁 Скидка {result['promocode_applied']}: -{result['discount']:.2f} руб")
    
    if result['insurance_cost'] > 0:
        print(f"🛡️ Страховка: +{result['insurance_cost']:.2f} руб")
    
    if result['urgent_fee'] > 0:
        print(f"⚡ Срочность: +{result['urgent_fee']:.2f} руб")
    
    print("-"*50)
    print(f"💵 ИТОГО: {result['total']:.2f} руб")
    print("="*50)




