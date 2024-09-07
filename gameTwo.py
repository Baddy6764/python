# Play and Win Big #

# modules #
import  random

# info #
print('Play and Win Big!!!')

# numbers #
rand_num = random.randrange(10, 100)
predicted_num = input('Predict a integer number from 10-100: ')

# compare
if int(predicted_num) < 10:
    print('Enter a valid number')


# game func
def game():
    if int(predicted_num) == rand_num:
        print(f'Your prediction {int(predicted_num)}')
        print(f'Actual number {rand_num}')
        print('Congrats, You won!!!')
    else:
        print(f'Your prediction {int(predicted_num)}')
        print(f'Actual number {rand_num}')
        print('You loose, Play again!!!')
game()
