# NameGenerator

Generate random names based on syllables in a file (Python 3)
Syllable files should put each syllable on a separate line. Blank lines and lines starting with # are ignored.
Sample syllable file is provided but only contains a small number of examples. If only the minimum syllable count
is provided, the name will be exactly that amount of syllables. If the minimum and maximum are provided, the name
generated will have between minimum and maximum syllables.

## Usage

```
python name_generator.py <syllables_file_path> <minimum_syllable_count> [<maximum_syllable_count>]
```

## Example Usages

```
# Exactly 3 syllable name
python name_generator.py syllables.txt 3

# Name with 3 to 5 syllables
python name_generator.py syllables.txt 3 5
```

## Contact

<a href="mailto:nanodano@devdungeon.com">nanodano@devdungeon.com</a>
