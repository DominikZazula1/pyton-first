class OrderLimitError(Exception):
    def __init__(self, allowed_limit, message=None, *args):
        self.allowed_limit = allowed_limit
        if message is None:
            message = f"Przekroczono limit miejsc, który wynosi: {allowed_limit}"
        super().__init__(message, *args)
