import pandas as pd
import os

from ..application.ports import IDataset

class Adult50kDataset(IDataset):
    data_path = "src/data/"

    def __init__(self, input_dataset_filename: str):
        self.load_dataset(input_dataset_filename)

    def load_dataset(self, input_dataset_filename: str) -> None:
        dataset_path = self.data_path + input_dataset_filename
        self.dataset = pd.read_csv(dataset_path)

    def print_column_information_type(self) -> None:
        print(self.dataset.head(3))
