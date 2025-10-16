NOME="Rodrigo Guimaraes Pereira Rodrigues"
RA="0220482523012"
NOME_SOCIAL="Dido Rodrigues"
print(f"Nome : {NOME} ")
print(f"RA: {RA} ")
print(f"Nome Social: {NOME_SOCIAL} ")

pdc=int(input("Qual o custo para fabricacao desse produto? "))
pdv=int(input("Por quanto esse produto é vendido? "))
la=pdv-pdc
md1=(la/pdc)*100

if md1>=10 and md1 <= 30:
    print("Margem Satisfatoria. ")
elif md1<10:
    print("Margem Baixa: Avaliar preco de venda! ")
else:
    print("Margem Exelente!" )