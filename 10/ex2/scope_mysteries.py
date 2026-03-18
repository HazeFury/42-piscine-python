from typing import Callable, Any

# ==============================================================================
#   MAGE COUNTER
# ==============================================================================


def mage_counter() -> Callable[[], int]:
    """Create a closure that counts how many times it's been called."""
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter

# ==============================================================================
#   SPELL ACCUMULATOR
# ==============================================================================


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Create a power accumulator closure starting from initial_power."""
    total_power: int = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return accumulator

# ==============================================================================
#   ENCHANTEMENT FACTORY
# ==============================================================================


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Create an enchantment function using the provided enchantment_type."""

    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return apply_enchantment

# ==============================================================================
#   MEMORY VALUT
# ==============================================================================


def memory_vault() -> dict[str, Callable[..., Any]]:
    """Create a memory management system with private storage closure."""
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }

# ==============================================================================
#   MAIN
# ==============================================================================


def main() -> None:
    """Demonstrate the usage of Memory Depths closures."""

    print("============= MAGE COUNTER =============")
    print("# Testing mage counter...")
    my_counter: Callable[[], int] = mage_counter()

    print(f"Call 1: {my_counter()}")
    print(f"Call 2: {my_counter()}")
    print(f"Call 3: {my_counter()}")

    another_counter: Callable[[], int] = mage_counter()
    print(f"New counter Call 1: {another_counter()}")

    print("\n============= SPELL ACCUMULATOR =============")
    print("# Testing spell accumulator (Starting at 100)...")
    accumulate: Callable[[int], int] = spell_accumulator(100)

    print(f"Adding 50: {accumulate(50)}")
    print(f"Adding 20: {accumulate(20)}")
    print(f"Adding 5: {accumulate(5)}")

    print("\n============= ENCHANTMENT FACTORY =============")
    print("# Testing enchantment factory...")
    fire_enchanter: Callable[[str], str] = enchantment_factory("Flaming")
    ice_enchanter: Callable[[str], str] = enchantment_factory("Frozen")

    print(fire_enchanter("Sword"))
    print(ice_enchanter("Shield"))
    print(fire_enchanter("Axe"))

    print("\n============= MEMORY VAULT =============")
    print("# Testing memory vault...")
    vault_interface: dict[str, Callable[..., Any]] = memory_vault()

    store_spell: Callable[..., Any] = vault_interface['store']
    recall_spell: Callable[..., Any] = vault_interface['recall']

    store_spell("first_spell", "Fireball")
    store_spell("secret_code", 42)

    print(f"Recalling 'first_spell': {recall_spell('first_spell')}")
    print(f"Recalling 'secret_code': {recall_spell('secret_code')}")
    print(f"Recalling 'unknown': {recall_spell('unknown')}")


if __name__ == "__main__":
    main()
