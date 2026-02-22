def water_plants(plant_list: list[str | None]) -> bool:
    """Water every plants given from an array of plant."""
    print("Opening watering system")
    success = False

    try:
        for plant in plant_list:
            if plant is None:
                raise TypeError("Cannot water None - invalid plant!")

            print(f"Watering {plant}")
        success = True
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"==> Unexpected Error : {e}")
    finally:
        print("Closing watering system (cleanup)")

    return success


def test_watering_system() -> None:
    """Test watering the plants with different arrays of plant."""
    valid_plant_list: list[str] = ["tomato", "lettuce", "carrots"]
    invalid_plant_list: list[str | None] = ["tomato", None, "carrots"]

    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    if water_plants(valid_plant_list):
        print("Watering completed successfully!")

    print("\nTesting with error...")
    if water_plants(invalid_plant_list):
        print("Watering completed successfully!")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
