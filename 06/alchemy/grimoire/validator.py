def validate_ingredients(ingredients: str) -> str:
    """Validate if ingredients contains at least one base elements"""
    valid_elements = ["fire", "water", "earth", "air"]

    for element in valid_elements:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
