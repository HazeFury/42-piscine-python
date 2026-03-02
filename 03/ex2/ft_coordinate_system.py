import sys
import math


def calc_distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    """Calculates the distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


def parse_coordinate_str(coord_str: str) -> tuple[int, int, int] | None:
    """Parses a string like 'x,y,z' into a tuple of integers."""
    try:
        parts = coord_str.split(',')

        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])

        return (x, y, z)

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def main() -> None:
    """Demonstrate the calul between two 3D points"""
    print("=== Game Coordinate System ===\n")

    origin: tuple[int, int, int] = (0, 0, 0)

    try:
        if len(sys.argv) > 1:
            if len(sys.argv) > 2:
                raise ValueError("Error : too much arguments !")
            else:
                str = sys.argv[1]
                pos1: tuple[int, int, int] = parse_coordinate_str(str)
        else:
            pos1 = (10, 20, 5)
    except Exception as e:
        print(e)
        return
    print(f"Position created: {pos1}")
    dist1 = calc_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {round(dist1, 2)}\n")

    coord_str_valid = "3,4,0"
    print(f'Parsing coordinates: "{coord_str_valid}"')
    pos2 = parse_coordinate_str(coord_str_valid)

    if pos2 is not None:
        print(f"Parsed position: {pos2}")
        dist2 = calc_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {round(dist2, 1)}\n")

    coord_str_invalid = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{coord_str_invalid}"')
    parse_coordinate_str(coord_str_invalid)
    print()

    print("Unpacking demonstration:")
    if pos2 is not None:
        x, y, z = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
