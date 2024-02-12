def merge_sort_string(string):
    """Sort a string using merge sort algorithm."""
    if isinstance(string, str):
        string = list(string)
    if len(string) > 1:
        middle = len(string) // 2
        left_half = string[:middle]
        right_half = string[middle:]

        merge_sort_string(left_half)
        merge_sort_string(right_half)

        merge(string, left_half, right_half)
    return "".join(string)


def merge(string, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            string[k] = left_half[i]
            i += 1
        else:
            string[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        string[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        string[k] = right_half[j]
        j += 1
        k += 1


def is_anagram(first_string, second_string):
    """Verify if two strings are anagrams."""
    if not first_string or not second_string:
        return (
            merge_sort_string(first_string),
            merge_sort_string(second_string),
            False,
        )
    first_string = first_string.lower()
    second_string = second_string.lower()
    return (
        merge_sort_string(first_string),
        merge_sort_string(second_string),
        merge_sort_string(first_string) == merge_sort_string(second_string),
    )


if __name__ == "__main__":
    print(is_anagram("amor", "RomA"))
    print(is_anagram("ALEgria", "alergia"))
    print(is_anagram("f", "F"))
