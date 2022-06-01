from typing import List


class Pokemon:
    def __init__(self):
        self._name: str = ''
        self._number: int = 0
        self._types: List[str] = []
        self._weaknesses: List[str] = []
        self._stats: List[int] = []
        self._stats_name: List[str] = []

    def __repr__(self):
        s = f'{self._name}\n'
        s += f'number: {self._number}\n'
        s += f'types: {self._types}\n'
        s += f'weaknesses: {self._weaknesses}\n'
        s += f'stats: {self._stats}\n'
        s += f'stats_name: {self._stats_name}\n'

        return s

    def set_name(self, n):
        self._name = n

    def set_number(self, n):
        self._number = int(n)

    def set_types(self, t):
        self._types = t

    def set_weaknesses(self, w):
        self._weaknesses = w

    def set_stats(self, s):
        self._stats = s

    def set_stats_name(self, s):
        self._stats_name = s

    def get_csv_line(self) -> str:
        return f'{self._name},{self._number},{self._types},{self._weaknesses},{self._stats},{self._stats_name}\n'
