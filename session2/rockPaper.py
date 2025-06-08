# Task 4: Rock, Paper, Scissors
# Description:
#  Ask for two players to each enter "rock", "paper" or "scissors".
#  Determine who wins:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# If same → “It’s a tie”
# Example:
# Player 1: rock  
# Player 2: scissors  
# Output: Player 1 wins

playerOne=input("1st input - (Rock, Paper or Scissors): ")
playerTwo=input("2nd input - (Rock, Paper or Scissors): ") 

if playerOne==playerTwo:
    print("It's a tie")
elif (playerOne=="rock" and playerTwo=="scissors" or \
      playerOne=="scissors" and playerTwo=="paper" or \
      playerOne=="paper" and playerTwo=="rock"):
    print("Player 1 wins")
else:
    print("Player 2 wins")