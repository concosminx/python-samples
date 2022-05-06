def interact():
    while True:
        try:
            user_input = int(input('Please input an integer:'))    # try to turn user input into an integer
        except ValueError:
            print('Please input integers only.')  
        else:
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     
        finally:    
            user_input = input('Do you want to play again? (y/N):')     
            if user_input != 'y':       
                print('Goodbye.')
                break

interact()