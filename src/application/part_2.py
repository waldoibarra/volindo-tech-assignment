from .ports import IAction, IDataset


class Part2Action(IAction):
    def __init__(self, dataset: IDataset):
        self.dataset = dataset

    def execute(self):
        print("Answer for part 2:\n")
        self.dataset.print_columns_balanceness()
