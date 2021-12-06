from collections import Counter, defaultdict


def read_input(filename):
    with open(filename) as file:
        fish = [int(n) for n in file.readline().strip().split(',')]
    return defaultdict(int, Counter(fish))


def age(fish):
    fish = defaultdict(int, fish)
    fish_having_babies = fish[0]
    for i in range(1, 9):
        fish[i-1] = fish[i]
    fish[8] = fish_having_babies
    fish[6] += fish_having_babies
    return fish


def count(fish):
    return sum(fish.values())


def run(fish, days):
    for d in range(days):
        fish = age(fish)
    return count(fish)


def day_one(filename):
    fish = read_input(filename)
    return run(fish, 80)


print(day_one('day6/input'))
