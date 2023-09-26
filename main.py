def find_largest_k(numbers, k):
    numbers.sort(reverse=True)
    largest_k_number = numbers[k - 1]
    largest_k_index = numbers.index(largest_k_number)
    return largest_k_number, largest_k_index

if __name__ == '__main__':
    numbers = [15, 7, 22, 9, 36, 2, 42, 18]
    k = 3
    result = find_largest_k(numbers, k)

    print(f"Вхідний масив {numbers}. Задане k = {k}. {k}-й найбільший елемент та його позиція для numbers: {result}")
