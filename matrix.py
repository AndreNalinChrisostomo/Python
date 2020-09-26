colunaA = []
colunaB = []
colunaC = []

colunaA2 = []
colunaB2 = []

colunaA3 = []
colunaB3 = []

# primeira matriz
print("\nlinhas da primeira coluna da primeira matriz\n")

a1 = int(input("qual o valor do primeiro elemento da priemira coluna da primeia matriz?: "))
colunaA.append(a1)
a2 = int(input("qual o valor do segundo elemento da segunda coluna da primeira matriz?: "))
colunaA.append(a2)

print("\n")


print("\nlinhas da segunda coluna da  primeira matriz\n")

b1 = int(input("qual o valor do primeiro elemento da segunda coluna da primeira matriz?: "))
colunaB.append(b1)
b2 = int(input("qual o valor do segundo elemento da segunda coluna da primeira matriz??: "))
colunaB.append(b2)


print("\nlinhas da terceira coluna da  primeira matriz\n")

c1 = int(input("qual o valor do primeiro elemento da terceira coluna da primeira matriz?: "))
colunaC.append(c1)
c2 = int(input("qual o valor do segundo elemento da terceira coluna da primeira matriz?: "))
colunaC.append(c2)

#segunda matriz
print("\nlinhas da primeira coluna da segunda matriz\n")
a12 = int(input("qual o valor do primeiro elemento da  primeira coluna da segunda matriz?: "))
colunaA2.append(a12)
a22 = int(input("qual o valor do segundo elemento da primeira coluna da segunda matriz?: "))
colunaA2.append(a22)
a32 = int(input("qual o valor do terceiro elemento da primeira coluna da segunda matriz?: "))
colunaA2.append(a32)


print("\nlinhas da segunda coluna da segunda matriz\n")

b12 = int(input("qual o valor do primeiro elemento da segunda coluna da segunda matriz?: "))
colunaB2.append(b12)
b22 = int(input("qual o valor do segundo elemento da segunda coluna da segunda matriz?: "))
colunaB2.append(b22)
b32 = int(input("qual o valor do terceiro elemento da segunda coluna da segunda matriz?: "))
colunaB2.append(b32)

print(" ")


r1_3 = colunaA[0] * colunaA2[0]
r2_3 = colunaB[0] * colunaA2[1]
r3_3 = colunaC[0] * colunaA2[2]

r4_3 = colunaA[0] * colunaB2[0]
r5_3 = colunaB[0] * colunaB2[1]
r6_3 = colunaC[0] * colunaB2[2]

r7_3 = colunaA[1] * colunaA2[0]
r8_3 = colunaB[1] * colunaA2[1]
r9_3 = colunaC[1] * colunaA2[2]

r10_3 = colunaA[1] * colunaB2[0]
r11_3 = colunaB[1] * colunaB2[1]
r12_3 = colunaC[1] * colunaB2[2]



ra1 = r1_3 + r2_3 + r3_3
rb1 = r4_3 + r5_3 + r6_3
ra2 = r7_3 + r8_3 + r9_3
rb2 = r10_3 + r11_3 + r12_3


colunaA3.append(ra1)
colunaA3.append(ra2)
colunaB3.append(rb1)
colunaB3.append(rb2)


print("a multiplicação das matrizes indicadas resultará em: ")
print(ra1, rb1)
print(ra2, rb2)


print("obrigado por ter tido disposição suficiente para terminar meu codigo ;)")
