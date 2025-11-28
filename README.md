# Hangman Game — Python (User vs Computer)

This is a Python implementation of the classic Hangman game, but with a twist:
- **Player 1 (User)** chooses a secret 5-letter word.
- **Player 2 (Computer)** tries to guess the letters randomly.
- The hangman drawing progresses with every wrong computer guess.
- The computer wins if it guesses all letters correctly before reaching 5 wrong guesses.

---

## 🔧 How the Game Works

1. The user enters a **5-letter secret word**.
2. The computer randomly guesses letters from the English alphabet.
3. If the guessed letter is correct:
   - It is revealed in the word.
4. If the guessed letter is incorrect:
   - A new part of the hangman is drawn.
5. The game ends when:
   - The computer reveals all letters (**Computer wins**)  
   - OR the hangman is fully drawn (**User wins**)

---

## 🧠 Features
- ASCII-art hangman drawings  
- Computer guesses letters without repeating  
- Correct letter placement handling  
- Tracks wrong guesses  
- Handles user input cleanup  
- Works fully in the terminal  

---

## ▶️ How to Run

1. Install Python (3.x recommended)
2. Save the script as `hangman.py`
3. Run:


4. Enter a **5-letter word** when asked.
5. Watch the computer try to guess it.

---

## 💡 Example Output

Enter a random word of 5 letters: loses
computer guessed: t
| |
O |
|
|

computer guessed: o
correct guess: -o---
...
User wins the game


---

## 🚀 Future Improvements
- Add difficulty levels  
- Improve computer guessing strategy using word frequency  
- Add input validation for word length  
- Add option for user to guess computer’s word  

---

## 📂 Files in Repository
- `hangman.py` → Main game script  
- `README.md` → Documentation  

---

## 🛠️ Technologies Used
- Python  
- `random` module  
- `string` module  

---

## 👤 Author
Deekshitha  
CSE Student — Python & DSA Learner  
Interested in Data Science & Open Source  

