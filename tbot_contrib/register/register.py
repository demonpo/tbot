import typing
from tbot.machine import Machine
from tbot.machine.board import UBootShell, LinuxBootLogin


class Register:
    def __init__(self, host: Machine, name: str, address: int, width: int):
        self.name = name
        self.address = address
        assert width in [8, 16, 32, 64], f"Unsupported register width: {width!r}"
        self.width = width
        if type(host) is UBootShell:
            self.machine = "uboot"
        elif type(host) is LinuxBootLogin:
            self.machine = "linux"
        else:
            raise Exception(
                f"You are not in allowed context (linux machine or uboot machine"
            )

    def getValue(self) -> None:
        if self.machine == "uboot":
            pass
        elif self.machine == "linux":
            pass


class RegisterMap:
    def __init__(self, registers_list: typing.List[Register] = []) -> None:
        self.registers_dict = {}
        if len(registers_list) > 0:
            for register in registers_list:
                self.registers_dict[register.name] = register

    def add_register(self, register: Register) -> None:
        if register.name in self.registers_dict:
            raise Exception(
                f"There is already a register with the name: {register.name}"
            )
        self.registers_dict[register.name] = register

    def remove_register(self, name: str) -> Register:
        if name in self.registers_dict:
            return self.registers_dict.pop(name)
        raise Exception(f"There is not a register with the name: {name}")

    def get_register(self, name: str) -> Register:
        if name in self.registers_dict:
            return self.registers_dict[name]
        raise Exception(f"There is not a register with the name: {name}")

    def get_all_registers(self) -> typing.List[Register]:
        return list(self.registers_dict.values())

    def get_all_registers_values(self):
        pass
