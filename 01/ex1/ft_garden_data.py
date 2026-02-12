class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_data(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    a = Plant("Rose", 25, 30)
    b = Plant("Sunflower", 80, 45)
    c = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    a.display_data()
    b.display_data()
    c.display_data()


if __name__ == "__main__":
    main()
