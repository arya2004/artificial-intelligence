import sys

# Global variables
letters = []
letter_to_digit = []
left_words = []
right_word = ""

def word_to_number(word):
    global letter_to_digit
    num = 0
    for c in word:
        idx = letter_index(c)
        if idx == -1:
            return -1
        digit = letter_to_digit[idx]
        if digit == -1:
            return -1
        num = num * 10 + digit
    # Check for leading zero
    if num > 0 and len(str(num)) != len(word):
        return -1
    return num

def letter_index(c):
    global letters
    for i in range(len(letters)):
        if letters[i] == c:
            return i
    return -1

def print_solution():
    global letters, letter_to_digit, left_words, right_word
    print("Solution found:")
    for i in range(len(letters)):
        print(f"{letters[i]} = {letter_to_digit[i]}")
    print("Verification:")
    for i in range(len(left_words)):
        sys.stdout.write(str(word_to_number(left_words[i])))
        if i < len(left_words) - 1:
            sys.stdout.write(" + ")
    sys.stdout.write(f" = {word_to_number(right_word)}")
    print()

def is_valid_assignment():
    global left_words, right_word
    left_sum = 0
    for word in left_words:
        num = word_to_number(word)
        if num == -1:
            return False
        left_sum += num
    right_num = word_to_number(right_word)
    if right_num == -1:
        return False
    return left_sum == right_num

def solve_cryptarithmetic(letter_index):
    global letters, letter_to_digit
    if letter_index == len(letters):
        if is_valid_assignment():
            print_solution()
            return True
        return False
    
    for digit in range(10):
        # Skip if digit is already used
        if digit in letter_to_digit:
            continue
        
        letter_to_digit[letter_index] = digit
        if solve_cryptarithmetic(letter_index + 1):
            return True
        letter_to_digit[letter_index] = -1
    
    return False

def main():
    global letters, letter_to_digit, left_words, right_word
    
    # Example: SEND + MORE = MONEY
    left_words = ["SEND", "MORE"]
    right_word = "MONEY"
    
    # Collect all unique letters
    letter_set = set()
    for word in left_words + [right_word]:
        for c in word:
            letter_set.add(c)
    letters = list(letter_set)
    
    # Initialize assignments
    letter_to_digit = [-1] * len(letters)
    
    print(f"Solving: {' + '.join(left_words)} = {right_word}")
    print(f"Letters: {letters}")
    
    if not solve_cryptarithmetic(0):
        print("No solution found")

if __name__ == "__main__":
    main()