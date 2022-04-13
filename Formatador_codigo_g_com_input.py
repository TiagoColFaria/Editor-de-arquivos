# import fileinput
import fileinput

arquivo=str(input("Insira o nome do arquivo:"))
print(arquivo)
flag=True
i=0;


substituir=[]
substituto=[]

while flag:

    substituir.append(str(input("Insira o que deve ser substituido (considera espaços):"))) 
    substituto.append(str(input("Insira o substituto(considera espaços):")))
    i=i+1
    print (substituir)

    confirma=str(input("Deseja substituir mais alguma coisa? (digite 'sim' ou 's' para sim e qualquer outra tecla para não)"))
    if not(confirma=="sim" or confirma=="Sim" or confirma=="SIM" or confirma=="s" or confirma=="S"):
        flag=False

with fileinput.FileInput(arquivo, 
                             inplace = True, backup ='.txt') as f:
    # Using fileinput.input() method
    for line in f:

        k=0;
        while k!=i:
            if substituir[k] in line:
                line=line.replace( substituir[k],substituto[k])
            k=k+1

        print(line, end ='')

    confirma=str(input("operação finalizada, pressione enter para sair."))

#abcd
#1
#2
#*
#teste