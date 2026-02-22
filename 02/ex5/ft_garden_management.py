class GardenError(Exception):
    """Base class for error handling."""
    pass


class WaterError(GardenError):
    """Specialized class for error related to watering."""
    pass


class GardenManager:
    """Manages the garden operations and handles related errors."""
    def __init__(self) -> None:
        """Initialize an empty garden."""
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        """Adds a plant to the garden."""
        if not name:
            raise ValueError("Plant name cannot be empty!")

        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Waters all plants safely, ensuring the system is always closed."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str, water: int, sun: int) -> None:
        """Checks if a plant's conditions are healthy."""
        e: str = f"Error checking {name}:"
        if water < 1:
            raise ValueError(f"{e} Water level {water} is too low (min 1)")
        elif water > 10:
            raise ValueError(f"{e} Water level {water} is too high (max 10)")

        if sun < 2:
            raise ValueError(f"{e} Sunlight hours {sun} is too low (min 2)")
        elif sun > 12:
            raise ValueError(f"{e} Sunlight hours {sun} is too high (max 12)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")

    def check_tank(self) -> None:
        """Simulates a critical garden system failure."""
        raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    """Demonstrates all error handling concepts integrated together."""
    print("=== Garden Management System ===\n")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except ValueError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    try:
        manager.check_health("tomato", 5, 8)
        manager.check_health("lettuce", 15, 8)
    except ValueError as e:
        print(e)

    print("\nTesting error recovery...")
    try:
        manager.check_tank()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
