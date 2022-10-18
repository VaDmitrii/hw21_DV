from typing import Dict

from hw21_DV.entities.abstract import Storage
from hw21_DV.entities.request import Request


class Courier:

    def __init__(self, request: Request, storages: Dict[str, Storage]):
        self.__request = request

        self.departure: Storage = storages[self.__request.departure]
        self.destination: Storage = storages[self.__request.destination]

    def move(self):
        self.departure.remove(title=self.__request.product, quantity=self.__request.amount)
        print(f"Курьер забрал {self.__request.amount} {self.__request.product} из {self.__request.departure}")

        print(f"Курьер везет {self.__request.amount} {self.__request.product} со {self.__request.departure} в "
              f"{self.__request.destination}")

        self.destination.add(title=self.__request.product, quantity=self.__request.amount)
        print(f"Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}")

    def cancel(self):
        self.departure.add(title=self.__request.product, quantity=self.__request.amount)
        print("Доставка отменена")

