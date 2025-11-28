import random
import string
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
       |   |
           |
    =========
    """,

    """
      -----
      |   |
      O   |
    / |   |
          |
  =========

""",

"""
      -----
      |   |
      O   |
    / | \ |
          |
  =========
""",
"""
      -----
      |   |
      O   |
    / | \ |
      |   |
  =========
""",
"""
      -----
      |   |
      O   |
    / | \ |
    / |   |
  =========
""",
"""
      -----
      |   |
      O   |
    / | \ |
    / | \ |
  =========
"""
]

player1 = "user"
player2 = "computer"

user_word = input("Enter a random word of 5 letters : ").lower()
word1 = ["-","-","-","-","-"]

wrong_guesses = 0
guessed_words = []

while wrong_guesses < 5 and "-" in word1:
 
     computer_guess = random.choice(string.ascii_letters).lower()
 
     if computer_guess in guessed_words:
      continue
     guessed_words.append(computer_guess)
     print("computer guessed:",computer_guess)

     if computer_guess in user_word:
      for i in range(len(user_word)):
       if user_word[i] == computer_guess:
         word1[i] = computer_guess
      print("correct guess:","".join(word1))
 
     else:
      wrong_guesses += 1
      print(hangman_stages[wrong_guesses])

if "-" not in word1:
    print("Computer wins the game")
else:
    print("User wins the game")














