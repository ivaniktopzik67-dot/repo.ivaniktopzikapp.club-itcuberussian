import json
import os
from inventory import Inventory
from utils import save_game, load_game, show_help

def load_story():
    """Загружает сюжет из JSON‑файла."""
    with open('story.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def show_scene(scene_data, inventory):
    """Отображает сцену и доступные варианты действий."""
    print("\n" + scene_data['text'])

    # Автоматически подбираем предметы, если они указаны в сцене
    if 'items' in scene_data:
        for item in scene_data['items']:
            inventory.add_item(item)

    # Показываем варианты действий
    for i, option in enumerate(scene_data['options'], 1):
        # Проверяем условие наличия предмета, если оно задано
        if 'condition' in option:
            condition_item = option['condition'].split(':')[1]
            if not inventory.has_item(condition_item):
                continue  # Пропускаем вариант, если предмета нет
        print(f"{i}. {option['text']}")

def main():
    story = load_story()
    current_scene = 'start'
    inventory = Inventory()

    print("Добро пожаловать в «Побег из школы 4–5: Грандиозный финал»!")
    print("Введите 'help' для списка команд.")

    while current_scene:
        scene_data = story[current_scene]
        show_scene(scene_data, inventory)

        # Если в сцене нет вариантов — это финал
        if not scene_data['options']:
            break

        command = input("\nВаш выбор (номер или команда): ").strip().lower()

        # Обрабатываем команды
        if command == 'save':
            save_game(current_scene, inventory.items)
            continue
        elif command == 'load':
            loaded_scene, loaded_items = load_game()
            if loaded_scene:
                current_scene = loaded_scene
                inventory.items = loaded_items
            continue
        elif command == 'inv':
            inventory.show_items()
            continue
        elif command == 'help':
            show_help()
            continue

        # Обработка выбора варианта
        try:
            choice = int(command) - 1
            # Получаем все доступные варианты (с учётом условий)
            available_options = []
            for option in scene_data['options']:
                if 'condition' in option:
                    condition_item = option['condition'].split(':')[1]
                    if inventory.has_item(condition_item):
                        available_options.append(option)
                else:
                    available_options.append(option)

            if 0 <= choice < len(available_options):
                current_scene = available_options[choice]['next_scene']
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите номер варианта или команду.")

if __name__ == "__main__":
    main()
