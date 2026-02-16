class SecurePlant():
    """Represent a plant object with secured data."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize data for new object."""
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def __str__(self) -> str:
        """Show all data of this plant."""
        return f"{self.name} ({self.__height}cm, {self.__age} days)"

    def get_height(self) -> int:
        """Return the height of this plant."""
        return self.__height

    def set_height(self, new_height: int) -> None:
        """Set the height (in cm) of this plant. Minimum = 0cm."""
        if new_height < 0:
            print("Invalid operation attempted: ", end="")
            print(f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = new_height
        print(f"Height updated: {new_height}cm [OK]")

    def get_age(self) -> int:
        """Return the age of this plant."""
        return self.__age

    def set_age(self, new_age: int) -> None:
        """Set the age (in days) of this plant. Minimum = 0 day."""
        if new_age < 0:
            print("Invalid operation attempted: ", end="")
            print(f"age {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = new_age
        print(f"Age updated: {new_age} days [OK]")


def main() -> None:
    print("=== Garden Security System ===")

    a = SecurePlant("Rose", 25, 30)
    print("")
    a.set_height(-5)
    print("")
    print("Current plant:", a)


if __name__ == "__main__":
    main()
