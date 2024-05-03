frase = input("Digite uma frase: ")
ql =0
qv =0
qc = 0
eb = 0
for letra in frase:
    if letra in "aeiouAEIOU":
        qv = qv + 1
    elif letra in "bcdfghjklmnpqrstvwxyz":
        qc = qc + 1
    elif letra == " ":
        eb = eb + 1
ql = qv + qc
print(qc,qv,eb,ql)
