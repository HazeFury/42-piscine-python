class SecurePlant():
    """Represent a plant object with secured data."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize data for new object."""
        self.name = name
        self.__height = height
        self.__age = age

    def display_data(self) -> None:
        """Show all data of this plant."""
        print(f"{self.name}: {self.__height}cm, {self.__age} days old")

    def get_height(self):
        """Return the height of this plant"""
        return self.__height

    def set_height(self, new_height: int):
        """Set the height of this plant (in cm). Min = 0m and max = 50m"""
        if new_height < 0 or new_height > 5000:
            print("ERROR: height cannot be negative or superior to 5000 !")
            return
        self.__height = new_height

    def get_age(self):
        """Return the age of this plant"""
        return self.__age

    def set_age(self, new_age: int):
        """Set the age of this plant (in days). Min = 0 day and no maximum"""
        if new_age < 0:
            print("ERROR: age cannot be negative !")
            return
        self.__age = new_age


def main() -> None:
    print("=== Garden Security System ===")
    a = SecurePlant("Rose", 5, -2)

    a.display_data()

    a.set_age(8)

    a.display_data()


if __name__ == "__main__":
    main()
