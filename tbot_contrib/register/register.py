import typing


class Register:
    def __init__(self, name: str, address: int, width: int):
        self.name = name
        self.address = address
        self.width = width


class RegisterMap:
    def __init__(self, registers_list: typing.List[Register] = []) -> None:
        self.registers_dict = {}
        if len(registers_list) > 0:
            for register in registers_list:
                self.registers_dict[register.name] = register

    def add_register(self, register: Register) -> None:
        self.registers_dict[register.name] = register

    def remove_register(self, name: str) -> Register:
        return self.registers_dict.pop(name)

    def get_register(self, name: str) -> Register:
        if name in self.registers_dict:
            return self.registers_dict[name]

        return self.registers_dict[name]

    def get_all_registers(self) -> typing.List[Register]:
        return list(self.registers_dict.values())
