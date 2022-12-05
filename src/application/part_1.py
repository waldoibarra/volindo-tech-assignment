from .ports import IAction, IDataset


class Part1Action(IAction):
    def __init__(self, dataset: IDataset):
        self.dataset = dataset

    def execute(self):
        print("Answer for part 1:\n")
        self.dataset.print_columns_type_information()
