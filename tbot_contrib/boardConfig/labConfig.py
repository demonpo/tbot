
from tbot.machine import connector, linux, board

class MyLabHost(
    connector.SubprocessConnector,
    linux.Bash,
    linux.Lab,
):
    name = "my-lab"

    @property
    def workdir(self):
        return linux.Workdir.static(self, f"/work/{self.username}/tbot-workdir")

# Tell tbot about the class by defining a global `LAB`
LAB = MyLabHost