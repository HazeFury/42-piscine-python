class Plant():
    """Represent a plant object."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        """Return a string with all data of this plant."""
        return (f"{self.name} ({self.__class__.__name__}): " +
                f"{self.height}cm, {self.age} days")


class Flower(Plant):
    """Represent a flower object."""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Indicate if this flower grows well."""
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        """Show all data of this plant."""
        return super().__str__() + f", {self.color} color"


class Tree(Plant):
    """Represent a tree object."""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate shade area based on tree height."""
        shade_radius = self.height / 100
        area = 3.14 * (shade_radius ** 2)
        print(f"Oak provides {int(area)} square meters of shade")

    def __str__(self) -> str:
        """Show all data of this plant."""
        return super().__str__() + f", {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Represent a vegetable object."""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_nutritional_info(self) -> None:
        """Show the nutritional information of this vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def __str__(self) -> str:
        """Show all data of this plant."""
        return super().__str__() + f", {self.harvest_season} harvest"


def main() -> None:
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

    sunflower = Flower("Sunflower", 150, 60, "yellow")
    pine = Tree("Pine", 1200, 3650, 40)
    spinach = Vegetable("Spinach", 20, 45, "spring", "iron")

    garden: list[Plant] = [rose, oak, tomato, sunflower, pine, spinach]

    for plant in garden:
        print(plant)

        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            plant.display_nutritional_info()
        print()


if __name__ == "__main__":
    main()
