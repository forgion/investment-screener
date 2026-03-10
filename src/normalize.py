import math

def normalize_values(values, higher_is_better=True):
    if not values:
        return []

    for value in values:
        validate_number(value)

    min_value = min(values)
    max_value = max(values)

    if min_value == max_value:
        return [50.0] * len(values)

    result = []
    for value in values:
        if higher_is_better:
            result.append((value - min_value) / (max_value - min_value)*100)
        else:
            result.append((max_value - value) / (max_value - min_value)*100)

    return result

def validate_number(value):
    if isinstance(value, bool):
        raise ValueError("Value is boolean, number expected")
    if not isinstance(value, (int, float)):
        raise TypeError("All values must be integers or floats")
    if math.isnan(value):
        raise ValueError("Value is NaN")