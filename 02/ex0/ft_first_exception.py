def check_temperature(temp_str: str) -> int | None:
    """Check temperature received in arg and returns it as int if valid"""
    print(f"Testing temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int


def test_temperature_input() -> None:
    """Test the 'check_temperature()' function with differents values"""
    try:
        print("=== Garden Temperature Checker ===\n")
        check_temperature("25")
        print()
        check_temperature("abc")
        print()
        check_temperature("100")
        print()
        check_temperature("-50")
    except Exception as e:
        print(f"\nTests failed, program crashed : {e}")
    else:
        print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
