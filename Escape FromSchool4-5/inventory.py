class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            print(f"✓ Вы подобрали: {item}")
        else:
            print(f"У вас уже есть {item}.")

    def has_item(self, item):
        return item in self.items

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"✗ Вы использовали: {item}")
            return True
        return False

    def show_items(self):
        if self.items:
            print("🎒 Ваш инвентарь:", ", ".join(self.items))
        else:
            print("Ваш инвентарь пуст.")
