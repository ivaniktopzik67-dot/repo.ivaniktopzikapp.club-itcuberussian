import game_data
import time

class Game:
    def __init__(self):
        self.current_location = "main_room"
        self.inventory = []
        self.time_left = 60  # минуты до заката

    def show_status(self):
        print(f"\n⏰ До заката осталось: {self.time_left} минут")
        print(f"🎒 Инвентарь: {', '.join(self.inventory) if self.inventory else 'пусто'}")
        print(game_data.LOCATIONS[self.current_location]["description"])

    def move(self, direction):
        locations = game_data.LOCATIONS
        if direction in locations[self.current_location]["exits"]:
            self.current_location = locations[self.current_location]["exits"][direction]
            self.time_left -= 5
            return True
        else:
            print("Туда нельзя пойти!")
            return False

    def play(self):
        print("=== ПОБЕГ ИЗ ДОМА НА ДЕРЕВЕ ===")
        print("Вы должны выбраться до заката!\n")

        while self.time_left > 0:
            self.show_status()
            command = input("\nЧто делать? > ").lower().strip()

            if command in ["вверх", "на чердак"]:
                self.move("attic")
            elif command in ["вниз", "в подвал"]:
                self.move("basement")
            elif command == "осмотреться":
                print(game_data.LOCATIONS[self.current_location]["description"])
            elif command.startswith("взять "):
                item = command[5:]
                if item in game_data.LOCATIONS[self.current_location]["items"]:
                    self.inventory.append(item)
                    game_data.LOCATIONS[self.current_location]["items"].remove(item)
                    print(f"Вы взяли {item}!")
                else:
                    print("Этого здесь нет.")
            elif command == "выход":
                print("Спасибо за игру!")
                break
            else:
                print("Не понимаю команду.")

            if self.time_left <= 0:
                print("\n❌ Солнце село! Вы не успели выбраться!")
                break

if __name__ == "__main__":
    game = Game()
    game.play()
