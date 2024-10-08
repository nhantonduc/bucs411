from typing import Any

class Migration:
    
    def __init__(self,
                migration_id: int,
                start_date: str,
                current_date: str,
                current_location: str,
                status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.start_date = start_date
        self.current_date = current_date
        self.status = status
        self.current_location = current_location

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass