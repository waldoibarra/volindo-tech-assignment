import pandas as pd

from ..application.ports import IDataset


class Adult50kDataset(IDataset):
    data_path = "src/data/"
    categorical_type = "categorical"
    continuous_type = "continuous"

    def __init__(self, input_dataset_filename: str):
        self.load_dataset(input_dataset_filename)

    def load_dataset(self, input_dataset_filename: str) -> None:
        dataset_path = self.data_path + input_dataset_filename
        self.df = pd.read_csv(dataset_path)

    def print_columns_type_information(self) -> None:
        for column in self.df.columns:
            self.print_information(column)

    def print_information(self, column):
        column_type = self.get_column_type(column)
        unique_values = len(self.df[column].unique())
        values_range = self.get_column_range(column, column_type)
        message = "{} - {} - {} values - {}"

        print(message.format(column, column_type, unique_values, values_range))

    def get_column_type(self, column):
        if self.df[column].dtype == "object":
            return self.categorical_type

        unique_values = len(self.df[column].unique())
        total_values = self.df[column].count()

        if (unique_values <= 10 or unique_values == total_values):
            return self.categorical_type

        return self.continuous_type

    def get_column_range(self, column, column_type):
        if column_type == self.categorical_type:
            return ", ".join(self.df[column].unique())

        min = self.df[column].min()
        max = self.df[column].max()

        return "{} to {}".format(min, max)
