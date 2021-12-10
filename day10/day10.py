pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def read_file(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def score(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        elif pairs[stack[-1]] == c:
            stack.pop()
        else:
            return scores[c]
    return 0


def part_one(filename):
    return sum(score(line) for line in read_file(filename))


print(part_one('day10/input'))
