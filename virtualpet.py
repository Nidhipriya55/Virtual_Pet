import time

class VirtualPet:
    def __init__(self, name):  # Corrected the typo in __init__
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger <= 90:
            self.hunger += 10
        else:
            self.hunger = 100
        print(f"{self.name} is eating...")

    def sleep(self):
        if self.energy <= 90:
            self.energy += 10
        else:
            self.energy = 100
        print(f"{self.name} is sleeping...")

    def play(self):  # Fixed indentation
        if self.energy >= 10 and self.hunger >= 10:
            self.happiness += 10
            self.energy -= 10
            self.hunger -= 10
            if self.happiness > 100:
                self.happiness = 100
            print(f"{self.name} is playing!")
        else:
            print(f"{self.name} is too tired or hungry to play.")

    def status(self):
        print("\n--- Status ---")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/100")
        print(f"Energy: {self.energy}/100")
        print(f"Happiness: {self.happiness}/100")

    def update(self):
        self.hunger -= 5
        self.energy -= 5
        self.happiness -= 2

        if self.hunger < 0:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0
        if self.happiness < 0:
            self.happiness = 0

        if self.hunger == 0 or self.energy == 0 or self.happiness == 0:
            print(f"\n{self.name} is not doing well. Please take care!")

def main():
    name = input("What would you like to name your pet? ")
    pet = VirtualPet(name)

    while True:
        pet.status()
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.sleep()
        elif choice == '3':
            pet.play()
        elif choice == '4':
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Invalid choice. Try again.")

        pet.update()
        time.sleep(1)

if __name__ == "__main__":  # Corrected if statement for script execution
    main()
