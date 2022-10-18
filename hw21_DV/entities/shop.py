from typing import Dict

from hw21_DV.entities.BaseClass import BaseStorage
from hw21_DV.exceptions import LimitExceedError


class Shop(BaseStorage):

    def __init__(self, items: Dict[str, int], capacity: int, store_limit: int):
        self.store_limit = store_limit
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int) -> None:
        if self.get_unique_items_count() >= self.store_limit:
            raise LimitExceedError("В магазин недостаточно места, попробуйте что то другое")
        super().add(title=title, quantity=quantity)
