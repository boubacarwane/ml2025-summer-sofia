# module5_mod.py
class NumberStore:
    def __init__(self):
        self._data = []

    def add_number(self, value: int) -> None:
        self._data.append(value)

    def find_first_index(self, target: int) -> int:
        for i, v in enumerate(self._data, start=1):
            if v == target:
                return i
        return -1
