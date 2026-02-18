class Plant:
    """Create a blueprint for plants."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with a name, a height and an age."""
        self.name = name
        self.height = height
        self.age = age
        self.final_growth = 0

    def grow(self, size: int) -> None:
        """Give a plant ability to grow."""
        self.height += size
        self.final_growth += size

    def get_type(self) -> str:
        """Define the plant type"""
        return "regular"

    def display_info(self) -> None:
        """Display plant data."""
        print(f"- {self.name}: "
              f"{self.height}cm,")


class FloweringPlant(Plant):
    """Create a specialized plant with floral characteristics."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flowering plant with an additionnal color attribute."""
        super().__init__(name, height, age)
        self.color = color

    def get_type(self) -> str:
        """Define the plant type"""
        return "flowering"

    def display_info(self) -> None:
        """Display flowering plant data."""
        print(f"- {self.name}: "
              f"{self.height}cm, "
              f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    """Create a type of flowering plant eligible for competition prizes."""

    def __init__(self, name: str, height: int,
                 age: int, color: str, prize: int) -> None:
        """Initialize prize-winning flower with its competition score."""
        super().__init__(name, height, age, color)
        self.prize = prize

    def win_prize(self) -> None:
        """Display the competition prize points earned by the flower."""
        print(f"Prize points: {self.prize}")

    def get_type(self) -> str:
        """Define the plant type"""
        return "prize"

    def display_info(self) -> None:
        """Display prize flowering plant data."""
        print(f"- {self.name}: "
              f"{self.height}cm, "
              f"{self.color} flowers (blooming), "
              f"Prize points: {self.prize}")


class GardenManager:
    """Create a garden manager, which creates gardens and statistics."""

    def __init__(self, garden_name: str) -> None:
        """Initialize garden manager and its internal analytics helper."""
        self.garden_name = garden_name
        self.plants = []
        self.stats_helper = self.GardenStats()

    def add_plant(self, plant: Plant) -> None:
        """Add a plant in the manager's garden."""
        self.plants = self.plants + [plant]
        print(f"Added {plant.name} to {self.garden_name}'s garden")

    def help_all_grow(self, size: int) -> None:
        """Make everyone grow and announce it."""
        print(f"{self.garden_name} is helping all plants grow...")
        for p in self.plants:
            p.grow(size)
            print(f"{p.name} grew {size}cm")

    class GardenStats:
        """Nested class helper to calculate analytics."""

        def display_report(self, garden_name: str, plants: list):
            """Display analytics report."""

            print(f"=== {garden_name}'s Garden Report ===")
            print("Plants in garden:")
            for p in plants:
                p.display_info()
            print()

            total_plants = 0
            total_growth = 0
            counts = {"regular": 0, "flowering": 0, "prize": 0}

            for p in plants:
                total_plants += 1
                ptype = p.get_type()
                if ptype in counts:
                    counts[ptype] += 1
                total_growth += p.final_growth

            print(f"Plants added: {total_plants}, "
                  f"Total growth: {total_growth}cm")
            print(f"Plant types: {counts['regular']} regular, "
                  f"{counts['flowering']} flowering, "
                  f"{counts['prize']} prize flowers")

    def show_analytics(self) -> None:
        """Delegate the report display to the GardenStats helper."""
        self.stats_helper.display_report(self.garden_name, self.plants)

    @staticmethod
    def factory_data(data: tuple) -> Plant:
        """Create a Plant instance from a tuple of data.

        The tuple must contain the class as the first element,
        followed by the arguments required for instantiation.

        """
        plant_class = data[0]
        args = data[1:]
        return plant_class(*args)

    @staticmethod
    def height_validation_test(height: int) -> bool:
        """Validate plant's height."""
        return height > 0

    @staticmethod
    def calculate_scores(plants: list):
        """Calculate a garden score, by summing height, age and prize."""
        score = 0
        for p in plants:
            score += p.height + p.age
            if p.get_type() == "prize":
                score += p.prize
        return score

    @classmethod
    def create_garden_network(cls, names: list) -> list:
        """Initialize a list of managers and display the gardens number"""
        gardens_number = 0
        for name in names:
            gardens_number += 1
        return [cls(name) for name in names]

    @classmethod
    def run_full_demo(cls, garden_name: str) -> None:
        """Orchestrate the entire scenario."""

        gardens = cls.create_garden_network([garden_name, "Bob"])
        alice_garden = gardens[0]
        bob_garden = gardens[1]

        bob_garden.plants = [cls.factory_data(
            (FloweringPlant, "Peony", 60, 32, "pink")
            )]
        print("=== Garden Management System Demo ===")
        print()
        alice_garden.add_plant(cls.factory_data(
            (Plant, "Oak Tree", 100, 10)
            ))
        alice_garden.add_plant(cls.factory_data(
            (FloweringPlant, "Rose", 25, 10, "red")
            ))
        alice_garden.add_plant(cls.factory_data(
            (PrizeFlower, "Sunflower", 50, 10, "yellow", 10)
            ))
        print()

        alice_garden.help_all_grow(1)
        print()
        alice_garden.show_analytics()
        print()
        is_valid = cls.height_validation_test(alice_garden.plants[0].height)
        print(f"Height validation test: {is_valid}")
        score_alice = cls.calculate_scores(alice_garden.plants)
        score_bob = cls.calculate_scores(bob_garden.plants)
        print(f"Garden scores - Alice: {score_alice}, Bob: {score_bob}")
        gardens_count = 0
        for g in gardens:
            gardens_count += 1
        print(f"Total gardens managed: {gardens_count}")


if __name__ == "__main__":
    GardenManager.run_full_demo("Alice")
