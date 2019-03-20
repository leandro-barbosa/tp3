vet = []
vet2 = []
ativa = True
while ativa:
    frase = str(input('Digite a frase:'))
    if frase != 'sair':
        vet.append(frase)
    else:
        ativa = False
for i in range(len(vet)):
    if 'eu' in vet[i].split(' '):
        print(vet[i])