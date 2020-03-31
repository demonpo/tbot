from tbot.machine import board, linux, connector


class MyBoard(
    connector.ConsoleConnector,
    board.PowerControl,
    board.Board,
):
    name = "myboard"

    def poweron(self):
        self.host.exec0("perl", "/opt/fhem/fhem.pl", "192.168.178.53:7072", "set ESCAPECOM on")

    def poweroff(self):
        self.host.exec0("perl", "/opt/fhem/fhem.pl", "192.168.178.53:7072", "set ESCAPECOM off")

    def connect(self, mach):
        # Open the serial console
        return mach.open_channel("picocom", "-b", "115200", "/dev/ttyUSB0")


# Similarl to the `LAB`, the board needs to be made available as `BOARD`


class MyUBoot(
    board.Connector,
    board.UBootAutobootIntercept,
    board.UBootShell,
):
    prompt ="Colibri iMX6 # "

class LinuxFromUBoot(
    board.LinuxUbootConnector,
    board.LinuxBootLogin,
    linux.Bash,
):
    # Configuration for LinuxUbootConnector
    uboot = MyUBoot  # <- Our UBoot machine
    
    def do_boot(self, ub):  # <- Procedure to boot Linux
       return ub.boot("run", "dani")

    # LinuxBootLogin handles waiting for Linux to boot & logging in
    username = "root"
    password = None
BOARD = MyBoard
UBOOT = MyUBoot
LINUX = LinuxFromUBoot