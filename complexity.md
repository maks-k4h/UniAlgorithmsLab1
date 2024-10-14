# Complexity analysis

- **S**: Number of buckets in the hash map.

- **Sm**: Size of a bucket.

- **N**: Number of inputs.

- **Nm**: Maximum size of an input.


## Common Task: HashSet Implementation

```python
class HashSet:
    def __init__(self, size=1000):  # () - O(S)
        self.size = size             # O(1)
        self.buckets = [[] for _ in range(size)]  # O(S)

    def _hash(self, s: str) -> int:  # () -  O(Nm)
        """Hash the string and return the index of the bucket."""
        p = 499                      # O(1)
        m = 2 ** 61 - 1              # O(1)
        hash_value = 0               # O(1)
        p_power = 1                  # O(1)
        for char in s:               # O(Nm) * O(1)
            hash_value = (hash_value + ord(char) * p_power) % m  # O(1)
            p_power = (p_power * p) % m  # O(1)
        return hash_value % self.size  # O(1)

    def insert(self, s: str):        # () - O(Sm * Nm)
        bucket_index = self._hash(s) % self.size  # O(Nm)
        bucket = self.buckets[bucket_index]  # O(1)
        if s not in bucket:               # O(Sm * Nm)
            bucket.append(s)               # O(1)

    def remove(self, s: str):         # () - O(Sm * Nm)
        bucket_index = self._hash(s) % self.size  # O(Nm)
        bucket = self.buckets[bucket_index]  # O(1)
        if s in bucket:                   # O(Sm * Nm)
            bucket.remove(s)               # O(Sm)

    def contains(self, s: str) -> bool:  # () - O(Sm * Nm)
        bucket_index = self._hash(s) % self.size  # O(Nm)
        bucket = self.buckets[bucket_index]  # O(1)
        return s in bucket                  # O(Sm * Nm)
```

### Time Complexity Summary for HashSet:
- **Initialization**: O(S)
- **Hashing**: O(Nm)
- **Insert**: O(Nm * Sm)
- **Remove**: O(Nm * Sm)
- **Contains**: O(Nm * Sm)

## Variant 1: CountHashSet Implementation

```python
class CountHashSet:
    def __init__(self, size=1000):  # () - O(S)
        self.size = size             # O(1)
        self.buckets = [[] for _ in range(size)]  # O(S)

    def insert(self, s: str):        # () - O(Sm * Nm)
        bucket_index = my_hash(s) % self.size  # O(Nm)
        bucket = self.buckets[bucket_index]  # O(1)
        for i, (x, c) in enumerate(bucket):  # O(Sm) * O(Nm)
            if x == s:                  # O(Nm)
                bucket[i] = (s, c + 1)  # O(1)
                return                  # O(1)
        bucket.append((s, 1))          # O(1)

    def get_counts(self):              # () - O(S * Sm)
        """Return a list of strings and their counts."""
        counts = []                   # O(1)
        for bucket in self.buckets:   # O(S) * O(Sm)
            for s, count in bucket:    # O(Sm)
                counts.append((s, count))  # O(1)
        return counts                 # O(1)
```

### Time Complexity Summary for CountHashSet:
- **Initialization**: O(S)
- **Insert**: O(Nm * Sm)
- **Get Counts**: O(S * Sm)