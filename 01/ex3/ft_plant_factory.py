from typing import TypedDict


class PlantType(TypedDict):
    """Define the type structure of a plant"""
    name: str
    height: int
    age: int


class Plant():
    """Represent a plant object."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize data for new object."""
        self.name = name
        self.height = height
        self.age = age

    def display_data(self) -> None:
        """Show all data of this plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class PlantFactory():
    @staticmethod
    def create_plants(plant_array: list[PlantType]) -> list[Plant]:
        """Creates multiple Plant objects from a list of dictionaries."""
        garden = []
        for plant in plant_array:
            new = Plant(plant["name"], plant["height"], plant["age"])
            garden.append(new)
            print(f"Created: {new.name} ({new.height}cm, {new.age} days)")
        print(f"\nTotal plants created: {len(garden)}")
        return garden


def main() -> None:
    plants_to_create: list[PlantType] = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120}]

    my_garden = PlantFactory.create_plants(plants_to_create)

    print("\n=== My Garden ===")
    for each_plant in my_garden:
        each_plant.display_data()


if __name__ == "__main__":
    main()
