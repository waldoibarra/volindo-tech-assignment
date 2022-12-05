from .ports import IAction, IDataset


class Part1Action(IAction):
    def __init__(self, dataset: IDataset):
        self.dataset = dataset

    def execute(self):
        self.dataset.print_column_information_type()
