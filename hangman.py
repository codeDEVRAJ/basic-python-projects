from wordslist import words
import random

hang_man ={ 0:(" ",
                " ",
                " "),
            1:("o",
               " ",
               " "),
            2:("o",
               "|",
               " "),
            3:(" o ",
               "/| ",
               " "),
            4:(" o ",
               "/|\\",
               " "),
            5:(" o",
               "/|\\",
               "/"),
            6:(" o",
               "/|\\",
               "/ \\")
}

def display_man(wrong_guesses):
   print("************************")
   for line in hang_man[wrong_guesses]:
      print(line)
   print("************************")

def display_hint(hint):
   print(" ".join(hint))

def display_answer(answer):
   print(" ".join(answer))
   
def main():
   answer = random.choice(words)
   hint = ["_"] * len(answer)
   wrong_guesses = 0
   guessed_letter = set()
   is_running = True
   
   while is_running:
      display_man(wrong_guesses)
      display_hint(hint)
      guess = input("enter a letter :").lower()
      
      if len(guess) != 1 or not guess.isalpha():  # Fixed the isalpha() method
         print("Invalid input, please enter a single letter.")
         continue
      
      if guess in guessed_letter:
         print(f"{guess} is already guessed")
         continue
      
      guessed_letter.add(guess)
      
      if guess in answer:
         for i in range(len(answer)):
            if answer[i] == guess:
               hint[i] = guess
      else:
         wrong_guesses += 1
         
      if "_" not in hint:
         display_man(wrong_guesses)
         display_answer(answer)
         print("YOU WIN!")
         is_running = False
      elif wrong_guesses >= len(hang_man)-1:
         display_man(wrong_guesses)
         display_answer(answer)
         print("YOU LOSE!")
         is_running = False
         
         play_again = input("Want to play again? (y/n): ").lower()
         if play_again == 'y':
            main()
         else:
            break
   
if __name__ == "__main__":
   main()
