def main(c):

    n_balls, guesses = map(int, input().split())
    if n_balls == 0 and guesses == 0:
        return
    else:
        balls = [int(input()) for _ in range(n_balls)]
        
        print(f"CASE# {c}:")

        for _ in range(guesses):
            guess = int(input())
            if guess in balls:
                position = balls.index(guess) + 1
                print(f"{guess} found at {position + 1}")
            else:
                print(f"{guess} not found")
        return main(c + 1)

if __name__ == '__main__':
    main(1)
    