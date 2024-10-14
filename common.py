from hash import my_hash


class HashSet:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def insert(self, s: str):
        bucket_index = my_hash(s) % self.size
        bucket = self.buckets[bucket_index]
        if s not in bucket:
            bucket.append(s)

    def remove(self, s: str):
        bucket_index = my_hash(s) % self.size
        bucket = self.buckets[bucket_index]
        if s in bucket:
            bucket.remove(s)

    def contains(self, s: str) -> bool:
        bucket_index = my_hash(s) % self.size
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
