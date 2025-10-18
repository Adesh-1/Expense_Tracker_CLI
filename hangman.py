import random

# Simple sequential-letter hangman-like guesser (reveals middle letters one by one)
# Decorations with emojis and improved spacing + comments for readability.

# Uniform word list: all words are 6 letters long (formal length)
words = ['planet', 'python', 'rocket', 'galaxy', 'forest', 'stream', 'market', 'people']
word = random.choice(words)

# Mask: show first and last letter, hide the middle with underscores
guess_word = f"{word[0]}{'_' * (len(word) - 2)}{word[-1]}"

print(f"🎯 Guess this word --> {guess_word}\n")

tries = 5           # remaining attempts
ind = 1             # current index to guess (we reveal letters sequentially)

while tries > 0:
    try:
        # prompt user for a single character
        n = input("Enter character: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        # handle Ctrl+C / Ctrl+D gracefully
        print(f"\n⏹️ No input received — exiting.")
        break

    # If user pressed Enter without typing anything
    if not n:
        tries -= 1
        print(f"⚠️  Please enter a character.\nYou have {tries} tries left.\n")
        continue

    # Validate input: must be a single alphabetic character
    if len(n) != 1 or not n.isalpha():
        tries -= 1
        print(f"❌ Please enter a single alphabetic character (a-z).\nYou have {tries} tries left.\n")
        continue

    # Ensure the index we are revealing is valid
    if ind >= len(word) - 1:
        # All middle letters already revealed (edge case)
        print(f"✅ All middle positions already revealed.\nFinal word: {word}")
        break

    # Check the guessed character against the current target position
    if n == word[ind]:
        # Build and show current progress: reveal up to current index
        current_progress = f"{word[:ind + 1]}{'_' * (len(word) - ind - 2)}{word[-1]}"
        print(f"✅ Yes! You guessed it right.")
        print(f"Current progress: {current_progress}\n")
        ind += 1

        # If we've revealed all letters (reached the last index), player wins
        if ind == len(word) - 1:
            print(f"🎉 Congratulations! You have guessed the word: {word}")
            break
    else:
        # Wrong guess: decrement tries and show remaining attempts
        tries -= 1
        print(f"❌ Wrong guess! You have {tries} tries left.")
        current_progress = f"{word[:ind]}{'_' * (len(word) - ind - 1)}{word[-1]}"
        print(f"Current progress: {current_progress}\n")


# If loop ends because tries ran out, inform the user
if tries == 0:
    print(f"💀 No tries left. The word was: {word}")