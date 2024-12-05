def recognize_number(word):
    one = ['o', 'n', 'e']
    two = ['t', 'w', 'o']
    
    if len(word) == 3:
        for_one = 0
        for_two = 0

        for i in range(3):
            if word[i] in one[i]:
                for_one += 1
            if word[i] in two[i]:
                for_two += 1
                
        if for_one >= 2:
            return 1
        if for_two >= 2:
            return 2
        
    return 3

n = int(input())
words = [input().strip() for _ in range(n)]

for word in words:
    print(recognize_number(word))
