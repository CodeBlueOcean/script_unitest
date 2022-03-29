# example 1 uncomment to run
# from distutils.log import error
# from multiprocessing.sharedctypes import Value


# def do_stuff(num=0):
#     try:
#         if num: 
#             return int(num) + 5
#         else: 
#             return 'please enter number' 
#     except ValueError as err:
#         return err 
    

# example 2 uncomment to run (can't used the break keyword if we are outside of the loop, this ex while loop), we can have a return here 

import random 

def run_guess(guess):
    if 0 < guess < 11:
            if guess == answer: 
                print('you are a genius!')
                return True
    else:
            print('hey bozo, I said 1~10')
            return False    


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:   '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue 




