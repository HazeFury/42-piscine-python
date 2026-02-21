class GardenError(Exception):
    """Base class for error handling."""
    pass


class PlantError(GardenError):
    """Specialized class for error related to plants."""
    pass


class WaterError(GardenError):
    """Specialized class for error related to watering."""
    pass


def check_tomato_plant() -> None:
    """Simulate a problem with a plant."""
    raise PlantError("The tomato plant is wilting!")


def check_water_tank() -> None:
    """Simulate a problem with the water supply."""
    raise WaterError("Not enough water in the tank!")


def test_plants_errors() -> None:
    """Test different types of error on a garden with plant."""
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        check_tomato_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water_tank()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    actions = [check_tomato_plant, check_water_tank]

    for action in actions:
        try:
            action()
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_plants_errors()
