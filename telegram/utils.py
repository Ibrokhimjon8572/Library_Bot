
def extract_number(s: str):
    res = None

    for i in s:
        if i.isdigit():
            if res is None:
                res = int(i)
            else:
                res *= 10
                res += int(i)
        else:
            if res is None:
                continue
            return res

    if res is None:
        raise ValueError()

    if 1<=res<=11:
        return res
    raise ValueError()