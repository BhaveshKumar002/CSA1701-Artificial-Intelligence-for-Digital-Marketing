from itertools import permutations

def solve_cryptarithmetic():
    a = input("Enter first word\n")
    b = input("Enter second word\n")
    c = input("Enter third word\n")
    puzzle = [a, b, c]
    unique_letters = set(''.join(puzzle))
    if len(unique_letters) > 10:
        return None
    digit_permutations = permutations('0123456789', len(unique_letters))

    for digit_permutation in digit_permutations:
        letter_to_digit = dict(zip(unique_letters, digit_permutation))
        replaced_puzzle = [''.join([letter_to_digit[letter] for letter in word]) for word in puzzle]
        if int(replaced_puzzle[0]) + int(replaced_puzzle[1]) == int(replaced_puzzle[2]):
            return letter_to_digit
    return None

solution = solve_cryptarithmetic()

if solution:
    print("Solution found:")
    for word in solution:
        replaced_word = ''.join([solution[letter] for letter in word])
        print(f"{word} = {replaced_word}")
else:
    print("No solution found.")
