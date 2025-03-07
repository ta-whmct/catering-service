from abc import ABCMeta, abstractmethod


class BusinessRule(ABCMeta):
    @abstractmethod
    def is_broken(self) -> bool:
        raise NotImplementedError()
