import operator
import time
from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Any

# ==============================================================================
# 1. REDUCE : Le Compresseur
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
            # min() et max() natives acceptent 2 arguments, parfait pour reduce !
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
# 2. PARTIAL : L'Usine de pré-remplissage
# ==============================================================================

def base_enchantment(power: int, element: str, target: str) -> str:
    """Base generic spell to be specialized."""
    return f"Enchanting {target} with {element} magic at {power} power level"

def partial_enchanter() -> dict[str, Callable[[str], str]]:
    """Create a dictionary of pre-configured enchantment spells."""
    # On gèle les deux premiers arguments (power et element)
    # Les nouvelles fonctions n'attendront plus que le dernier argument (target)
    fire_spell: Callable[[str], str] = partial(base_enchantment, 50, "Fire")
    ice_spell: Callable[[str], str] = partial(base_enchantment, 30, "Ice")
    arcane_spell: Callable[[str], str] = partial(base_enchantment, 100, "Arcane")
    
    return {
        'fire_enchant': fire_spell,
        'ice_enchant': ice_spell,
        'arcane_enchant': arcane_spell
    }


# ==============================================================================
# 3. LRU_CACHE : La Mémoire Haute Vitesse
# ==============================================================================

# On limite le carnet à 100 calculs en mémoire
@lru_cache(maxsize=100)
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number, accelerated by memoization."""
    if n < 0:
        return 0
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ==============================================================================
# 4. SINGLEDISPATCH : Le Standardiste
# ==============================================================================

@singledispatch
def dispatch_spell(target: Any) -> str:
    """Default fallback spell if the target type is unknown."""
    return f"Casting generic spell on mysterious entity of type: {type(target).__name__}"

@dispatch_spell.register(str)
def _(target: str) -> str:
    """Specialized spell for String targets."""
    return f"Casting verbal spell on {target}"

@dispatch_spell.register(int)
def _(target: int) -> str:
    """Specialized spell for Integer targets."""
    return f"Casting physical spell with {target} raw damage"

@dispatch_spell.register(list)
def _(target: list[Any]) -> str:
    """Specialized spell for List targets."""
    return f"Casting Area of Effect (AoE) spell hitting {len(target)} targets"


# ==============================================================================
# FONCTION PRINCIPALE DE DEMONSTRATION
# ==============================================================================

def main() -> None:
    """Demonstrate the usage of Ancient Library artifacts."""
    
    # ============= REDUCE =============
    print("============= SPELL REDUCER =============")
    power_list: list[int] = [2, 4, 6, 8]
    print(f"Base powers: {power_list}")
    print(f"Sum (add): {spell_reducer(power_list, 'add')}")
    print(f"Product (multiply): {spell_reducer(power_list, 'multiply')}")
    print(f"Max power: {spell_reducer(power_list, 'max')}")


    # ============= PARTIAL =============
    print("\n============= PARTIAL ENCHANTER =============")
    grimoire: dict[str, Callable[[str], str]] = partial_enchanter()
    
    # On n'a plus qu'à fournir la cible !
    print(grimoire['fire_enchant']("Sword"))
    print(grimoire['ice_enchant']("Shield"))
    print(grimoire['arcane_enchant']("Staff"))


    # ============= LRU CACHE =============
    print("\n============= LRU CACHE =============")
    print("Testing Fibonacci sequence with cache...")
    
    # Premier appel (calcul réel qui descend tout l'arbre récursif)
    start_time: float = time.time()
    result1: int = fibonacci(35)
    end_time: float = time.time()
    print(f"First call (fibonacci 35): {result1}")
    print(f"Time taken (Computing): {end_time - start_time:.5f} seconds")
    
    # Deuxième appel (le standardiste lit juste le carnet)
    start_time2: float = time.time()
    result2: int = fibonacci(35)
    end_time2: float = time.time()
    print(f"\nSecond call (fibonacci 35): {result2}")
    print(f"Time taken (Cached): {end_time2 - start_time2:.5f} seconds")
    print("-> That's the power of memoization!")


    # ============= SINGLEDISPATCH =============
    print("\n============= SINGLEDISPATCH =============")
    print("Testing dispatch spell with different types...")
    
    print(dispatch_spell("The Dragon"))           # Appelle la version str
    print(dispatch_spell(42))                     # Appelle la version int
    print(dispatch_spell(["Goblin", "Orc"]))      # Appelle la version list
    print(dispatch_spell({"name": "Arthur"}))     # Type inconnu (dict), appelle le par défaut

if __name__ == "__main__":
    main()