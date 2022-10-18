from typing import Dict

from hw21_DV.entities.abstract import Storage
from hw21_DV.exceptions import NotEnoughSpaceError, NoSuchItemError, LessAmountError


class BaseStorage(Storage):

    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, title: str, quantity: int) -> None:
        """увеличивает запас items"""
        if self.get_free_space() < quantity:
            raise NotEnoughSpaceError("На складе недостаточно места")
        if title in self.__items:
            self.__items[title] += quantity
        else:
            self.__items[title] = quantity

    def remove(self, title: str, quantity: int) -> None:
        """уменьшает запас items"""
        if title not in self.__items:
            raise NoSuchItemError("На складе нет такого товара")
        if self.__items[title] < quantity:
            raise LessAmountError(f"Не хватает на складе, попробуйте заказать меньше")
        else:
            self.__items[title] -= quantity
        if self.__items[title] == 0:
            self.__items.pop(title)

    def get_free_space(self) -> int:
        """Возвращает количество свободных мест"""
        return self.__capacity - sum(self.__items.values())

    def get_items(self) -> Dict[str, int]:
        """Возвращает содержание склада в
        словаре {товар: количество}"""
        return self.__items

    def get_unique_items_count(self) -> int:
        """Возвращает количество уникальных товаров"""
        return len(self.__items)
