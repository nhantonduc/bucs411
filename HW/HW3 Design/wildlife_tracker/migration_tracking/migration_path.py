from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self,
                path_id: int,
                start_location: Habitat,
                species: str,
                destination: Habitat,
                duration: Optional[int] = None) -> None:
        self.path_id = path_id
        self.duration = duration
        self.start_location = start_location
        self.species = species
        self.destination = destination

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass
    
    def remove_migration_path(path_id: int) -> None:
        pass

    def get_migration_path_details(path_id) -> dict:
        pass
    
    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass
