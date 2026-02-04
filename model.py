from dataclasses import dataclass
# This file contains all the datastructure needed.
@dataclass
class Task:
    id: int
    description: str
    status: str
    created_at: str
    updated_at: str


