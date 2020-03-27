import tbot

@tbot.testcase
def testcase_prueba():
    with tbot.acquire_lab() as lb:
        lb.exec0("whoami")
        with tbot.acquire_board(lb) as b:
            with tbot.acquire_uboot(b) as ub:
                ub.exec0("pri", "dani")