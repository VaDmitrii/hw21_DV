from typing import Dict, List

from hw21_DV.entities.abstract import Storage
from hw21_DV.exceptions import BadRequestError, StorageError


class Request:

    departure: str = ''
    destination: str = ''
    amount: int = 0
    product: str = ''

    def __init__(self, request: str, storages: Dict[str, Storage]):
        self.storages = storages
        self.request = request

        request: List[str] = self.request.strip().lower().split(' ')
        if len(request) != 7:
            raise BadRequestError("Неправильный запрос")
        self.amount = int(request[1])
        self.product = request[2]
        self.departure = request[4]
        self.destination = request[6]

        if self.departure not in storages.keys() or self.destination not in storages.keys():
            raise StorageError("Такого склада нет")
