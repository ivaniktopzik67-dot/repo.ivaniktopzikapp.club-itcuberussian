import json
import os

def save_game(current_scene, inventory_items):
    save_data = {
        'scene': current_scene,
        'inventory': inventory_items
    }
    with open('saves/save_game.json', 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)
    print("✅ Игра сохранена!")

def load_game():
    if os.path.exists('saves/save_game.json'):
        with open('saves/save_game.json', 'r', encoding='utf-8') as f:
            save_data = json.load(f)
        print("✅ Игра загружена!")
        return save_data['scene'], save_data['inventory']
    else:
        print("❌ Сохранения не найдены.")
        return None, []

def show_help():
    print("""
📋 Доступные команды:
1–3 — выбрать вариант действия
save — сохранить игру
load — загрузить сохранение
inv — показать инвентарь
help — показать эту справку
"")
