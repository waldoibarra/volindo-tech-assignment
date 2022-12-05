import pandas as pd

from ..application.ports import IDataset


class Adult50kDataset(IDataset):
    data_path = "src/data/"
    categorical_type = "categorical"
    continuous_type = "continuous"
    balanced_state = "balanced"
    imbalanced_state = "imbalanced"
    categorical_min_values = 10
    one_hundred_percent = 100
    min_occurrence_percent = 10

    def __init__(self, input_dataset_filename: str):
        self.load_dataset(input_dataset_filename)

    def load_dataset(self, input_dataset_filename: str) -> None:
        dataset_path = self.data_path + input_dataset_filename
        self.df = pd.read_csv(dataset_path)

    def print_columns_type_information(self) -> None:
        for column in self.df.columns:
            self.__print_information(column)

    def print_columns_balanceness(self) -> None:
        for column in self.df.columns:
            self.__print_balanceness(column)

    def __print_information(self, column: str) -> None:
        column_type = self.__get_column_type(column)
        unique_values = len(self.df[column].unique())
        values_range = self.__get_column_range(column, column_type)
        message = "{} - {} - {} values - {}"

        print(message.format(column, column_type, unique_values, values_range))

    def __print_balanceness(self, column: str):
        column_type = self.__get_column_type(column)
        balanceness = self.__get_column_balance_state(column, column_type)
        message = "{} - {} - {}"

        if (column_type == self.categorical_type):
            message += self.__get_categorical_message_portion(column)

        print(message.format(column, column_type, balanceness))

    def __get_column_type(self, column: str) -> str:
        if self.df[column].dtype == "object":
            return self.categorical_type

        unique_values = len(self.df[column].unique())
        total_values = self.df[column].count()

        if (unique_values <= self.categorical_min_values or unique_values == total_values):
            return self.categorical_type

        return self.continuous_type

    def __get_column_range(self, column: str, column_type: str) -> str:
        if column_type == self.categorical_type:
            return ", ".join(self.df[column].unique())

        min = self.df[column].min()
        max = self.df[column].max()

        return "{} to {}".format(min, max)

    def __get_column_balance_state(self, column: str, column_type: str) -> str:
        if column_type == self.continuous_type:
            return self.balanced_state

        min_occurrence = self.__get_min_occurrence(column)
        relative_frequencies = self.df[column].value_counts(normalize=True)

        for relative_frequency in list(relative_frequencies):
            occurrence = relative_frequency * self.one_hundred_percent
            if (occurrence < min_occurrence):
                return self.imbalanced_state

        return self.balanced_state

    def __get_min_occurrence(self, column: str) -> float:
        unique_values = len(self.df[column].unique())
        min_occurrence = self.one_hundred_percent / \
            unique_values / self.min_occurrence_percent

        return min_occurrence

    def __get_categorical_message_portion(self, column: str) -> str:
        min_occurrence = self.__get_min_occurrence(column)
        classes_ocurrence = self.__get_column_classes_and_occurrence(column)
        message = " - {:g}% min occurrence - {}"

        return message.format(min_occurrence, classes_ocurrence)

    def __get_column_classes_and_occurrence(self, column: str) -> str:
        relative_frequencies = self.df[column].value_counts(normalize=True)
        occurrences = []

        for category, relative_frequency in relative_frequencies.items():
            occurrence = relative_frequency * self.one_hundred_percent
            occurrences.append("{} {:g}%".format(category, occurrence))

        return ", ".join(occurrences)
