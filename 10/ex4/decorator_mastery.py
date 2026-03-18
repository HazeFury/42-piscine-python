import time
from functools import wraps
from typing import Callable, Any

# ==============================================================================
#   SPELL TIMER
# ==============================================================================


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints the execution time of a function."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        start_time: float = time.time()
        result: Any = func(*args, **kwargs)
        end_time: float = time.time()

        execution_time: float = end_time - start_time
        print(f"Spell completed in {execution_time:.8f} seconds")

        return result
    return wrapper


# ==============================================================================
#   POWER VALIDATOR
# ==============================================================================

def power_validator(
        min_power: int
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory that checks if the caster has sufficient power."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            power: int | None = None

            if 'power' in kwargs:
                power = kwargs['power']
            else:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break

            if power is None and args:
                power = args[0]

            if isinstance(power, int):
                if power >= min_power:
                    return func(*args, **kwargs)
                else:
                    return "Insufficient power for this spell"
            else:
                return "[ERROR]: Wrong or no value for power"

        return wrapper
    return decorator


# ==============================================================================
#   RETRY SPELL
# ==============================================================================

def retry_spell(
        max_attempts: int
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory that retries a failed spell up to max_attempts."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying..."
                          f"(attempt {attempt}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


# ==============================================================================
#   MAGE GUILD
# ==============================================================================

class MageGuild:
    """A guild handling mage registrations and spell casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validates if a name is at least 3 chars and only letters/spaces."""
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Casts a spell if the power validation passes."""
        return f"Successfully cast {spell_name} with {power} power"


# ==============================================================================
#   TEST FUNCTIONS
# ==============================================================================

@spell_timer
def fireball() -> str:
    """Simulates a complex spell casting with a slight delay."""
    time.sleep(0.1)
    return "Result: Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_summoning() -> str:
    """A spell that always fails to demonstrate the retry mechanism."""
    raise ValueError("The portal collapsed!")


# ==============================================================================
#   MAIN
# ==============================================================================

def main() -> None:
    print("============= SPELL TIMER =============")
    print("# Testing spell timer...")
    print(fireball())

    print("\n============= MAGE GUILD =============")
    print("# Testing MageGuild validate name...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("42"))

    print("\n# Testing MageGuild power validator...")
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Meteor", power=5))
    print(guild.cast_spell("Fireball"))

    print("\n============= RETRY SPELL =============")
    print("# Testing retry spell...")
    print(unstable_summoning())


if __name__ == "__main__":
    main()
