import typing

dic: dict = {}

print()


def get_register(dic: dict, name: str) -> typing.Any:
    if name in dic:
        return dic[name]
    raise Exception(f"There is not a register with name: {name}")


def get_all_registers(dic: dict) -> typing.List[str]:
    return list(dic.values())


# get_register(dic,"aloha")
print(get_all_registers(dic))
