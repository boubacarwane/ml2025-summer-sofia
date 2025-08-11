"""module5_call.py
Main program that imports NumberStore from module5_mod and performs I/O.

Behavior:
1) Ask for N (positive integer).
2) Read N integers one by one and insert into NumberStore.
3) Ask for X (integer) and print either the 1-based index of X or -1 if absent.
"""

from module5_mod import NumberStore

def _read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def _read_positive_int(prompt: str) -> int:
    while True:
        n = _read_int(prompt)
        if n > 0:
            return n
        print("Please enter a POSITIVE integer (> 0).")


def main() -> None:
    store = NumberStore()

    n = _read_positive_int("Enter N (positive integer): ")

    for i in range(1, n + 1):
        value = _read_int(f"Enter number #{i}: ")
        store.insert(value)

    x = _read_int("Enter X (integer to search): ")
    result = store.search(x)
    print(result)  # Per spec: print 1-based index or -1


if __name__ == "__main__":
    main()
