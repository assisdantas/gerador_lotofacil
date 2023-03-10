#   Gerador de jogos da lotofácil usando pesos estátisticos obtidos dos 2.707
#   resultados anteriores. Cada bola tem uma dezena com maior e menor probalidade
#   de ser sorteado, estas foram mapeadas e pesadas usando estátisca. Cada dezena
#   tem um peso específico que é levado em conta na hora da escolha pseudo-aleatória
#   para geração dos jogos. Para mais informações consulte: https://www.lotodicas.com.br/lotofacil/estatisticas
#
#   Resultados podem ser baixados em: https://asloterias.com.br/download-todos-resultados-lotofacil
#   Arquivo para processamento do resultado pode ser feito com PowerBI com modelo em: 
#   https://github.com/assisdantas/gerador_lotofacil
#
#

import random
import numpy as np
import time
import csv

# bolas do bilhete
fibonacci = [1, 2, 3, 5, 8, 13, 21]
bolas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
ult_concurso = []
jogos = []
jogo = []

# peso geral de cada dezena
pd_geral = {1: 0.594384927964536, 2: 0.594384927964536, 3: 0.606206132249723, 4: 0.601403768008866, 5: 0.607683782785371,
            6: 0.580716660509789, 7: 0.585888437384559, 8: 0.575914296268932, 9: 0.599926117473218, 10: 0.622829700775766,
            11: 0.618396749168822, 12: 0.598079054303657, 13: 0.613224972294052, 14: 0.609900258588844, 15: 0.594754340598448,
            16: 0.578869597340229, 17: 0.591799039527152, 18: 0.596231991134097, 19: 0.596970816401921, 20: 0.623568526043591,
            21: 0.5932766900628, 22: 0.598079054303657, 23: 0.586257850018471, 24: 0.610639083856668, 25: 0.615072035463613}

# pesos das dezenas nas respectivas bolas
pd_bola1 = [0.046915405, 0.036202438, 0.04063539, 0.041374215, 0.037310676, 
            0.034355375, 0.038788327, 0.038788327, 0.04063539, 0.044329516, 
            0.042482453, 0.03361655, 0.041743628, 0.038049501, 0.036202438,
            0.043221278, 0.029922423, 0.041374215, 0.038788327, 0.041743628, 
            0.042851866, 0.043590691, 0.04211304, 0.041004802, 0.043590691]

pd_bola2 = [0.043590691, 0.044329516, 0.043960103, 0.038788327, 0.032508312,
            0.040265977, 0.044698929, 0.037310676, 0.041374215, 0.038788327,
            0.040265977, 0.036202438, 0.038788327, 0.039157739, 0.04765423, 
            0.038788327, 0.035833025, 0.035463613, 0.042851866, 0.039527152, 
            0.039157739, 0.043590691, 0.037680089, 0.039527152, 0.039527152]

pd_bola3 = [0.040265977, 0.0350942, 0.039896564, 0.039527152, 0.043221278,
            0.033985962, 0.042482453, 0.035463613, 0.039527152, 0.043960103,
            0.044329516, 0.046545992, 0.045068341, 0.047284817, 0.038049501,
            0.038418914, 0.036941263, 0.040265977, 0.034724788, 0.041004802,
            0.041004802, 0.036941263, 0.036571851, 0.037680089, 0.041374215]

pd_bola4 = [0.038049501, 0.039157739, 0.038418914, 0.042851866, 0.04765423,
            0.036571851, 0.043590691, 0.036571851, 0.0350942, 0.036571851,
            0.037310676, 0.042851866, 0.043221278, 0.040265977, 0.039527152,
            0.039527152, 0.043590691, 0.0350942, 0.046915405, 0.039157739,
            0.036571851, 0.038788327, 0.036202438, 0.043960103, 0.04211304]

pd_bola5 = [0.036941263, 0.038788327, 0.04211304, 0.039527152, 0.045437754,
            0.046176579, 0.036941263, 0.044329516, 0.039527152, 0.035833025,
            0.041004802, 0.038049501, 0.04211304, 0.040265977, 0.038788327,
            0.041374215, 0.041743628, 0.034355375, 0.041004802, 0.041374215,
            0.035463613, 0.038049501, 0.037310676, 0.04063539, 0.042482453]

pd_bola6 = [0.039157739, 0.036571851, 0.041004802, 0.0350942, 0.04063539,
            0.037680089, 0.035463613, 0.037680089, 0.034355375, 0.037680089,
            0.044329516, 0.039527152, 0.039527152, 0.045437754, 0.042482453,
            0.034355375, 0.049870706, 0.040265977, 0.038788327, 0.041004802,
            0.039527152, 0.04211304, 0.036571851, 0.046545992, 0.043960103]

pd_bola7 = [0.04211304, 0.039527152, 0.045807167, 0.033247137, 0.039527152,
            0.038788327, 0.034355375, 0.036571851, 0.044698929, 0.033985962,
            0.040265977, 0.044698929, 0.043590691, 0.042851866, 0.035833025,
            0.043221278, 0.038049501, 0.043221278, 0.041004802, 0.043590691,
            0.036941263, 0.043590691, 0.039157739, 0.038049501, 0.036941263]

pd_bola8 = [0.037310676, 0.041004802, 0.04063539, 0.047284817, 0.041743628,
            0.035833025, 0.0350942, 0.038418914, 0.050609531, 0.042851866,
            0.04063539, 0.035833025, 0.046545992, 0.038049501, 0.038788327,
            0.042482453, 0.039527152, 0.036571851, 0.032508312, 0.043590691,
            0.042851866, 0.031400074, 0.041374215, 0.04211304, 0.036571851]

pd_bola9 = [0.043960103, 0.041374215, 0.030661249, 0.038788327, 0.036941263,
            0.043960103, 0.038418914, 0.038049501, 0.046545992, 0.04211304,
            0.049501293, 0.038418914, 0.041374215, 0.042482453, 0.041004802,
            0.028814185, 0.033985962, 0.038788327, 0.036202438, 0.052456594,
            0.041374215, 0.037680089, 0.030661249, 0.04211304, 0.043960103]

pd_bola10 = [0.038049501, 0.04765423, 0.045437754, 0.044698929, 0.037310676,
             0.036571851, 0.042482453, 0.0350942, 0.039896564, 0.041004802,
             0.038418914, 0.039896564, 0.039527152, 0.035833025, 0.034724788,
             0.040265977, 0.039157739, 0.036941263, 0.041374215, 0.045437754,
             0.041374215, 0.033985962, 0.039527152, 0.045437754, 0.039527152]

pd_bola11 = [0.036202438, 0.037680089, 0.037680089, 0.036202438, 0.036202438,
             0.046545992, 0.04063539, 0.038788327, 0.032877724, 0.041004802,
             0.036571851, 0.041374215, 0.040265977, 0.042851866, 0.045068341,
             0.036941263, 0.043590691, 0.037680089, 0.047284817, 0.044698929,
             0.032877724, 0.042851866, 0.040265977, 0.042482453, 0.041004802]

pd_bola12 = [0.040265977, 0.037680089, 0.039157739, 0.043590691, 0.04211304,
             0.037680089, 0.0350942, 0.041743628, 0.041004802, 0.041004802,
             0.042851866, 0.04211304, 0.032508312, 0.036571851, 0.041743628,
             0.04211304, 0.039896564, 0.040265977, 0.039527152, 0.038788327,
             0.042851866, 0.039527152, 0.038788327, 0.041743628, 0.041004802]

pd_bola13 = [0.037680089, 0.034724788, 0.04063539, 0.045807167, 0.045068341,
             0.036941263, 0.039896564, 0.038788327, 0.04063539, 0.043960103,
             0.038788327, 0.034724788, 0.041743628, 0.04765423, 0.036941263,
             0.035833025, 0.039527152, 0.048023642, 0.037680089, 0.038049501,
             0.036202438, 0.039527152, 0.040265977, 0.035463613, 0.045068341]

pd_bola14 = [0.039157739, 0.042482453, 0.037310676, 0.0350942, 0.043221278,
             0.039157739, 0.038418914, 0.04063539, 0.03361655, 0.050978943,
             0.04063539, 0.041743628, 0.040265977, 0.038418914, 0.043960103,
             0.040265977, 0.044698929, 0.043960103, 0.036202438, 0.032508312,
             0.039527152, 0.043221278, 0.042851866, 0.036571851, 0.034724788]

pd_bola15 = [0.048762468, 0.046915405, 0.044698929, 0.043960103, 0.043221278,
             0.043221278, 0.042851866, 0.042482453, 0.04211304, 0.04211304,
             0.041004802, 0.04063539, 0.039527152, 0.039527152, 0.039527152,
             0.038788327, 0.037680089, 0.037310676, 0.036941263, 0.036202438,
             0.035463613, 0.034724788, 0.034724788, 0.033985962, 0.033247137]

j = 1
b = 1
mult = 0
primos = 0
novo = True
lista = []
tentativa = 1
dez_ant = 0
dez_ants = []
dez_antsp = []
total_tenta = 0
pesos = ("pd_bola%s" %b)

num_jogos = int(input("Quantos jogos você quer gerar? "))

usar_ant = (input("Deseja utilizar o concurso anteior [s: sim, n: não]? "))
while (usar_ant != "s") and (usar_ant != "n"):
    usar_ant = (input("Deseja utilizar o concurso anteior [s: sim, n: não]? "))

if (usar_ant == "s"):

    lista = input("Entre com o último resultado (separe as dezenas por vírgula sem espaços): ")
    u_res = lista.split(',')
    while(len(u_res) < 14):
        lista = input("Entre com o último resultado (separe as dezenas por vírgula sem espaços): ")
        u_res = lista.split(',')

    dez_ant = int(input("Quantas dezenas deste último concurso deseja utilizar [Entre 6~12, melhor 7~11]? "))
    while (dez_ant < 7) or (dez_ant > 11):
        dez_ant = int(input("Quantas dezenas deste último concurso deseja utilizar [Entre 6~12, melhor 7~11]? "))
else:
    dez_ant = 0

qtd_bolas = int(input("Quantas dezenas por jogo [15 até 16]? "))
while (qtd_bolas < 15) or (qtd_bolas > 16):
    qtd_bolas = int(input("Quantas dezenas por jogo [15 até 16]? "))

qtd_sorte = int(input("Número de dezenas por escolha [Melhor 10~20]: "))
while (qtd_sorte < 10) or (qtd_bolas > 20):
    qtd_sorte = int(input("Número de dezenas por escolha [Melhor 10~20]: "))
    
def conta_pares(jogo):
    pares = 0
    impar = 0
    
    for num in jogo:
        if(num % 2) == 0:
            pares += 1
        else:
            impar += 1
    
    return pares, impar        

inicio = time.time()

while (j <= num_jogos) or (novo == True):
    
    if (dez_ant > 0):
        
        for da in u_res:
            dez_antsp.append(pd_geral[int(da)])
    
    while (len(dez_ants) < dez_ant):    
        
        mdez_ants = random.choices(u_res, weights=dez_antsp, k=dez_ant)
        mdez_ant = np.random.choice(mdez_ants)
        
        if (mdez_ant not in dez_ants):
            dez_ants.append(mdez_ant)
        
    jogo.extend(list(map(int, dez_ants)))
           
    while (len(jogo) < qtd_bolas):
        
        bolas_melhores = random.choices(bolas, weights=globals()[pesos], k=qtd_sorte)
        bola = np.random.choice(bolas_melhores)
        
        if (bola not in jogo):
            jogo.append(bola)
            b += 1
            if (b == 16):
                b = 1
            pesos = ("pd_bola%s" %b)

        n = jogo[-1]
        
        for count in range(2, n):
            if (n % count == 0):
                mult += 1
                
        if (mult == 0):
            primos += 1
            
        jogo_fib = len(set(jogo) & set(fibonacci))
        media = (sum(jogo) / qtd_bolas)
    
    if (jogo not in jogos) and (primos >= 3 and primos <= 6) and (sum(jogo) >= 166 and sum(jogo) <= 227) and (jogo_fib >= 2 and jogo_fib <= 5) and (media >= 13 and media <= 15):
        print("")
        print("===========================================================================")
        print("Jogo %s: " %j, sorted(jogo))
        print("===========================================================================")
        print("Estátisticas:")
        print("---------------------------------------------------------------------------")
        print("Passos necessários:", tentativa)
        print("Primos: %s [i] Melhor entre 3 e 6" %primos)
        print("Soma:", sum(jogo), "[i] Melhor entre 166 e 227")
        print("Fibbonacci:", jogo_fib, "[i] Melhor entre 2 e 5")
        print("Média:", media, "[i] Melhor entre 13 e 15") 
        print("Pares/Ímpares:", conta_pares(jogo), "[i] Melhor 6~9/9~6")
        print("Dezenas utilizadas do resultado anteior %s:" %dez_ant, dez_ants)       
        
        j += 1
        jogos.append(sorted(jogo))
        jogo = []
        dez_antsp = []
        bolas_melhores = []
        mdez_ants = []
        dez_ants = []
        b = 1
        primos = 0
        mult = 0
        total_tenta = total_tenta + tentativa
        tentativa = 0
        pesos = ("pd_bola%s" %b)
        novo = False
    else:
        novo = True
        # print('''\033[K Tentativa %s para gerar o jogo %s. Jogo: %s''' %(tentativa, j, jogo), end="\r")
        tentativa += 1
        jogo = []
        dez_antsp = []
        bolas_melhores = []
        mdez_ants = []
        dez_ants = []
        b = 1
        primos = 0
        mult = 0
        pesos = ("pd_bola%s" %b)

fim = time.time()        

with open('jogos.csv', 'w', newline='') as jogos_csv:
    escritor = csv.writer(jogos_csv)
    escritor.writerows(jogos)

print('''
      Salvo no arquivo 'jogos.csv'. Verifique diretório.''')

tempo_total = (fim - inicio)

print('''
      Gerado(s) %i jogos com %i dezenas em um total de %i passos em %.2f segundos.''' %(num_jogos, qtd_bolas, total_tenta, tempo_total))
