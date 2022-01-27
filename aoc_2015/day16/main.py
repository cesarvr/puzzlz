inputFile = ''

sample = {'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1}

sample2 = {'children': lambda n: n == 3,
           'cats': lambda n: n == 7,
           'samoyeds': lambda n: n == 2,
           'pomeranians': lambda n: n == 3,
           'akitas': lambda n: n == 0,
           'vizslas': lambda n: n == 0,
           'goldfish': lambda n: n == 5,
           'trees': lambda n: n == 3,
           'cars': lambda n: n == 2,
           'perfumes': lambda n: n == 1
           }


sample3 = {'children': lambda n: n == 3,
           'cats': lambda n: n > 7,
           'samoyeds': lambda n: n == 2,
           'pomeranians': lambda n: n < 3,
           'akitas': lambda n: n == 0,
           'vizslas': lambda n: n == 0,
           'goldfish': lambda n: n < 5,
           'trees': lambda n: n > 3,
           'cars': lambda n: n == 2,
           'perfumes': lambda n: n == 1
           }


with open('input.txt', 'r') as f:
    inputFile = f.readlines()


def extract_headers(tokens):
    token = tokens.pop(0).split()
    return [token[2].rstrip(':'), int(token[3])]


def extract_body(token):
    splitted = token.split()
    return [splitted[0].rstrip(':'), int(splitted[1])]


def process(lines):
    sue_list = []
    for line in lines:
        vec = []

        tokens = line.split(',')
        vec.append(extract_headers(tokens))

        for token in tokens:
            tmp = extract_body(token)
            vec.append(tmp)

        sue_list.append(vec)
    return sue_list


def find_sue(list_of_sue, sample_target):
    max_match = [-1, -1]
    sue_index = 1
    for sue in list_of_sue:
        matches = 0
        for prop in sue:
            property_name = prop[0]
            property_value = prop[1]
            if property_name in sample_target:
                if sample_target[property_name](property_value):
                    matches += 1

        if max_match[0] < matches:
            max_match = [matches, sue_index]

        sue_index += 1

    return max_match


sue_s = process(inputFile)
solution = find_sue(sue_s, sample2)
print('solution: ', solution)

solution2 = find_sue(sue_s, sample3)
print('solution2: ', solution2)