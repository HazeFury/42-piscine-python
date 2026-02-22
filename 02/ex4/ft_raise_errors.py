def check_plant_health(name: str, water_lvl: int, sunlight_hrs: int) -> str:
    """Checks if the plant parameters are valid or not."""
    if not name:
        raise ValueError("Plant name cannot be empty!")

    if water_lvl < 1:
        raise ValueError(f"Water level {water_lvl} is too low (min 1)")
    elif water_lvl > 10:
        raise ValueError(f"Water level {water_lvl} is too high (max 10)")

    if sunlight_hrs < 2:
        raise ValueError(f"Sunlight hours {sunlight_hrs} is too low (min 2)")
    elif sunlight_hrs > 12:
        raise ValueError(f"Sunlight hours {sunlight_hrs} is too high (max 12)")

    return f"Plant '{name}' is healthy!"


def test_plant_checks() -> None:
    """Tests to demonstrate error raising and handling."""
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        print(check_plant_health("", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        print(check_plant_health("tomato", 15, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 0))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
