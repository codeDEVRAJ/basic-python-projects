import random
guesses = 1
score = 0
lowest_num = 1
Highest_num = 100
answer = random.randint(lowest_num , Highest_num)
is_running = True
print("this is the python number guessing game ")
print(f"select the number between {lowest_num} and {Highest_num}")
while is_running:
   guess = input("guess the number")
   if guess.isdigit() :
      guess = int(guess)
      guesses += 1
      if guess < lowest_num or guess > Highest_num:
         print(f"{guess} is out of range")
         print(f"please select the number between {lowest_num} and {Highest_num}")
      elif guess < answer :
         print(f"{guess} is Too Low ! try again")
         # score +=1
      elif guess > answer:
         print(f"{guess} Too High ! , Try again")
         # score += 1
         
      elif guess == answer:
         print(f"{guess} Is Correct !")
         # score += 1
         print(f"you guessed the number in {guesses} attempts")

   else:
      print(f" {guess} is invalid guess")
      print(f"please select the number between {lowest_num} and {Highest_num}");
   
   