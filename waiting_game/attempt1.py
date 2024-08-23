from random import randrange
from time import time


class Solution:
    def waiting_game(self):
        self.play()
    
    def play(self):
        self.greet()

        while True:
            rand_sec = self.get_rand_sec()
            answer = self.prompt_user(rand_sec)
            if answer.lower() == 'q':
                break
            elif answer.lower() == '':
                user_time = self.time_user()
                self.evaluate_game(user_time, rand_sec)
            else:
                print('invalid input'.title())
        
        print('Thanks for playing!')

    def greet(self):
        print(
            'Welcome to the waiting game!\n'  
        )

    def get_rand_sec(self):
        return randrange(2, 5)
    
    def prompt_user(self, rand_sec):
        
        print('Press enter and press enter again\n' +
              f'exactly {rand_sec} later and you win.\n\n')
        
        return input('Press enter to start, or q to quit: ')

    def time_user(self):
        start, end = time(), None

        answer = input()
        if answer == '':
            end = time()
            return end - start
    
    def evaluate_game(self, user_time, rand_sec):
        if user_time == rand_sec:
            print('Spot on! You win.')
        elif user_time < rand_sec:
            print(f'You were early by {(rand_sec - user_time):.2f} seconds')
            print('You lose. Please try again')
        else:
            print(f'You were late by {(user_time - rand_sec):.2f} seconds')
            print('You lose. Please try again')
        
        print('\n' + '-' * 29 + '\n')
        
        
Solution().play()