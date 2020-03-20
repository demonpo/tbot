import tbot
from tbot.machine import linux


class Gpio:
    def __init__(self, host: linux.LinuxShell, gpio_number: int):

        self.host = host
        self._gpio_number = str(gpio_number)
        self._gpio_sysclass_path = self.host.fsroot / "sys/class/gpio"
        self._gpio_path = self._gpio_sysclass_path / f"gpio{self._gpio_number}"
        self._export()

    def _export(self) -> None:
        if not self._gpio_path.is_dir():
            self.host.exec0(
                "echo",
                str(self._gpio_number),
                linux.RedirStdout(self._gpio_sysclass_path / "export"),
            )

    def _is_in_direction(self) -> bool:
        direction = self.host.exec0("cat", self._gpio_path / "direction")
        return direction.strip().lower() == "in"

    def set_in_direction(self) -> None:
        if self._is_in_direction():
            pass
        else:
            self.host.exec0(
                "echo", "in", linux.RedirStdout(self._gpio_path / "direction")
            )

    def set_out_direction(self) -> None:
        if not self._is_in_direction():
            pass
        else:
            self.host.exec0(
                "echo", "out", linux.RedirStdout(self._gpio_path / "direction")
            )

    def get_direction(self) -> str:
        return self.host.exec0("cat", self._gpio_path / "direction").strip()

    def set_value(self, value: str) -> None:
        if self._is_in_direction():
            tbot.log.message("You can not set value from a GPIO that has out direction")
        else:
            self.host.exec0("echo", value, linux.Raw(">"), self._gpio_path / "value")

    def get_value(self) -> str:
        if self._is_in_direction():
            return self.host.exec0("cat", self._gpio_path / "value").strip()
        else:
            tbot.log.message("You can not get value from a GPIO that has in direction")
            return ""
