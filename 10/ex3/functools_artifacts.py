import operator
import time
from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any

# ==============================================================================
# 1. REDUCE
# ==============================================================================


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers into a single value based on operation."""
    if not spells:
        return 0

    try:
        if operation == "add":
            return reduce(operator.add, spells)
        elif operation == "multiply":
            return reduce(operator.mul, spells)
        elif operation == "min":
            return reduce(min, spells)
        elif operation == "max":
            return reduce(max, spells)
        else:
            print(f"Unknown operation: {operation}")
            return 0
    except Exception as e:
        print(f"Error during reduction: {e}")
        return 0


# ==============================================================================
# 2. PARTIAL
# ==============================================================================

def enchantment(power: int, element: str, target: str) -> str:
    """Base generic spell to be specialized."""
    return f"Enchanting {target} with {element} magic at {power} power level"


def partial_enchanter(
        base_enchantment: Callable[..., str]
        ) -> dict[str, Callable[[str], str]]:
    """Create a dictionary of pre-configured enchantment spells."""
    fire_spell: Callable[[str], str] = partial(base_enchantment, 50, "Fire")
    ice_spell: Callable[[str], str] = partial(base_enchantment, 50, "Ice")
    light_spell: Callable[[str], str] = partial(base_enchantment, 50, "Light")

    return {
        'fire_enchant': fire_spell,
        'ice_enchant': ice_spell,
        'lightning_enchant': light_spell
    }


# ==============================================================================
# 3. LRU_CACHE
# ==============================================================================

@lru_cache(maxsize=150)
def memoized_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number, accelerated by memoization."""
    if n < 0:
        return 0
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# ==============================================================================
# 4. SINGLEDISPATCH
# ==============================================================================

@singledispatch
def spell_dispatcher(target: Any) -> str:
    """Default fallback spell if the target type is unknown."""
    return "Casting generic spell on mysterious entity" \
           f" of type: {type(target).__name__}"


@spell_dispatcher.register(str)
def _(target: str) -> str:
    """Specialized spell for String targets."""
    return f"Casting verbal spell on {target}"


@spell_dispatcher.register(int)
def _(target: int) -> str:
    """Specialized spell for Integer targets."""
    return f"Casting physical spell with {target} raw damage"


@spell_dispatcher.register(list)
def _(target: list[Any]) -> str:
    """Specialized spell for List targets."""
    return f"Casting Area of Effect spell hitting {len(target)} targets"


# ==============================================================================
# MAIN
# ==============================================================================

def main() -> None:
    """Demonstrate the usage of Ancient Library artifacts."""

    # ============= REDUCE =============
    print("============= SPELL REDUCER =============")
    print("# Testing spell reducer on a list...")
    power_list: list[int] = [2, 4, 6, 8]
    print(f"Base powers: {power_list}")
    print(f"Sum (add): {spell_reducer(power_list, 'add')}")
    print(f"Product (multiply): {spell_reducer(power_list, 'multiply')}")
    print(f"Max power: {spell_reducer(power_list, 'max')}")

    # ============= PARTIAL =============
    print("\n============= PARTIAL ENCHANTER =============")
    print("# Testing partial enchanter function...")
    grimoire: dict[str, Callable[[str], str]] = partial_enchanter(enchantment)

    print(grimoire['fire_enchant']("Sword"))
    print(grimoire['ice_enchant']("Shield"))
    print(grimoire['lightning_enchant']("Staff"))

    # ============= LRU CACHE =============
    print("\n============= LRU CACHE =============")
    print("# Testing Fibonacci sequence with cache...")

    start_time: float = time.time()
    result1: int = memoized_fibonacci(100)
    end_time: float = time.time()
    print(f"First call (fibonacci 100): {result1}")
    print(f"Time taken (Computing): {end_time - start_time:.8f} seconds")

    start_time2: float = time.time()
    result2: int = memoized_fibonacci(100)
    end_time2: float = time.time()
    print(f"\nSecond call (fibonacci 100): {result2}")
    print(f"Time taken (Cached): {end_time2 - start_time2:.8f} seconds")
    print("-> That's the power of memoization!")

    # ============= SINGLEDISPATCH =============
    print("\n============= SINGLEDISPATCH =============")
    print("# Testing dispatch spell with different types...")

    print(spell_dispatcher("The Dragon"))
    print(spell_dispatcher(42))
    print(spell_dispatcher(["Goblin", "Orc"]))
    print(spell_dispatcher({"name": "Arthur"}))


if __name__ == "__main__":
    main()
