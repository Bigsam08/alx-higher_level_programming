#!/usr/bin/python3
for digit in range(0, 100):
    if digit <= 99:
        print(f"{digit: 02}", end=",", "{\n}")
    else:
        print("\n")
