import os

from ..application.ports import IDataset

class Adult50kDataset(IDataset):
    def print_column_information_type(self) -> None:
        pass
