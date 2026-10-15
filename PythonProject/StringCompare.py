def compare_strings(a: str, b: str, method: str = "lex"):
    """
    Compare two strings.

    Methods:
      - "eq":  returns True if exactly equal (bool)
      - "ci":  case-insensitive equality (bool)
      - "lex": lexicographic comparison, returns -1, 0, or 1
      - "lev": Levenshtein distance (int)
    """
    if method == "eq":
        return a == b
    if method == "ci":
        return a.lower() == b.lower()
    if method == "lex":
        return (a > b) - (a < b)
    if method == "lev":
        # efficient iterative Levenshtein (O(len(a)*len(b)) time, O(min(len)) space)
        if len(a) < len(b):
            a, b = b, a
        prev = list(range(len(b) + 1))
        for i, ca in enumerate(a, start=1):
            cur = [i]
            for j, cb in enumerate(b, start=1):
                ins = cur[j - 1] + 1
                delet = prev[j] + 1
                repl = prev[j - 1] + (ca != cb)
                cur.append(min(ins, delet, repl))
            prev = cur
        return prev[-1]
    raise ValueError("Unknown method: choose 'eq', 'ci', 'lex', or 'lev'")


def main():
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")

    if compare_strings(first, second, "eq"):
        print("The strings are exactly equal.")
    else:
        print("The strings are not exactly equal.")

    if compare_strings(first, second, "ci"):
        print("The strings are equal when letter case is ignored.")
    else:
        print("The strings are different when letter case is ignored.")

    order = compare_strings(first, second, "lex")
    if order == 0:
        print("The strings have the same lexicographic order.")
    elif order < 0:
        print(f'"{first}" comes before "{second}" lexicographically.')
    else:
        print(f'"{second}" comes before "{first}" lexicographically.')

    distance = compare_strings(first, second, "lev")
    print(f"Levenshtein distance: {distance}")


if __name__ == "__main__":
    main()
