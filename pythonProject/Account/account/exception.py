class AccountException(Exception):
    def __init__(self, message):
        super().__init__(message)


class AccountWithdrawalException(AccountException):
    def __init__(self, message):
        super().__init__(message)


class InsufficientAmount(AccountException):
    def __init__(self, message):
        super().__init__(message)
