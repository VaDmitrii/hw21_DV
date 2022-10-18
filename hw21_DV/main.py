from typing import Dict

from entities.abstract import Storage
from entities.courier import Courier
from entities.request import Request
from entities.shop import Shop
from entities.store import Store
from exceptions import MyExceptions, CancelExceptions

store = Store(
    items={
        "картошка": 10,
        "печеньки": 10,

    },
    capacity=100,
)
shop = Shop(items={"печеньки": 5, }, capacity=20, store_limit=5, )

storages: Dict[str, Storage] = {
    "склад": store,
    "магазин": shop,
}


def main():
    print("Привет!\n")

    while True:
        for storage_name, storage in storages.items():
            print(f"В {storage_name} хранится:\n{storage.get_items()}")

        user_request: str = input("Введите запрос в формате 'Доставить 3 печеньки из склад в магазин'"
                                  "Введите 'stop' или 'стоп', чтобы закончить ввод\n")

        if user_request in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_request, storages=storages)
        except MyExceptions as error:
            print(error)
            continue

        courier = Courier(request=request, storages=storages)
        try:
            courier.move()
        except CancelExceptions as error:
            print(error)
            courier.cancel()
            continue
        except MyExceptions as error:
            print(error)
            continue


if __name__ == '__main__':
    main()
