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
            valid_keys = ("temp", "humidity", "pressure")
            sensor_data = [
                d for d in data_batch
                if isinstance(d, str) and any(k in d for k in valid_keys)
            ]

            temps = [
                float(d.split(":")[1].strip())
                for d in sensor_data if "temp:" in d
            ]

            self.processed_count += len(sensor_data)
            self.temp_readings += len(temps)
            self.total_temp += sum(temps)

            avg: float = (
                self.total_temp / self.temp_readings
                if self.temp_readings > 0 else 0.0
            )

            return (f"Sensor analysis: {self.processed_count} readings"
                    f" processed, avg temp: {avg:.1f}°C")
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
            valid_keys = ("buy", "sell")
            trans_data = [
                d for d in data_batch
                if isinstance(d, str) and any(k in d for k in valid_keys)
            ]

            for item in trans_data:
                action, val_str = item.split(":")
                value = float(val_str.strip())
                if "buy" in action:
                    self.net_flow += value
                elif "sell" in action:
                    self.net_flow -= value

            self.processed_count += len(trans_data)
            sign = "+" if self.net_flow >= 0 else ""

            return (f"Transaction analysis: {self.processed_count} operations"
                    f", net flow: {sign}{self.net_flow:.0f} units")
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

            return (f"Event analysis: {self.processed_count} events, "
                    f"{self.error_count} error(s) detected")
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
            result = stream.process_batch(batch)
            print(f"{result}")


def main() -> None:
    """Demonstrates polymorphic streams in the Code Nexus."""
    print("CODE NEXUS POLYMORPHIC STREAM SYSTEM\n")

    # #########################  Sensor Stream  #########################
    print("Initializing Sensor Stream...")
    sensor: DataStream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch: List[str] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))

    # #######################  Transaction Stream  #######################
    print("\nInitializing Transaction Stream...")
    trans: DataStream = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    transac_batch: List[str] = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transac_batch}")
    print(trans.process_batch(transac_batch))

    # ##########################  Event Stream  ##########################
    print("\nInitializing Event Stream...")
    event: DataStream = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch: List[str] = ["login", "error", "logout"]
    event_batch_str: str = ", ".join(event_batch)
    print(f"Processing event batch: {event_batch_str}")
    print(event.process_batch(event_batch))

    # #################  StreamProcessor (Polymorphism)  #################
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    mixed_batch: List[str] = [
        "temp: 18.0", "buy: 500", "login",
        "error", "sell: 800", "humidity: 40",
        "error", "temp: 20.0"
    ]

    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(trans)
    manager.add_stream(event)

    print("Batch 1 Results:")
    manager.process_all(mixed_batch)

    print("\nStream filtering active: High-priority data only")
    alerts = event.filter_data(mixed_batch, criteria="error")
    high_trans = [t for t in mixed_batch if "sell: 800" in str(t)]
    print(f"Filtered results: {len(alerts)} critical alerts, "
          f"{len(high_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
