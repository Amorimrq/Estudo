import random
import time

class Car:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.start_boost = self.get_start_boost()

    def get_start_boost(self):
        chance = random.random()
        if chance < 0.2:
            print(f"{self.name} teve uma má largada!")
            return -2  # má largada
        elif chance > 0.8:
            print(f"{self.name} teve uma boa largada!")
            return 3   # boa largada
        else:
            return 0   # largada normal

    def move(self):
        vacuo = 2 if random.random() < 0.1 else 0  # 10% de chance de vácuo
        move = random.randint(1, 6) + vacuo
        if self.position == 0:
            move += self.start_boost
            self.start_boost = 0  # só aplica na largada
        self.position += max(move, 0)

def race(cars, finish_line=50):
    print("Corrida iniciada!\n")
    while True:
        for car in cars:
            car.move()
            print(f"{car.name}: {'-' * car.position}>")
            if car.position >= finish_line:
                print(f"\n{car.name} venceu a corrida!")
                return
        print("-" * 60)
        time.sleep(0.5)

if __name__ == "__main__":
    nomes = ["Carro A", "Carro B", "Carro C"]
    carros = [Car(nome) for nome in nomes]
    race(carros)