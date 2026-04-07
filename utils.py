import time
import random

def clear_screen():
    """Очищает экран консоли (кросс‑платформенно)."""
    print("\n" * 50)  # Простой способ очистить экран в консоли

def slow_print(text, delay=0.03):
    """
    Печатает текст посимвольно с задержкой для драматического эффекта.
    
    Args:
        text (str): текст для вывода;
        delay (float): задержка между символами в секундах.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Новая строка в конце

def get_input(prompt="> "):
    """
    Получает ввод от пользователя с обработкой ошибок.
    
    Args:
        prompt (str): приглашение к вводу.
    Returns:
        str: очищенный ввод пользователя.
    """
    try:
        return input(prompt).strip().lower()
    except KeyboardInterrupt:
        print("\n\nИгра прервана. До свидания!")
        exit()

def validate_puzzle_answer(user_answer, correct_answer):
    """
    Проверяет ответ игрока на головоломку.
    
    Args:
        user_answer (str): ответ игрока;
        correct_answer (str): правильный ответ.
    Returns:
        bool: True, если ответ верный.
    """
    return user_answer.strip().lower() == correct_answer.lower()

def show_inventory(inventory):
    """
    Показывает содержимое инвентаря игрока.
    
    Args:
        inventory (list): список предметов в инвентаре.
    """
    if inventory:
        print("🎒 Ваш инвентарь:")
        for item in inventory:
            print(f"  • {item}")
    else:
        print("🎒 Инвентарь пуст.")

def show_location_info(location_data):
    """
    Отображает информацию о текущей локации.
    
    Args:
        location_data (dict): данные локации из game_data.
    """
    print(f"\n📍 Вы находитесь: {location_data['name']}")
    print(f"{location_data['description']}")

    if location_data.get("items"):
        items_list = ', '.join(location_data["items"])
        print(f"На полу лежат: {items_list}")

    exits_list = ", ".join(location_data["exits"].keys())
    print(f"Доступные выходы: {exits_list}")

def trigger_trap():
    """
    Активирует случайную ловушку. Возвращает потерю времени и сообщение.
    
    Returns:
        tuple: (потеря времени в минутах, сообщение о ловушке).
    """
    traps = [
        ("Вы зацепили растяжку! Приходится распутывать.", 10),
        ("Пол под вами заскрипел и прогнулся. Осторожно обходите опасный участок.", 8),
        ("Сверху посыпались сухие листья и ветки, мешая идти.", 5),
        ("Ловушка с сетью! Выпутаться удалось, но время потеряно.", 12)
    ]
    trap_msg, time_loss = random.choice(traps)
    return time_loss, trap_msg

def check_time(time_left):
    """
    Проверяет оставшееся время и выдаёт предупреждения.
    
    Args:
        time_left (int): оставшееся время в минутах.
    Returns:
        str: статус времени.
    """
    if time_left > 45:
        return "☀️ Солнце ещё высоко. У вас достаточно времени."
    elif time_left > 30:
        return "🌤️ Солнце начинает клониться к закату."
    elif time_left > 15:
        return "🌇 Небо становится оранжевым. Спешите!"
    else:
        return "🌆 Сумерки сгущаются! Осталось совсем немного времени!"

def save_game(game_state, filename="savegame.dat"):
    """
    Сохраняет состояние игры в файл (упрощённо).
    
    Args:
        game_state (dict): состояние игры для сохранения;
        filename (str): имя файла для сохранения.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for key, value in game_state.items():
                f.write(f"{key}:{value}\n")
        print("✅ Игра сохранена!")
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")

def load_game(filename="savegame.dat"):
    """
    Загружает состояние игры из файла.
    
    Args:
        filename (str): имя файла для загрузки.
    Returns:
        dict: загруженное состояние игры или None при ошибке.
    """
    try:
        game_state = {}
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split(':', 1)
                game_state[key] = value
        print("✅ Игра загружена!")
        return game_state
    except FileNotFoundError:
        print("❌ Файл сохранения не найден.")
        return None
    except Exception as e:
        print(f"❌ Ошибка при загрузке: {e}")
        return None
