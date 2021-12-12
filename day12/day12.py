from collections import defaultdict
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


def can_step(current_path, next_step):
    if is_lowercase(next_step) and next_step in current_path:
        return False
    for before, after in zip(current_path[:-1], current_path[1:]):
        if before == current_path[-1] and after == next_step:
            return False
    return True
    

def find_paths(path_im_on, path_map):
    paths = []
    current_step = path_im_on[-1]
    next_steps = path_map[current_step]
    for next_step in next_steps:
        if next_step == 'end':
            paths.append(path_im_on + [next_step])
        elif can_step(path_im_on, next_step):
            paths.extend(find_paths(path_im_on + [next_step], path_map))
    return paths


def part_one(filename):
    path_map = build_map(filename)
    paths = find_paths(['start'], path_map)
    return len(paths)


print(part_one('day12/input'))

