class Register:
    def __init__(self, name: str, address: int, width: int):

        self.name = name
        self.address = address
        self.width = width


class RegisterMap:
    def __init__(self) -> None:
        pass

    def get_register(self, name: str) -> Register:
        pass

    def get_all_registers(self) -> None:
        pass
