# Play and Win

# import random module
import random

print('Play to Win!!!\n Predict an integer number from 1-10!!!\n If the predicted number match with a number from 1-10 you won else you loose try again!!!')

predicted_number = input("Pick a number from 1-10: ")
random_number = random.randrange(1, 10)

if int(predicted_number) == random_number:
    print('Actual number: ', random_number)
    print('Predicted Number: ', predicted_number)
    print('Congrats, you won!!!')
else:
    print('Actual number: ', random_number)
    print('Predicted Number: ', predicted_number)
    print('You loose!!! Play again')



