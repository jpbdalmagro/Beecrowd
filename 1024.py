def first_factor(word: list) -> list:
    for i in range(len(word)):
        if word[i].isalpha():
            word[i] = chr(ord(word[i]) + 3)
    return word
    
def second_factor(word: list) -> list:
    word = word[::-1]
    return word

def third_factor(word: list) -> list:
    for i in range(len(word) // 2, len(word)):
        word[i] = chr(ord(word[i]) - 1)
    return word

cases = int(input())

for i in range(cases):
    password = list(input())
    print("".join(third_factor(second_factor(first_factor(password)))))
    