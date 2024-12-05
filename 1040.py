notes = list(map(float, input().split()))

media = (notes[0] * 2 + notes[1] * 3 + notes[2] * 4 + notes[3]) / 10

if media >= 7:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif media < 5:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
else:   
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam}")
    media = (media + exam) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
