#! /usr/bin/python
import random, sys ,time
"""Implement simple rock paper scissors"""

options = ["Rock","Paper","Scissors"]

def get_rounds(): #Gets number of rounds from player
	rounds =0
	rounds = raw_input("Choose number of rounds:")
	return rounds

def playRock(result):
	
	ai_choice = random.randint(-1,1)

	if ai_choice ==1:
		print "Scissors"
		result+=1
		return result
	elif ai_choice ==0:
		print "Paper"
		result-=1
		return result
	elif ai_choice== -1:
		print "Rock"
		return result

def playPaper(result):
	
	ai_choice = random.randint(-1,1)

	if ai_choice ==1:
		print "Scissors"
		result-=1
		return result
	elif ai_choice ==0:
		print "Paper"
		return result
	elif ai_choice== -1:
		print "Rock"
		result+=1
		return result

def playScissors(result):
	
	ai_choice = random.randint(-1,1)

	if ai_choice ==1:
		print "Scissors"
		return result
	elif ai_choice ==0:
		print "Paper"
		result+=1
		return result
	elif ai_choice== -1:
		print "Rock"
		result-=1
		return result
		
print "Welcome to Rock Paper Scissors"
rounds=int(get_rounds())

"""Check if user chooses odd rounds"""

while rounds % 2 ==0:
	print "Please enter an odd number of rounds"
	rounds = int(get_rounds())
total = 0

"""Start the game"""

while rounds > 0:
	
		print "Please enter your choice of:"
		for i in options:
			print i
		choice = raw_input("Please type in the choice correctly: ")
		print "Let's Go! "
		time.sleep(1)
		print "Rock"
		time.sleep(1)
		print "Paper"
		time.sleep(1)
		print "Scissors"
		if choice == "Rock" or choice[0] == "R" or choice[0] == "r":
			total=playRock(total)
			print total
		elif choice == "Paper" or choice[0] == "P" or choice[0] == "p":
			total=playPaper(total)
			print total
		elif choice == "Scissors" or choice[0] == "S" or choice[0] == "s":
			total=playScissors(total)
			print total
		rounds-=1

"""Result"""

if total > 0:
	print "You won!!"
elif total < 0:
	print "Damn, you got bested. Try again next time"
else:
	print "Draw! You're as good as a machine!"