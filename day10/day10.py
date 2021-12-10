pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


completion_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


syntax_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


class ClosingCharacterError(Exception):
    def __init__(self, character: str, *args: object) -> None:
        super().__init__(*args)
        self.character = character


def read_file(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                yield line


def parse(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        elif pairs[stack[-1]] == c:
            stack.pop()
        else:
            raise ClosingCharacterError(c)
    return stack


def syntax_score(line):
    try:
        parse(line)
        return 0
    except ClosingCharacterError as e:
        return syntax_scores[e.character]


def completion_score(line):
    score = 0
    try:
        stack = parse(line)
        while(len(stack) > 0):
            score = score * 5 + completion_scores[pairs[stack.pop()]]
    except ClosingCharacterError as e:
        pass
    return score


def part_one(filename):
    return sum(syntax_score(line) for line in read_file(filename))


def part_two(filename):
    scores = [completion_score(line) for line in read_file(filename)]
    scores = [score for score in scores if score > 0]
    scores.sort()
    return scores[len(scores) // 2]


print(part_two('day10/input'))
