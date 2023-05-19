import csv
from typing import Iterable
from argparse import ArgumentParser


def read_nums(file_name: str):
    with open('numbers.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                yield int(row[0])
            except ValueError:
                pass


def max_positive_subsequence(nums: Iterable) -> int:
    max_length = 0
    cur_l = 0
    for num in nums:
        if num > 0:
            cur_l += 1
            max_length = max(max_length, cur_l)
        else:
            max_length = max(max_length, cur_l)
            cur_l = 0
    return max_length


def write_csv(filename, data: Iterable) -> None:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)


if __name__ == '__main__':
    argp = ArgumentParser()
    argp.add_argument("-f", "--file", action='store')
    argp.add_argument("-t", "--targetfile", action='store')
    args = argp.parse_args()

    if args.file:
        source_file = args.file
    else:
        source_file = "numbers.csv"
    if args.targetfile:
        target = args.targetfile
    else:
        target = "numbers_out.csv"

    nums = read_nums(source_file)
    write_csv(target, [["max_length"], [max_positive_subsequence(nums)]])
