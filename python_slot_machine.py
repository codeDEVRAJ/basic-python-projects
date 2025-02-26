import random
def spin_row():
   symbols = ["🍒", "🍉", "🥭", "🔔", "⭐"]
   return [random.choice(symbols) for _ in range(3)]
def print_row(row):
   print("*******************")
   print(" | ".join(row))
   print("*******************")
   
def get_payout(row , bet):
   if row[0] == row[1] == row[2]:
      if row[0] == '🍒':
         return bet*3
      elif row[0] == '🍉' :
         return bet *4
      elif row[0] == '🥭':
         return bet * 5
      elif row[0] == '🔔':
         return bet * 10
      elif row[0] == '⭐':
         return bet *20
   return 0
      

def main():
   balance = 100 
   print("******************")
   print("welcome to the slot machine")
   print("Symbols: 🍒 | 🍉 | 🥭 | 🔔 | ⭐ ")
   print("******************")
   
   while balance > 0:
      print(f"your balance is {balance}")
      bet = input("how much would you like to bet ?")
      
      if not bet.isdigit():
            print("please enter a valid numbers")
            continue
      bet = int(bet)
   
      if bet >balance:
         print("you can't bet more than your balance")
         continue
      if bet<=0 :
         print("you can't bet 0 or negative numbers")
         continue
      balance -= bet
      row = spin_row()
      print("Spinnning...")
      print_row(row)
      
      payout = get_payout(row , bet)
      if payout > 0 :
         print(f"you wan {payout}")
         
      else:
         print("you lost")
      balance += payout
      print(balance)
      
      play_again = input("do you want to play again (Y/N) :").upper()
      if play_again !=  'Y':
         break
   print("**************************************")
   print(f"game over your final balance is  : {balance}")
   print("**************************************")
if __name__ == '__main__':
   main()