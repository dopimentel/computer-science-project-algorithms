def merge_sort(string):
    """Ordena a string usando o algoritmo merge sort."""
    if isinstance(string, str):
        string = list(string)
    if len(string) > 1:
        middle = len(string) // 2
        left_half = string[:middle]
        right_half = string[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

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
    """Faça o código aqui."""
    raise NotImplementedError


print(merge_sort("amor"))
