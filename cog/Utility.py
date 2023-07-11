def extract_value_from_map(input: str, location_map: map) -> str | None:
    if input in location_map:
        return location_map[input]
    else:
        print('エラー extract_value_from_map')
        return None


def extract_value_from_map(input: str, location_map: map) -> int | None:
    if input in location_map:
        return location_map[input]
    else:
        print('エラー extract_value_from_map')
    return None
