import sys


def parse_args_to_dict(args: list[str]) -> dict[str, int]:
    """Converts command line arguments 'item:qty' into a dictionary."""
    inventory: dict[str, int] = dict()
    for arg in args:
        parts: list[str] = arg.split(":")
        if len(parts) == 2:
            key: str = parts[0]
            val: int = int(parts[1])
            inventory.update({key: val})
    return inventory


def sort_inventory(inv: dict[str, int]) -> dict[str, int]:
    """Sorts the dictionary by values descending."""
    sorted_inv: dict[str, int] = dict()
    processed_keys: dict[str, bool] = dict()

    for _ in inv:
        highest_k: str = ""
        highest_v: int = -1

        for key, val in inv.items():
            if val > highest_v and processed_keys.get(key, False) is False:
                highest_v = val
                highest_k = key

        sorted_inv.update({highest_k: highest_v})
        processed_keys.update({highest_k: True})

    return sorted_inv


def main() -> None:
    """Show the demonstration of inventory management."""
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty item:qty ...")
        return

    inventory = parse_args_to_dict(sys.argv[1:])

    if len(inventory) == 0:
        print("Error : no item in inventory")
        return

    # ################  Inventory System Analysis  #################
    total_items: int = 0
    for val in inventory.values():
        total_items += val

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")

    # ####################  Current Inventory  #####################
    print("=== Current Inventory ===")
    sorted_inventory: dict[str, int] = sort_inventory(inventory)

    most_abundant_k: str = ""
    most_abundant_v: int = -1
    least_abundant_k: str = ""
    least_abundant_v: float | int = float('inf')

    for key, value in sorted_inventory.items():
        percentage: float = (value / total_items) * 100
        unit_str: str = "unit" if value == 1 else "units"
        print(f"{key}: {value} {unit_str} ({percentage:.1f}%)")

        if value > most_abundant_v:
            most_abundant_v = value
            most_abundant_k = key
        if value < least_abundant_v:
            least_abundant_v = value
            least_abundant_k = key

    # ##################  Inventory Statistics  ###################
    print("\n=== Inventory Statistics ===")
    unit_str_max: str = "unit" if most_abundant_v == 1 else "units"
    unit_str_min: str = "unit" if least_abundant_v == 1 else "units"

    print(f"Most abundant: {most_abundant_k} ({most_abundant_v}"
          f" {unit_str_max})")
    print(f"Least abundant: {least_abundant_k} ({least_abundant_v}"
          f" {unit_str_min})\n")

    categories: dict[str, dict[str, int]] = dict()
    categories.update({"Moderate": dict()})
    categories.update({"Scarce": dict()})

    restock_needed: list[str] = []

    for key, value in inventory.items():
        if value >= 5:
            categories["Moderate"].update({key: value})
        else:
            categories["Scarce"].update({key: value})

        if value == 1:
            restock_needed.append(key)

    print("=== Item Categories ===")
    for cat_name, cat_dict in categories.items():
        print(f"{cat_name}: {cat_dict}")

    # ################  Management Suggestions  #################
    print("\n=== Management Suggestions ===")
    need: str = ', '.join(restock_needed) if len(restock_needed) > 0 else "No"
    print(f"Restock needed: {need}\n")

    # ##############  Dictionary Properties Demo  ###############
    print("=== Dictionary Properties Demo ===")
    has_sword: bool = inventory.get("sword") is not None

    keys_list: list[str] = []
    values_list: list[str] = []
    for key, value in inventory.items():
        keys_list.append(key)
        values_list.append(str(value))

    print(f"Dictionary keys: {', '.join(keys_list)}")
    print(f"Dictionary values: {', '.join(values_list)}")
    print(f"Sample lookup - 'sword' in inventory: {has_sword}")


if __name__ == "__main__":
    main()
