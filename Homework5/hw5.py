from itertools import permutations

def is_solvable(words, result):
    # Combine all characters in words and result
    all_chars = set(''.join(words) + result)

    # Check if there are more than 10 unique characters
    if len(all_chars) > 10:
        return False

    # Assign the value 1 to the first letter in the result
    char_to_digit = {result[0]: 1}

    # Propagate the assignment to other occurrences of the first letter in words
    for word in words:
        if result[0] in word:
            char_to_digit[word[word.index(result[0])]] = 1

    # Generate all possible permutations of digits 0-9
    # Note: the first permutation should not have leading zeros
    permutations_list = [p for p in permutations(range(10), len(all_chars)) if p[0] != 0]

    # Iterate through each permutation and check if it satisfies the equation
    for perm in permutations_list:
        char_to_digit.update(dict(zip(all_chars, perm)))

        # Check if any leading character is assigned the digit 0
        if any(char_to_digit[word[0]] == 0 for word in words) or char_to_digit[result[0]] == 0:
            continue

        word_values = [int(''.join(str(char_to_digit[c]) for c in word)) for word in words]
        result_value = int(''.join(str(char_to_digit[c]) for c in result))

        if sum(word_values) == result_value:
            # Print the assigned digit values
            print("Assigned Digit Values:")
            for char, digit in char_to_digit.items():
                print(f"{char}: {digit}")
            return True

    # If no permutation satisfies the equation, return False
    return False

# Example usage:
words1 = ["SEND", "MORE"]
result1 = "MONEY"

words2 = ["TO", "GO"]
result2 = "OUT"

words = ["SIX", "SEVEN", "SEVEN"]
result = "TWENTY"

words3 = ["LEET", "CODE"]
result3 = "POINT"

result_found1 = is_solvable(words1, result1)
if result_found1:
    print("The first equation is solvable.")
else:
    print("The first equation is not solvable.")

result_found2 = is_solvable(words2, result2)
if result_found2:
    print("The second equation is solvable.")
else:
    print("The second equation is not solvable.")


result_found3 = is_solvable(words3, result3)
if result_found3:
    print("The third equation is solvable.")
else:
    print("The third equation is not solvable.")
