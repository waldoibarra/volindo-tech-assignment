from abc import ABC, abstractmethod

class IDataset(ABC):
    @abstractmethod
    def load_dataset(self, input_dataset_filename: str) -> None:
        pass

    @abstractmethod
    def print_columns_type_information(self) -> None:
        pass

    @abstractmethod
    def print_columns_balanceness(self) -> None:
        pass
