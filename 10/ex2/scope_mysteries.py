from typing import Callable, Any

def mage_counter() -> Callable[[], int]:
    """Create a closure that counts how many times it's been called."""
    # La variable "sac à dos"
    count: int = 0
    
    def counter() -> int:
        nonlocal count
        count += 1
        return count
        
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Create a power accumulator closure starting from initial_power."""
    # La variable "sac à dos" initialisée avec le paramètre du parent
    total_power: int = initial_power
    
    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power
        
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Create an enchantment function using the provided enchantment_type."""
    # Ici, pas besoin de nonlocal car on ne fait que LIRE enchantment_type
    
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
        
    return apply_enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    """Create a memory management system with private storage closure."""
    # Le coffre-fort privé. C'est un dictionnaire stocké dans le sac à dos !
    vault: dict[str, Any] = {}
    
    # Première fonction enfant : pour écrire dans le coffre
    def store(key: str, value: Any) -> None:
        vault[key] = value
        
    # Deuxième fonction enfant : pour lire dans le coffre
    def recall(key: str) -> Any:
        # On utilise .get() pour retourner une valeur par défaut si la clé n'existe pas
        return vault.get(key, "Memory not found")
        
    # Le parent retourne les deux fonctions empaquetées dans un dictionnaire
    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    """Demonstrate the usage of Memory Depths closures."""
    
    # ============= MAGE COUNTER =============
    print("============= MAGE COUNTER =============")
    print("Testing mage counter...")
    my_counter: Callable[[], int] = mage_counter()
    
    print(f"Call 1: {my_counter()}")
    print(f"Call 2: {my_counter()}")
    print(f"Call 3: {my_counter()}")
    
    # Preuve que chaque closure a son PROPRE sac à dos indépendant
    another_counter: Callable[[], int] = mage_counter()
    print(f"New counter Call 1: {another_counter()}")


    # ============= SPELL ACCUMULATOR =============
    print("\n============= SPELL ACCUMULATOR =============")
    print("Testing spell accumulator (Starting at 100)...")
    accumulate: Callable[[int], int] = spell_accumulator(100)
    
    print(f"Adding 50: {accumulate(50)}")
    print(f"Adding 20: {accumulate(20)}")
    print(f"Adding 5: {accumulate(5)}")


    # ============= ENCHANTMENT FACTORY =============
    print("\n============= ENCHANTMENT FACTORY =============")
    print("Testing enchantment factory...")
    # On crée deux usines différentes
    fire_enchanter: Callable[[str], str] = enchantment_factory("Flaming")
    ice_enchanter: Callable[[str], str] = enchantment_factory("Frozen")
    
    print(fire_enchanter("Sword"))
    print(ice_enchanter("Shield"))
    print(fire_enchanter("Axe"))


    # ============= MEMORY VAULT =============
    print("\n============= MEMORY VAULT =============")
    print("Testing memory vault...")
    vault_interface: dict[str, Callable[..., Any]] = memory_vault()
    
    store_spell: Callable[..., Any] = vault_interface['store']
    recall_spell: Callable[..., Any] = vault_interface['recall']
    
    # On stocke des souvenirs
    store_spell("first_spell", "Fireball")
    store_spell("secret_code", 42)
    
    # On les récupère
    print(f"Recalling 'first_spell': {recall_spell('first_spell')}")
    print(f"Recalling 'secret_code': {recall_spell('secret_code')}")
    print(f"Recalling 'unknown': {recall_spell('unknown')}")

if __name__ == "__main__":
    main()