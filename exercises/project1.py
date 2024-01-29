import random 


def roll():
  max_value = 6
  min_value = 1
  roll = random.randint(min_value, max_value)
  return roll

while True: # continue to ask the user while their number is valid
  players = input("Enter the number of players (1 - 4): ")
  if players.isdigit():
    players  = int(players)
    if 1 <= players <= 4:
      print
      break
  else: 