from typing import Callable, Any

# ==============================================================================
#   SPELL COMBINER
# ==============================================================================

def spell_combiner(
        spell1: Callable[..., Any], spell2: Callable[..., Any]
        ) -> Callable[..., tuple[Any, Any]]:
    """Combine two spells into a single new spell returning a tuple of
    both results."""

    def combined_spell(*args: Any, **kwargs: Any) -> tuple[Any, Any]:
        res1: Any = spell1(*args, **kwargs)
        res2: Any = spell2(*args, **kwargs)

        return (res1, res2)

    return combined_spell

# ==============================================================================
#   POWER AMPLIFIER
# ==============================================================================

def power_amplifier(
        base_spell: Callable[..., int | float], multiplier: int
        ) -> Callable[..., int | float]:
    """Amplify a spell's numerical result by a multiplier."""

    def amplified_spell(*args: Any, **kwargs: Any) -> int | float:
        original_power: int | float = base_spell(*args, **kwargs)
        amplified_power: int | float = original_power * multiplier

        return amplified_power

    return amplified_spell

# ==============================================================================
#   CONDITIONAL CASTER
# ==============================================================================

def conditional_caster(
        condition: Callable[..., bool], spell: Callable[..., Any]
        ) -> Callable[..., Any]:
    """Cast a spell only if the condition returns True,
    else returns 'Spell fizzled'."""

    def conditional_spell(*args: Any, **kwargs: Any) -> Any:
        is_valid: bool = condition(*args, **kwargs)

        if is_valid:
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return conditional_spell

# ==============================================================================
#   SPELL SEQUENCE
# ==============================================================================

def spell_sequence(
        spells: list[Callable[..., Any]]
        ) -> Callable[..., list[Any]]:
    """Create a sequence of spells to be cast in order,
    returning a list of results."""

    def sequence_spell(*args: Any, **kwargs: Any) -> list[Any]:
        results: list[Any] = []

        for spell in spells:
            res: Any = spell(*args, **kwargs)
            results.append(res)

        return results

    return sequence_spell


# ==============================================================================
#   TEST FUNCTIONS
# ==============================================================================

def fireball(target: str, power: int) -> str:
    """Basic fireball spell."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Basic healing spell."""
    return f"Heal {target} for {power} HP"


def raw_damage(power: int) -> int:
    """Returns pure numerical damage."""
    return power


def is_boss(target: str, power: int) -> bool:
    """Condition check: returns True only if target is Dragon."""
    return target == "Dragon"


# ==============================================================================
#   MAIN
# ==============================================================================

def main() -> None:
    """Demonstrate the usage of Higher Realm spells."""

    test_values: list[int] = [11, 11, 10]
    test_targets: list[str] = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    # ============= SPELL COMBINER =============
    print("============= SPELL COMBINER =============")
    fire_and_heal: Callable[..., tuple[Any, Any]] = spell_combiner(
        fireball, heal
        )

    combo_result: tuple[Any, Any] = fire_and_heal("Dragon", test_values[0])

    print(f"Combined spell result: {combo_result[0]}, {combo_result[1]}")

    # ============= POWER AMPLIFIER =============
    print("\n============= POWER AMPLIFIER =============")

    mega_damage: Callable[..., int | float] = power_amplifier(raw_damage, 3)

    base_dmg: int = raw_damage(10)
    amped_dmg: int | float = mega_damage(10)

    print(f"Original: {base_dmg}, Amplified: {amped_dmg}")

    # ============= CONDITIONAL CASTER =============
    print("\n============= CONDITIONAL CASTER =============")

    boss_only_spell: Callable[..., Any] = conditional_caster(is_boss, fireball)

    for target in test_targets[:2]:  # On teste sur Dragon puis Goblin
        result: Any = boss_only_spell(target, test_values[1])

        print(f"Targeting {target}: {result}")

    # ============= SPELL SEQUENCE =============
    print("\n============= SPELL SEQUENCE =============")

    routine: list[Callable[..., Any]] = [fireball, heal, fireball]
    barrage_spell: Callable[..., list[Any]] = spell_sequence(routine)

    sequence_results: list[Any] = barrage_spell(
        test_targets[2], test_values[2]
        )

    print("Casting sequence on Wizard:")
    for res in sequence_results:
        print(f" -> {res}")


if __name__ == "__main__":
    main()
