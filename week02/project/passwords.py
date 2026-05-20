"""
Author: Happiness Isaac
W02 Project: Password Strength
Purpose: Prove that you can write functions with parameters and 
call those functions multiple times with arguments.
"""

# EXCEEDING REQUIREMENT
# To exceed assignment expectation i added password history tracking 
# for all tested passwords and strength label (Very Weak → Very Strong ) and display label on quit

# Character set
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
       "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
       "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

DIGITS=["0","1","2","3","4","5","6","7","8","9"]

SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", 
         "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]


# word_file
def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if case_sensitive:
                if line == word:
                    return True
            else: 
                if line.lower() == word.lower():
                    return True
    
    return False

# word_has_character
def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True
    return False

# word_complexity
def word_complexity(word):
    complexity = 0

    # check against manual lists instead fo string module constants
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity

# password_strength
def password_strength(password, min_length=10, strong_length=16):
    word_list_file = "wordlist.txt"
    top_password_file = "toppasswords.txt"

    #check if password is a real dictionary word
    if word_in_file(password, word_list_file, False):
        print("Password is a dictionary word and is not secure.")
        return 0 
    
    # check if password is in known common password list
    if word_in_file(password, top_password_file, True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    #check if password is too short to be safe
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    #evaluate complexity
    complexity = word_complexity(password)
    strength = 1 + complexity
    print(f"Password complexity score: {complexity}")
    
    #check if password is long enough to be considered secure
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    return strength
    
#strength_label (Enhancement)
def strength_label(score):
    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Fair"
    elif score == 3:
        return "Good"
    elif score == 4:
        return "Strong"
    else:
        return "Very Strong 👍"
    
#main function (Interaction with the user)
def main():

    password = ""
    history = []

    while password.lower() != "q":
        print()
        print("To stop testing, type: 'q'")

        password = input("Enter password to test: ")

        #exit condition
        if password.lower()== "q":
            print()
            print("-----PASSWORD HISTORY-----")

            for entry in history:
                print(f"{entry[0]} - strength {entry[1]}/5 ({entry[2]})")
            
            print()
            print("All the best!")
            return
        else:
            strength = password_strength(password)
            label = strength_label(strength)

            print(f"Your password strength is {strength}/5 ({label})")

            #store full record in history
            history.append((password, strength, label))

if __name__ == "__main__":
    main()
