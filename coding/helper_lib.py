from abc import ABC


class BusinessService(ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def calculate(self, *args, **kwargs):
        pass
