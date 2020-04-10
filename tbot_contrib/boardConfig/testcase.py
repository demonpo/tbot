import tbot
import typing
from tbot.machine import Machine, linux, board
import contextlib


class Register:
    def __init__(self, name: str, address: int, width: int):
        self.name = name
        self.address = address
        assert width in [8, 16, 32, 64], f"Unsupported register width: {width!r}"
        self.width = width
       
    def getValue(self, host: Machine) -> None:
        if isinstance(host, board.UBootShell):
            pass
        elif isinstance(host, linux.LinuxShell):
            pass
        else:
            raise Exception(
                f"You are not in allowed context (linux machine or uboot machine)"
            )

def testcase_prueba() -> None:
    with tbot.acquire_lab() as lb:
        lb.exec0("whoami")
        with tbot.acquire_board(lb) as b:
            register1= Register("prueba",1231,16)
            with tbot.acquire_linux(b) as lx:
                register1.getValue(lx)
