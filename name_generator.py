"""
Very simple name generator that takes random syllables from a file
and mixes them together.
"""
import random
import sys


def print_usage():
    print("=========")
    print("Usage: name_generator <syllables_file_path> <syllable_count_for_name>")
    print("Example: python name_generator.py syllables.txt 5")
    print("=========")
    print("Syllable files should put each syllable on a separate line. Lines beginning with # are ignored.")
    print("=========")


def main():
    # Check args
    if len(sys.argv) < 3:
        print_usage()
        exit(1)

    # Parse args in to vars
    syllable_file_path = sys.argv[1]
    min_syllable_count = sys.argv[2]
    if len(sys.argv) > 3:
        max_syllable_count = sys.argv[3]
    else:
        max_syllable_count = min_syllable_count

    # Load syllables from file
    syllables = []
    with open(syllable_file_path) as syllable_file:
        for line in syllable_file:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == "#":
                continue
            syllables.append(line)

    # Generate the name
    name = ""
    for i in range(0, random.randint(int(min_syllable_count), int(max_syllable_count))):
        name += syllables[random.randint(0, len(syllables) - 1)]
    print(name)


main()
