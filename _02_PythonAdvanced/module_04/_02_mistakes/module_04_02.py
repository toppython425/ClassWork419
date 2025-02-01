def find_min_bad(pairs: dict) -> str:  # -- плохо --
    key, _ = min(pairs.items(), key=lambda item: item[1])
    return key


def find_min_good(pairs: dict[str, int]) -> str:  # -- хорошо --
    key, _ = min(pairs.items(), key=lambda item: item[1])
    return key
