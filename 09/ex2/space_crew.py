from enum import Enum
from datetime import datetime
from typing import List
from pydantic import (  # type: ignore
    BaseModel,
    Field,
    ValidationError,
    model_validator
)


class RankEnum(str, Enum):
    """Enumeration of all valid ranks for a space crew member."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Defines a single crew member with their attributes and validations."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: RankEnum
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Defines a space mission, containing a crew and specific parameters."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> 'SpaceMission':
        """Validates complex cross-field business rules for a space mission."""

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(member.rank in [RankEnum.COMMANDER, RankEnum.CAPTAIN]
                   for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            exp_count = sum(1 for member in self.crew
                            if member.years_experience >= 5)
            if exp_count < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days)"
                                 " need 50% experienced crew (5+ years)")

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    """Main function to demonstrate SpaceMission nested validations."""
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        print("Valid mission created:")
        commander = CrewMember(
            member_id="CM001", name="Sarah Connor", rank=RankEnum.COMMANDER,
            age=45, specialization="Mission Command", years_experience=15
        )
        lieutenant = CrewMember(
            member_id="CM002", name="John Smith", rank=RankEnum.LIEUTENANT,
            age=32, specialization="Navigation", years_experience=8
        )
        officer = CrewMember(
            member_id="CM003", name="Alice Johnson", rank=RankEnum.OFFICER,
            age=28, specialization="Engineering", years_experience=4
        )

        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-06-01T08:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[commander, lieutenant, officer]
        )

        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")
        print()

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    try:
        print("\n=========================================")
        print("Expected validation error:")
        invalid_mission = SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Lunar Outpost",
            destination="Moon",
            launch_date="2024-05-01T08:00:00",
            duration_days=30,
            budget_millions=500.0,
            crew=[lieutenant, officer]
        )
        print(invalid_mission)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
