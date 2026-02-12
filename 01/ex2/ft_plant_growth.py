class Plant():
    """Represent a plant object."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize data for new object."""
        self.name = name
        self.height = height
        self.age = age

    def display_data(self) -> None:
        """Display information about this plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow_height(self) -> None:
        """Increase height by 1cm."""
        self.height += 1

    def grow_age(self) -> None:
        """Increase age by 1."""
        self.age += 1


def main() -> None:
    days = 7
    a = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    a.display_data()
    for day in range(1, days, 1):
        a.grow_height()
        a.grow_age()
    else:
        print(f"=== Days {day + 1} ===")
        a.display_data()
        print(f"Growth this week: +{day}cm")


if __name__ == "__main__":
    main()
