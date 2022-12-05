from abc import ABC, abstractmethod

class IDataset(ABC):
    @abstractmethod
    def print_column_information_type() -> None:
        pass
