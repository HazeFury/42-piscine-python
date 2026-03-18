from typing import Any


# ==============================================================================
#   ARTIFACT SORTER
# ==============================================================================

def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sort magical artifacts by power level in descending order."""
    try:
        return sorted(artifacts, key=lambda x: x.get('power', 0), reverse=True)
    except Exception as e:
        print(f"Error sorting artifacts: {e}")
        return []


# ==============================================================================
#   POWER FILTER
# ==============================================================================

def power_filter(
        mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    """Filter mages returning only those with power >= min_power."""
    try:
        return list(filter(lambda x: x.get('power', 0) >= min_power, mages))
    except Exception as e:
        print(f"Error filtering mages: {e}")
        return []


# ==============================================================================
#   SPELL TRANFORMER
# ==============================================================================

def spell_transformer(spells: list[str]) -> list[str]:
    """Transform a list of spell names by adding '*' prefix and suffix."""
    try:
        return list(map(lambda x: f"* {x} *", spells))
    except Exception as e:
        print(f"Error transforming spells: {e}")
        return []


# ==============================================================================
#   MAGE STATS
# ==============================================================================

def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    """Calculate max, min, and average power levels of a list of mages."""
    try:
        if not mages:
            return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

        max_p: int = max(mages, key=lambda x: x.get('power', 0))['power']
        min_p: int = min(mages, key=lambda x: x.get('power', 0))['power']

        total_power: int = sum(map(lambda x: x.get('power', 0), mages))
        avg_p: float = round(total_power / len(mages), 2)

        return {
            'max_power': max_p,
            'min_power': min_p,
            'avg_power': avg_p
        }
    except Exception as e:
        print(f"Error calculating stats: {e}")
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}


# ==============================================================================
#   MAIN
# ==============================================================================

def main() -> None:
    """Demonstrate the usage of Lambda Sanctum spells."""

    artifacts = [
        {'name': 'Ice Wand', 'power': 81, 'type': 'weapon'},
        {'name': 'Lightning Rod', 'power': 66, 'type': 'armor'},
        {'name': 'Crystal Orb', 'power': 65, 'type': 'relic'},
        {'name': 'Fire Staff', 'power': 76, 'type': 'accessory'}
        ]

    mages = [
        {'name': 'Phoenix', 'power': 92, 'element': 'shadow'},
        {'name': 'Storm', 'power': 90, 'element': 'ice'},
        {'name': 'Nova', 'power': 68, 'element': 'light'},
        {'name': 'Nova', 'power': 84, 'element': 'lightning'},
        {'name': 'Phoenix', 'power': 98, 'element': 'ice'}
        ]

    spells = ['blizzard', 'heal', 'freeze', 'earthquake']

    # =============  ARTIFACT  =============
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print("before :")
    for art in artifacts:
        print(art)
    print("after :")
    for art in sorted_artifacts:
        print(art)

    # =============  POWER  =============
    print("\n\nTesting power filter (more than 90)...")
    filtered = power_filter(mages, 90)
    print("before :")
    for mage in mages:
        print(mage)
    print("after :")
    for element in filtered:
        print(element)

    # =============  SPELL  =============
    print("\n\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    for el in transformed:
        print(el, end=" ")
    print()

    # =============  STATISTICS  =============
    print("\n\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    main()
