def naive_search_last_occurrence(haystack, needle):
    comparisons = 0

    m, n = len(haystack), len(needle)
    last_occurrence = -1

    for i in range(m - n + 1):
        match = True
        for j in range(n):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break

        if match:
            last_occurrence = i

    return last_occurrence, comparisons

haystack = "masha"
needle = "sh"
result, comparisons = naive_search_last_occurrence(haystack, needle)

print(f"Останнє входження '{needle}' в '{haystack}' знаходиться на індексі {result}.")
print(f"Кількість порівнянь символів: {comparisons}")
