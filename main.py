import random

global score
score = 0
print('>>> The number is between 0 and 100')


def run(score):
    num = random.randint(0, 100)
    print('>>> You have 10 chances LEFT')
    for chance in range(10):
        print(f'chance {chance+1}')
        while True:
            guess = (input("--> Guess the number > "))
            try:
                guess = int(guess)
                break
            except:
                None

        if guess == num:
            print('>>> That guess was correct <<<')
            new_score = score + 5
            print(f">> Your Score is {new_score} <<<")
            run(new_score)
        elif num < guess:
            print('>>> The Number is lessthan Guess')
        elif num > guess:
            print('>>> The number is morethan Guess')
        else:
            None
    print('>>> You Failed <<<')
    print(f'>>> The correct number is {num}')


run(score)
