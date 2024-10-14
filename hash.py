def my_hash(s: str) -> int:
    """Hash the string and return the index of the bucket."""
    p = 499
    m = 2 ** 61 - 1
    hash_value = 0
    p_power = 1
    for char in s:
        hash_value = (hash_value + ord(char) * p_power) % m
        p_power = (p_power * p) % m
    return hash_value
