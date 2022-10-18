class MyExceptions(Exception):
    message = "Что-то пошло не так"


class CancelExceptions(Exception):
    pass


class NotEnoughSpaceError(CancelExceptions):
    pass


class NoSuchItemError(MyExceptions):
    pass


class LessAmountError(MyExceptions):
    pass


class LimitExceedError(CancelExceptions):
    pass


class BadRequestError(MyExceptions):
    pass


class StorageError(MyExceptions):
    pass
