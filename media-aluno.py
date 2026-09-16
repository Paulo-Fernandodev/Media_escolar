# MÉDIA DE NOTAS:

def calculo_media(numero_aluno):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3)/3
    media = round(media, 1)

    print (f"A média do aluno {numero_aluno} foi: {media}")

calculo_media (1)
calculo_media (2)
calculo_media (3)