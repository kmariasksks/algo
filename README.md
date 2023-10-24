# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"

## Виконала: Куліш Марія Сергіївна (Група ІР-23)

### Лабораторна робота №1 (Варіант 3 Рівень 2)

Масив вважається монотонним, якщо всі його елементи розташовані в зростаючому або спадаючому порядку.

Завдання: Напишіть функцію, яка перевіряє, чи є заданий масив монотонним. Функція повинна повертати логічне значення True, якщо масив є монотонним, і False, якщо масив не є монотонним.

Приклад вхідних даних і результатів:

Для масиву [1, 2, 3, 4, 5] функція повертає True, оскільки всі елементи зростають монотонно.
Для масиву [5, 4, 3, 2, 1] функція повертає True, оскільки всі елементи спадають монотонно.
Для масиву [1, 2, 2, 3, 2, 4] функція повертає False, оскільки масив не є строго монотонним.
Зверніть увагу, що масив із однаковими значеннями наступного елемента вважається монотонним.

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest .

***
### Лабораторна робота №2 (Варіант 3 Рівень 2)

Горила Джекі  із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами, у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід зоопарку на Н годин, протягом якого Джекі може поласувати своєю улюбленою стравою.

Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти. Якщо кошик має менше, ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години.

Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться.

Напишвть функцію, яка повертає мінімальне ціле число К, яке дозволить Джекі з'їсти всі банани на складі протягом Н годин, поки повернеться охорона.

Приклад 1: piles = [3,6,7,11], H = 8
Результат: 4

Приклад 2: piles = [30,11,23,4,20], H = 5
Результат: 30

Приклад 3: piles = [30,11,23,4,20], H = 6
Результат: 23

Важливо: 1 <= piles.length <= 10^4 piles.length <= H <= 10^9 1 <= piles[i] <= 10^9

Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище
***
### Лабораторна робота №3 (Варіант 3 Рівень 2)

Напишіть функцію, яка виконає операцію інвертування (перевернення) бінарного дерева таким чином, щоб лівий дочірній вузол став правим, а правий дочірній вузол став лівим.

Нехай у вас задане бінарне дерево такого вигляду:

    1
   / \
  2   3
 / \ / \
4  5 6  7
Ваша функція має повернути дерево, яке виглядатиме наступним чином:
    1
   / \
  3   2
 / \ / \
7  6 5  4
Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:
class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
Ваша функція має мати такий вигляд:
def invert_binary_tree(tree) -> BinaryTree:
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
Ваша функція має повернути об'єкт класу BinaryTree. Для спрощення тестування даної функції достатньо реалізувати порівняння значень вузлів дерева
