###########################################################################
# M HAINS                                                                 #
# MC test                                                                 #
###########################################################################

print ('WELCOME TO THE MULTIPLE CHOICE TEST\n')
name = raw_input('WHAT IS YOUR NAME? ')
print ('\nHI THERE ' + name + '! LET''S PLAY A GAME!\n')
print ('I will ask you 10 questions and give you three choices for each question.\n\nYou select which choice is the correct answer. Eg. A, B or C\n')
print ('Important : Please keep your CAPS LOCK on')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                          SET THE SCORE TO ZERO                          #
###########################################################################

score = 0
score = int(score)  #Convert the 0 into a number so we can add scores


###########################################################################
#                           QUESTION 1                                    #
###########################################################################

print ('QUESTION 1: WHAT IS THE LARGEST OCEAN IN THE WORLD?\n')
print ('A. The Indian Ocean')
print ('B. The Pacific Ocean')
print ('C. The Atlantic Ocean')
print ('')

Q1answer = "B"
Q1response= raw_input('Your answer : ')

if (Q1response != Q1answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q1response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10')
print ('\n-----------------------------------------------------------\n')

###########################################################################
#                           QUESTION 2                                    #
###########################################################################

print ('QUESTION 2: AUSTRALIA IS A ...\n')
print ('A. continent')
print ('B. island')
print ('C. very hot place')
print ('')

Q2answer = "A"
Q2response= raw_input('Your answer : ')

if (Q2response != Q2answer):
    print ('Sorry, that is incorrect!')
else:
    print ('Well done! ' + Q2response + ' is correct!')
    score = score + 1

print ('Your current score is ' + str(score) + ' out of 10') 
print ('\n-----------------------------------------------------------\n')


# continue in the same format to produce a quiz of 10 questions
# Thank you message the end with TOTAL score