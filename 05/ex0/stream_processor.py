from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):
    """Abstract base class defining the common processing interface."""

    def __init__(self) -> None:
        """Initializes the base processor. Demonstrates parent state."""
        self.is_active: bool = True

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate if data is appropriate for this processor."""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string."""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Specialized processor for numeric arrays."""

    def __init__(self) -> None:
        # Obligatoire selon l'énoncé : utilisation de super()
        super().__init__()

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        # Vérifie que chaque élément de la liste est un int ou un float
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for NumericProcessor")

        total: Union[int, float] = sum(data)
        avg: float = total / len(data) if data else 0.0
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    """Specialized processor for text strings."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and not ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for TextProcessor")

        chars: int = len(data)
        words: int = len(data.split())
        return f"Processed text: {chars} characters, {words} words"


class LogProcessor(DataProcessor):
    """Specialized processor for system logs."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        # Un log est une string qui contient obligatoirement un deux-points
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid data for LogProcessor")

        parts: List[str] = data.split(":", 1)
        level: str = parts[0].strip()
        msg: str = parts[1].strip()

        prefix: str = "[ALERT]" if level == "ERROR" else f"[{level}]"
        return f"{prefix} {level} level detected: {msg}"


def main() -> None:
    """Demonstrates polymorphic processing in the Code Nexus."""
    print("CODE NEXUS DATA PROCESSOR FOUNDATION\n")

    # --- TESTS INDIVIDUELS ---
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    num_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    if num_proc.validate(num_data):
        print("Validation: Numeric data verified")
        try:
            res_num: str = num_proc.process(num_data)
            print(num_proc.format_output(res_num))
        except Exception as e:
            print(f"Error: {e}")

    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    if text_proc.validate(text_data):
        print("Validation: Text data verified")
        try:
            res_txt: str = text_proc.process(text_data)
            print(text_proc.format_output(res_txt))
        except Exception as e:
            print(f"Error: {e}")

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        try:
            res_log: str = log_proc.process(log_data)
            print(log_proc.format_output(res_log))
        except Exception as e:
            print(f"Error: {e}")

    # --- LA MAGIE DU POLYMORPHISME ---
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface....")

    # On stocke nos objets enfants dans une liste typée avec le Parent !
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    inputs: List[Any] = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO: System ready"
    ]

    # La boucle polymorphique parfaite
    for i, (proc, data) in enumerate(zip(processors, inputs), 1):
        try:
            if proc.validate(data):
                res: str = proc.process(data)
                print(f"Result {i}: {res}")
        except Exception as e:
            print(f"Error on stream {i}: {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
