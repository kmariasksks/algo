def longest_chain(words):
    if not (1 <= len(words) <= 10**5):
        raise ValueError("Кількість слів у словнику повинна бути від 1 до 10^5")

    iterations = 0

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            iterations += 1
            if len(words[i]) > len(words[j]):
                words[i], words[j] = words[j], words[i]

    dp = {word: 1 for word in words}
    for word in words:
        if not (1 <= len(word) <= 50):
            raise ValueError("Довжина кожного слова повинна бути від 1 до 50 символів")
        if not word.islower():
            raise ValueError("Слово повинно складатися з малих латинських літер від a до z")
        for i in range(len(word)):
            iterations += 1
            prev_word = word[:i] + word[i+1:]
            if prev_word in dp:
                dp[word] = max(dp[word], dp[prev_word] + 1)

    print("Кількість ітерацій:", iterations)
    return max(dp.values())

with open('D:/algo7/src/wchain_in.in', 'r') as file:
    words = file.read().splitlines()[1:]

result = longest_chain(words)

with open('D:/algo7/src/wchain_out.out', 'w') as file:
    file.write(str(result))
