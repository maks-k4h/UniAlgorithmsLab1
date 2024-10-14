from hash import my_hash


class CountHashSet:
    def __init__(self, size=1000):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def insert(self, s: str):
        bucket_index = my_hash(s) % self.size
        bucket = self.buckets[bucket_index]
        for i, (x, c) in enumerate(bucket):
            if x == s:
                bucket[i] = (s, c + 1)
                return
        bucket.append((s, 1))

    def get_counts(self):
        """Return a dictionary of strings and their counts."""
        counts = []
        for bucket in self.buckets:
            for s, count in bucket:
                counts.append((s, count))
        return counts


def main():
    count_set = CountHashSet()

    inputs = [
        "kiwi",
        "apple",
        "banana",
        "apple",
        "grape",
        "banana",
        "orange",
        "apple",
        "grape",
        "grape"
    ]
    for i in inputs:
        count_set.insert(i)
    for s, c in count_set.get_counts():
        if c > 1:
            print(s, c)


if __name__ == "__main__":
    main()
