class HashSet:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, s: str) -> int:
        """Hash the string and return the index of the bucket."""
        p = 499
        m = 2 ** 61 - 1
        hash_value = 0
        p_power = 1
        for char in s:
            hash_value = (hash_value + ord(char) * p_power) % m
            p_power = (p_power * p) % m
        return hash_value % self.size

    def insert(self, s: str):
        bucket_index = self._hash(s)
        bucket = self.buckets[bucket_index]
        if s not in bucket:
            bucket.append(s)

    def remove(self, s: str):
        bucket_index = self._hash(s)
        bucket = self.buckets[bucket_index]
        if s in bucket:
            bucket.remove(s)

    def contains(self, s: str) -> bool:
        bucket_index = self._hash(s)
        bucket = self.buckets[bucket_index]
        return s in bucket


def main():
    hash_set = HashSet()
    while True:
        operation = input().strip()
        if operation == "#":
            break
        command, string = operation.split()
        if command == "+":
            hash_set.insert(string)
        elif command == "-":
            hash_set.remove(string)
        elif command == "?":
            print("yes" if hash_set.contains(string) else "no")


if __name__ == "__main__":
    main()
