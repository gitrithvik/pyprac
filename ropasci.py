#! /usr/bin/python
import random, sys ,time, os
"""Implement simple rock paper scissors"""
os.system("clear")
options = ["Rock","Paper","Scissors"]


def countdown():
	print "\nLet's GO!!"
	time.sleep(1)
	print "Rock!"
	time.sleep(1)
	print "Paper!"
	time.sleep(1)
	print "Scissors!"

def get_rounds(): #Gets number of rounds from player
	rounds =0
	rounds = raw_input("Choose number of rounds:")
	return rounds

def playRock(result): #If user chooses rock
	print "\nYou chose Rock"
	ai_choice = random.randint(-1,1)
	countdown()
	if ai_choice ==1:
		print "\nI choose Scissors","\nYou won this round"
		result+=1
		return result
	elif ai_choice ==0:
		print "\nI choose Paper","\nYou lost this round"
		result-=1
		return result
	elif ai_choice== -1:
		print "\nI choose Rock","\nDraw"
		return result

def playPaper(result): #if user chooses paper
	print "\nYou chose Paper"
	ai_choice = random.randint(-1,1)
	countdown()
	if ai_choice ==1:
		print "\nI choose Scissors","\nYou lost this round"
		result-=1
		return result
	elif ai_choice ==0:
		print "\nI choose Paper","\nDraw"
		return result
	elif ai_choice== -1:
		print "\nI choose Rock","\nYou won this round"
		result+=1
		return result

def playScissors(result): #if user chooses scissors
	print "\nYou chose Scissors"
	ai_choice = random.randint(-1,1)
	countdown()
	if ai_choice ==1:
		print "\nI choose Scissors","\nDraw"
		return result
	elif ai_choice ==0:
		print "\nI choose Paper","\nYou won this round"
		result+=1
		return result
	elif ai_choice== -1:
		print "\nI choose Rock","\nYou lost this round"
		result-=1
		return result
		
print "\t"*7, "Welcome to Rock Paper Scissors"
rounds=int(get_rounds())

"""Check if user chooses odd rounds"""

while rounds % 2 ==0:
	print "\nPlease enter an odd number of rounds"
	rounds = int(get_rounds())
total = 0

"""Start the game"""
start=0
while start < rounds:
	if total == (rounds/2)+1:
		break
	elif total == ((rounds/2)+1)*-1:
		break
	else:	
		print "\nPlease enter your choice of:"
		for i in options:
			print i,"\t"
		choice = raw_input("\nPlease type in the choice correctly: ")
		
		if choice == "Rock" or choice[0] == "R" or choice[0] == "r":
			total=playRock(total)
			print total
			start+=1
		elif choice == "Paper" or choice[0] == "P" or choice[0] == "p":
			total=playPaper(total)
			print total
			start+=1
		elif choice == "Scissors" or choice[0] == "S" or choice[0] == "s":
			total=playScissors(total)
			print total
			start+=1
		else:
			print"\nPlease enter from the list of given choice"

"""Result"""

if total > 0:
	print "\nYou won!!"
elif total < 0:
	print "\nDamn, you got bested. Try again next time"
else:
	print "\nDraw! You're as good as a machine!"