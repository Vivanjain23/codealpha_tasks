import random

# List of predefined words
words = ["python", "computer", "college", "coding", "student"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print(f"You have {max_wrong} incorrect guesses.\n")

while wrong_guesses < max_wrong:
    # Display current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    # Check if player has guessed the word
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!\n")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong! Attempts left: {max_wrong - wrong_guesses}\n")

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)