def build_graph(pairs):
    tribes = [set(pairs[0])]
    for pair in pairs[1:]:
        merged = False
        for tribe in tribes:
            if any(person in tribe for person in pair):
                tribe.update(pair)
                merged = True
                break
        if not merged:
            tribes.append(set(pair))
    return tribes


def count_possible_pairs(tribes):
    count = 0
    pairs = []
    for i in range(len(tribes)):
        for j in range(i + 1, len(tribes)):
            for male in tribes[i]:
                for female in tribes[j]:
                    if male % 2 != female % 2:
                        count += 1
                        pairs.append(f"{male}/{female}")
    return count, pairs


def read_input(file):
    with open(file, 'r') as file:
        N = int(file.readline())
        if not (0 < N < 10000):
            raise ValueError("0 < N < 10000")
        pairs = [tuple(map(int, line.split())) for line in file.readlines()]
    return N, pairs


def write_output(file, result):
    count, pairs = result
    with open(file, 'w') as file:
        file.write(f"{count} (")
        possible_pairs = ', '.join(pairs)
        file.write(f"{possible_pairs})")


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    try:
        N, pairs = read_input(input_file)
        if not (0 < N < 10000):
            raise ValueError("0 < N < 10000")
        tribes = build_graph(pairs)
        result = count_possible_pairs(tribes)
        write_output(output_file, result)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
