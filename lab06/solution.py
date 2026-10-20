def count_items(values: list) -> dict:
    result = {}
    for value in values:
        result[value] = result.get(value, 0) + 1
    return result

def unique_sorted(values: list) -> list:
    if not values:
        return []
    return sorted(set(values))

