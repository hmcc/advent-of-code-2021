from collections import defaultdict, Counter
import re

lowercase = re.compile('[a-z]+')


def build_map(filename):
    with open(filename) as file:
        path_map = defaultdict(set)
        for line in file:
            update(path_map, parse(line))
    return path_map


def parse(line):
    return line.strip().split('-')


def is_lowercase(path_element):
    return lowercase.match(path_element) is not None


def update(path_map, new_path):
    path_map[new_path[0]].add(new_path[1])
    path_map[new_path[1]].add(new_path[0])


def visited_small_cave_twice_already(path):
    small_caves = [step for step in path if is_lowercase(step)]
    counts = Counter(small_caves).most_common()
    return counts[0][1] >= 2


def can_step(current_path, next_step, visit_small_cave_twice=False):
    if next_step == 'start':
        return False
    return not (is_lowercase(next_step)
                and next_step in current_path
                and (not visit_small_cave_twice or visited_small_cave_twice_already(current_path)))


def find_paths(path_im_on, path_map, visit_small_cave_twice=False):
    paths = []
    current_step = path_im_on[-1]
    next_steps = path_map[current_step]
    for next_step in next_steps:
        if next_step == 'end':
            paths.append(path_im_on + [next_step])
        elif can_step(path_im_on, next_step, visit_small_cave_twice):
            paths.extend(find_paths(path_im_on + [next_step], path_map, visit_small_cave_twice))
    return paths


def part_one(filename):
    path_map = build_map(filename)
    return len(find_paths(['start'], path_map))


def part_two(filename):
    path_map = build_map(filename)
    return len(find_paths(['start'], path_map, True))


print(part_two('day12/input_sample'))
