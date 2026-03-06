from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class representing a generic data stream."""

    def __init__(self, stream_id: str) -> None:
        """Initializes the stream with its ID and state."""
        self.stream_id: str = stream_id
        self.stream_type: str = "Generic Data"
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data specific to the stream type."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on criteria using list comprehension."""
        if not criteria:
            return data_batch

        # Filtre de base : garde les éléments contenant le critère textuel
        return [
            d for d in data_batch
            if isinstance(d, str) and criteria.lower() in d.lower()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return generic stream statistics."""
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    """Specialized stream for environmental sensor data."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        self.total_temp: float = 0.0
        self.temp_readings: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            # 1. On utilise une List Comprehension pour ne garder QUE
            # les données qui concernent les capteurs (temp, humidity...)
            valid_keys = ("temp", "humidity", "pressure")
            sensor_data = [
                d for d in data_batch
                if isinstance(d, str) and any(k in d for k in valid_keys)
            ]

            # 2. Extraction spécifique des températures
            temps = [
                float(d.split(":")[1].strip())
                for d in sensor_data if "temp:" in d
            ]

            self.processed_count += len(sensor_data)
            self.temp_readings += len(temps)
            self.total_temp += sum(temps)

            avg = (
                self.total_temp / self.temp_readings
                if self.temp_readings > 0 else 0.0
            )

            return (f"Sensor analysis: {len(sensor_data)} readings processed,"
                    f" avg temp: {avg:.1f}°C")
        except Exception as e:
            return f"Error processing sensor batch: {e}"


class TransactionStream(DataStream):
    """Specialized stream for financial transactions."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"
        self.net_flow: float = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            # Extraction des transactions uniquement
            valid_keys = ("buy", "sell")
            trans_data = [
                d for d in data_batch
                if isinstance(d, str) and any(k in d for k in valid_keys)
            ]

            for item in trans_data:
                action, val_str = item.split(":")
                value = float(val_str.strip())
                if "buy" in action:
                    self.net_flow -= value
                elif "sell" in action:
                    self.net_flow += value

            self.processed_count += len(trans_data)
            sign = "+" if self.net_flow >= 0 else ""

            return (f"Transaction analysis: {len(trans_data)} operations, "
                    f"net flow: {sign}{self.net_flow:.0f} units")
        except Exception as e:
            return f"Error processing transaction batch: {e}"


class EventStream(DataStream):
    """Specialized stream for system events."""

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"
        self.error_count: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_keys = ("login", "logout", "error")
            event_data = [
                d for d in data_batch
                if isinstance(d, str) and any(k in d for k in valid_keys)
            ]

            errors = [e for e in event_data if "error" in e]
            self.error_count += len(errors)
            self.processed_count += len(event_data)

            return (f"Event analysis: {len(event_data)} events, "
                    f"{len(errors)} error(s) detected")
        except Exception as e:
            return f"Error processing event batch: {e}"


class StreamProcessor:
    """Manager class that orchestrates multiple streams polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Adds a stream to the manager's pool."""
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self, batch: List[Any]) -> None:
        """Processes a mixed batch through all managed streams."""
        for stream in self.streams:
            # Le polymorphisme en action : le manager appelle process_batch
            # sans savoir quel est le type réel du stream !
            result = stream.process_batch(batch)
            print(f"{stream.stream_type.split()[0]} data: {result}")


def main() -> None:
    """Demonstrates polymorphic streams in the Code Nexus."""
    print("CODE NEXUS POLYMORPHIC STREAM SYSTEM\n")

    # Initialisation individuelle
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(sensor.process_batch(
        ["temp: 22.5", "humidity: 65", "pressure: 1013"])
        )

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    print(trans.process_batch(["buy: 100", "sell: 150", "buy: 75"]))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print(event.process_batch(["login", "error", "logout"]))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    # Un lot de données complètement chaotique
    mixed_batch = [
        "temp: 18.0", "buy: 500", "login",
        "error", "sell: 800", "humidity: 40",
        "error", "temp: 20.0"
    ]

    # Le Chef d'Orchestre (StreamProcessor)
    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(trans)
    manager.add_stream(event)

    print("Batch 1 Results:")
    manager.process_all(mixed_batch)

    print("\nStream filtering active: High-priority data only")
    # Utilisation de la méthode héritée filter_data
    alerts = event.filter_data(mixed_batch, criteria="error")
    high_trans = [t for t in mixed_batch if "sell: 800" in str(t)]
    print(f"Filtered results: {len(alerts)} critical alerts, "
          f"{len(high_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
