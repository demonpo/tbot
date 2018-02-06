"""
Simple testcase to test if the boardshell is working
----------------------------------------------------
"""
import tbot


@tbot.testcase
def test_boardshell(tb: tbot.TBot):
    """ Test if the boardshell is working """
    with tb.with_boardshell() as tbn:
        tbn.boardshell.exec0("sleep 2")
        assert tbn.boardshell.exec0("echo SOMESTRING") == "SOMESTRING\n"
        # tbn.boardshell.exec0("coninfo")
        # tbn.boardshell.exec0("version")
