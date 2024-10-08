from typing import Optional, List, Any

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:
    
    #  environment_type: str,
    #   geographic_area: str,
    #   size: int,
    #   habitat_id: int,
    #   animals: Optional[List[int]] = None) -> None:
    def __init__(self) -> None:
        habitats: dict[int, Habitat] = {}
    
    
    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass
    
    def remove_habitat(habitat_id: int) -> None:
        pass
    
    def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
        pass
    
    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass

    def get_habitat_details(habitat_id: int) -> dict:
        pass

    def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
        pass

    def get_habitats_by_size(size: int) -> List[Habitat]:
        pass

    def get_habitats_by_type(environment_type: str) -> List[Habitat]:
        pass
    
    def get_animals_in_habitat(habitat_id: int) -> List[Animal]:
        pass
    
    def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
        pass
