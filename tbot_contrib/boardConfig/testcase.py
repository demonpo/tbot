import tbot
import typing
from tbot.machine import Machine, linux, board



class Register:
    def __init__(self, host: Machine, name: str, address: int, width: int):
        self._host =host
        self.name = name
        self.address = address
        assert width in [8, 16, 32, 64], f"Unsupported register width: {width!r}"
        self.width = width
        if isinstance(host, board.UBootShell):
            self._machine = "uboot"
        elif isinstance(host, linux.LinuxShell):
            self._machine = "linux"
        else:
            raise Exception(
                f"You are not in allowed context (linux machine or uboot machine)"
            )

    def getValue(self) -> None:
        if self._machine == "uboot":
            pass
        elif self._machine == "linux":
            pass



@tbot.testcase
def testcase_prueba() -> None:
    with tbot.acquire_lab() as lb:
        lb.exec0("whoami")
        with tbot.acquire_board(lb) as b:
            with tbot.acquire_linux(b) as lx:
                register1= Register(lx,"prueba",1231,16)
