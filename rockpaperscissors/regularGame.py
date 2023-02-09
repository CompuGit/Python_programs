from random import randint

items = {1:'Rock',2:'Paper',3:'Scissors'}

print(format(' Rock-Paper-Sicssors ','=^80'))
print('''
Introduction:
        This game is palyed by the Computer and a User. Every time the user is
    providing an input in the form of numbers(i.e. only 1, 2, 3).

        These represent as below -

        1 for ROCK
        2 for PAPER
        3 for SCISSORS

        At first user must provide an input, that decides how many times the 
    user wanted to play.
    
Rules:
    When choices are like below-

        Rock against Scissors : Rock wins
        Scissors against Paper : Scissors wins
        Paper against Rock : Paper wins

    When the both players having same item, it going to be a tie and that's not 
    calculated in the final Results. But it will displayed in Analysis.
''')

i = loose = win = tie = total = 0
n = int(input('Enter how many times you want to play ? '))

while i<n :
    print()
    computer = randint(1,3)
    user = int(input('user choice : '))

    if user == 1 or 2 or 3:

        if computer == 1 and user != 1 :
            if user == 2:
                print(f'computer choice "{items[computer]}" and user choice "{items[user]}"')
                print(f'### {items[user]} wins ###')
                win += 1
            if user == 3:
                print(f'computer choice "{items[computer]}" and user choice "{items[user]}"')
                print(f'### {items[computer]} wins ###')
                loose += 1

        if computer == 2 and user != 2 :
            if user == 3:
                print(f'computer choice "{items[computer]}" and user choice "{items[user]}"')
                print(f'### {items[user]} wins ###')
                win += 1
            if user == 1:
                print(f'computer choice "{items[computer]}" and user choice "{items[user]}"')
                print(f'### {items[computer]} wins ###')
                loose += 1

        if computer == 3 and user != 3 :
            if user == 1:
                print(f'computer choice "{items[computer]}" and user choice "{items[user]}"')
                print(f'### {items[user]} wins ###')
                win += 1
            if user == 2:
                print(f'computer choice "{items[computer]}" and user choice "{items[user]}"')
                print(f'### {items[computer]} wins ###')
                loose += 1
            
        if user == computer:
            print(f'computer choice "{items[computer]}" and user choice "{items[user]}"')
            print(f'### Tie ###')
            tie += 1
            i-=1
        
    else:
        print('not a valid number.')
        i -= 1
        

    i+=1

print('\n====== Results ======\n')
total = win + loose + tie
if n == win+loose:
    print(f'Total Number of matches played {total}')
    print(f'Number of valid matches played {n}')
    print(f'Number of User Wins {win}')
    print(f'Number of User Losts {loose}')
    print(f'Number of Ties {tie}')


input()
