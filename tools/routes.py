from enum import Enum


class APIRoutes(str, Enum):
    USER = "/user"
    STORE = "/store"
    PET = "/pet"

    def __str__(self):
        return self.value
