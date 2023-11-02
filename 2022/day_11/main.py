import os
import errno
import re
import math
from colorama import Fore, Style


def get_numbers(entry, is_list=False):
    number = re.findall(r"\d+", entry)
    if is_list:
        return [int(x) for x in number]
    else:
        return int(number[0]) if len(number) > 0 else None


def get_operator(entry):
    operator = re.findall(r"[^a-zA-Z\d\s]", entry)
    return operator[0] if len(operator) > 0 else None


def calculate_worry_level(entry, item):
    value = get_numbers(entry)

    if value != None:
        result = eval(f"{item} {get_operator(entry)} {value}")
    else:
        result = eval(f"{item} {get_operator(entry)} {item}")

    return result


def parse(entry):
    if not os.path.exists(entry):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), entry)

    with open(entry, "r") as f:
        lines = f.readlines()

    monkeys = []
    for i, line in enumerate(lines):
        if line.startswith("Monkey"):
            monkey = {
                "items": get_numbers(lines[i + 1], True),
                "operation": lines[i + 2][19:].strip(),
                "test": get_numbers(lines[i + 3]),
                "true": get_numbers(lines[i + 4]),
                "false": get_numbers(lines[i + 5]),
                "count": len(get_numbers(lines[i + 1], True)),
            }
            monkeys.append(monkey)

    return monkeys


def solve_part_one(entry):
    if entry == None or len(entry) == 0:
        raise TypeError("Missing entry argument or empty list")

    for _ in range(20):
        for monkey in entry:
            # take the first item from the items list

            while len(monkey["items"]) > 0:
                item = monkey["items"].pop(0)
                # calculate worry level
                worry_level = calculate_worry_level(monkey["operation"], item)
                # test worry level
                test = math.floor(worry_level / 3)

                if test % monkey["test"] == 0:
                    # if worry level is even, add true value to item
                    entry[monkey["true"]]["items"].append(test)
                    entry[monkey["true"]]["count"] += 1
                else:
                    # if worry level is odd, add false value to item
                    entry[monkey["false"]]["items"].append(test)
                    entry[monkey["false"]]["count"] += 1

    totals = []
    print()
    for monkey in entry:
        monkey["count"] -= len(monkey["items"])
        totals.append(monkey["count"])
        print(f"items {monkey['items']} count {monkey['count']}")
    print()

    totals.sort()
    total = totals[-1] * totals[-2]
    return total


def solve_part_two(entry):
    if entry == None or len(entry) == 0:
        raise TypeError("Missing entry argument or empty list")

    mod = 1
    for monkey in entry:
        mod *= monkey["test"]

    for _ in range(10000):
        for monkey in entry:
            # take the first item from the items list

            while len(monkey["items"]) > 0:
                item = monkey["items"].pop(0)
                # calculate worry level
                worry_level = calculate_worry_level(monkey["operation"], item)
                # test worry level
                test = worry_level
                test %= mod
                if test % monkey["test"] == 0:
                    # if worry level is even, add true value to item
                    entry[monkey["true"]]["items"].append(test)
                    entry[monkey["true"]]["count"] += 1
                else:
                    # if worry level is odd, add false value to item
                    entry[monkey["false"]]["items"].append(test)
                    entry[monkey["false"]]["count"] += 1

    totals = []
    print()
    for monkey in entry:
        monkey["count"] -= len(monkey["items"])
        totals.append(monkey["count"])
        print(f"count {monkey['count']}")
    print()

    totals.sort()
    total = totals[-1] * totals[-2]
    return total


if __name__ == "__main__":
    entry = parse("input.txt")

    # part_one_result = solve_part_one(entry)
    # print(f"Challenge result Part One: {Fore.LIGHTCYAN_EX}{part_one_result}")

    print(Style.RESET_ALL)

    # To solve part two dont run part one above
    part_two_result = solve_part_two(entry)
    print(f"Challenge result Part Two: {Fore.MAGENTA}{part_two_result}")
