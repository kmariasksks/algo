def count_pairs(N, pair):
    graph = {}

    for male, female in pair:
        if male not in graph:
            graph[male] = []
        graph[male].append(female)

    odd_males = set()
    even_females = set()

    for person, partner_list in graph.items():
        if person % 2 == 1:
            odd_males.add(person)
        for partner in partner_list:
            if partner % 2 == 0:
                even_females.add(partner)

    tribal_pair = len(odd_males) * len(even_females)

    return tribal_pair


def read_input_from_file(file):
    with open(file, 'r') as file:
        N = int(file.readline().strip())
        pair = [tuple(map(int, line.strip().split())) for line in file]

    return N, pair


def write_output_to_file(file, result):
    with open(file, 'w') as file:
        file.write(str(result))


input_file = 'input.txt'
output_file = 'output.txt'

N, pair = read_input_from_file(input_file)
result = count_pairs(N, pair)
write_output_to_file(output_file, result)
