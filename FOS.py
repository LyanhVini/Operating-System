import random
from re import A
import threading as th 
    
class fifo:
    
    # INICIANDO AS VARIÁVEIS:

    def __init__(self, processos, sort):

        self.processos = processos
        self.sort = sort

    def exe_f():
        
        print("\nESCALONADOR FIFO EXECUTANDO: \n")

        t_exit = [] # Armeza o tempo de saída dos processos
        t_tot = []  # tempo total é a subtração do tempo de saída menos o tempo de chegada
        t_wait = [] # tempo de espera é a diferença entre o tempo de execução e o tempo de retorno dos processos.

        print(sort)
        
        for i in range(len(sort)):
        
            if(i==0): 
                t_exit.append(sort[i][1][1])
            else:
                t_exit.append(t_exit[i-1] + sort[i][1][1])
   
        for i in range(len(sort)):
            t_tot.append(t_exit[i] - sort[i][1][0]) 
    
        for i in range(len(sort)): # calcula o tempo de espera
            t_wait.append(t_tot[i] - sort[i][1][1])
 
        # CALCULAR TEMPO MÉDIO DE ESPERA

        avg_wt = 0
        for i in t_wait:
            avg_wt = i + avg_wt

        avg_wt = (avg_wt/len(sort))

        # CALCULAR TEMPO MÉDIO DE RETORNO

        avg_turn_round = 0
        for i in t_tot:
            avg_turn_round = i + avg_turn_round

        avg_turn_round = (avg_turn_round/len(sort))
 
        # Printando o resultado dos valores:

        print("Processo | Tempo de chegada* | Tempo de execução* | Tempo de saida | Tempo de retorno | Tempo de espera |")
    
        for i in range(len(sort)):
            print(" ",sort[i][0],"      |        ",sort[i][1][0],"   |           ",sort[i][1][1]," |          ",t_exit[i],"  |          ",t_tot[i],"  |        ",abs(t_wait[i]),"   |     ")
    
        print("Tempo médio de espera: ", abs(avg_wt))
        print("Tempo médio de retorno: ", abs(avg_turn_round))

   
class sjf:
    
    def __init__(self, processos, list_sjf):
        
        self.list_sjf = list_sjf
        self.processos = processos
        
    def t_waiting(list_sjf, n, wt): 
        rt = [0] * n
        for i in range(n): 
            rt[i] = list_sjf[i][1]

        complete = 0
        t = 0
        minm = 999999999
        short = 0
        check = False
        
        while (complete != n):
            for j in range(n):
                if ((list_sjf[j][2] <= t) and 
                    (rt[j] < minm) and rt[j] > 0):
                    minm = rt[j]
                    short = j
                    check = True
            if (check == False):
                t += 1
                continue
              
            rt[short] -= 1
  
            minm = rt[short] 
            if (minm == 0): 
                minm = 999999999
  
            if (rt[short] == 0): 

                complete += 1
                check = False
                fint = t + 1
                wt[short] = (fint - list_sjf[short][1] -    
                                list_sjf[short][2])
  
                if (wt[short] < 0):
                    wt[short] = 0

            t += 1

    def t_retorno(list_sjf, n, wt, tat): 
 
        for i in range(n):
            tat[i] = list_sjf[i][1] + wt[i] 

    def t_medio(self, list_sjf, n): 

        wt = [0] * n
        tat = [0] * n
  
        self.t_waiting(list_sjf, n, wt) 
   
        self.t_retorno(list_sjf, n, wt, tat) 

        print("Processes    Tempo de execução     WEspera", 
                    "Time     Tempo de retorno")
        total_wt = 0
        total_tat = 0
        for i in range(n):
  
            total_wt = total_wt + wt[i] 
            total_tat = total_tat + tat[i] 
            print(" ", list_sjf[i][0], "\t\t", 
                        list_sjf[i][1], "\t\t", 
                        wt[i], "\t\t", tat[i])
  
        print("\nTempo médio de espera = %.5f "%(total_wt /n) )
        print("Tempo médio de retorno = ", total_tat / n) 
        

class sorteio:

    def __init__(self, processos, sort):

        self.processos = processos
        self.sort = sort
        n = 3

    def exe_s():

        print("\nESCALONADOR SORTEIO EXECUTANDO: \n")
        
        t_exit = [] # Armeza o tempo de saída dos processos
        t_tot = []  # tempo total é a subtração do tempo de saída menos o tempo de chegada
        t_wait = [] # tempo de espera é a diferença entre o tempo de execução e o tempo de retorno dos processos.
        
        # ERROr: IMPLEMENTAR UMA ESTRUTURA QUE ESCOLHA ALEATORIAMENTE UMA CHAVE DO DICIONÁRIO sort.
        
        l = []
        for i in range(len(sort)):
    
            id = random.choice(list(d.items()))
            a = id[0]
            l.append(a)
            
        print(l)
        
        for i in l:

            for i in range(len(sort)):

                if(i==0): 
                
                    t_exit.append(sort[i][1][1])
                    
                else:
                    
                    t_exit.append(t_exit[i-1] + sort[i][1][1])

            for i in range(len(sort)):

                t_tot.append(t_exit[i] - sort[i][1][0]) 

            for i in range(len(sort)):

                t_wait.append(t_tot[i] - sort[i][1][1])
 
        # CALCULAR TEMPO MÉDIO DE ESPERA

        avg_wt = 0
        for i in t_wait:
            avg_wt = i + avg_wt

        avg_wt = (avg_wt/len(sort))

        # CALCULAR TEMPO MÉDIO DE RETORNO

        avg_turn_round = 0
        for i in t_tot:
            avg_turn_round = i + avg_turn_round

        avg_turn_round = (avg_turn_round/len(sort))
 
        # Printando o resultado dos valores:

        print("Processo | Tempo de chegada* | Tempo de execução* | Tempo de saida | Tempo de retorno | Tempo de espera |")
    
        for i in range(len(sort)):
            
            print(" ",sort[i][0],"        |       ",sort[i][1][0],"     |           ",sort[i][1][1],"   |          ",t_exit[i],"  |          ",t_tot[i],"  |        ",abs(t_wait[i]),"   |     ")
   
        print("Tempo médio de espera: ", abs(avg_wt))
        print("Tempo médio de retorno: ", abs(avg_turn_round))

class RR():

    def __init__(self, processos, sort):

        self.processos = processos
        self.sort = sort
        self.n = len(sort)
    # tempo que precisa processar - time
    # tempo de execução - exe
    # tempo de espera - t_wait
    # armazena o tempo total de execução dos processos - tot_bt
        def t_waiting(processos, n, exe,
                         t_wait, time):

        tot_bt = [0] * n
 
        # armazena o tempo total de execução dos processos em rem_bt

        for i in range(n):
            tot_bt[i] = exe[i]

        t = 0 # tempo contando
        while(1):
            done = True
            # Realiza em tdos os processos    
            for i in range(n):        

                if (tot_bt[i] > 0) :
                    done = False
                 
                    if (tot_bt[i] > time) :
                 
                        #Aumente o valor de t, ou seja, mostra
                        # quanto tempo um processo foi processado
                        t += time
                        # Diminua o burst_time do processo 
                        # atual por quantum
                        tot_bt[i] -= time
                 
                    # Se o tempo de execução for menor ou igual ao quantum. 
                    # Último ciclo para este processo
                    else:         
                        # Increase the value of t i.e. shows
                        # how much time a process has been processed
                        t = t + tot_bt[i]
 
                        #tempo de espera é o tempo atual menos o 
                        # tempo usado por este processo
                        t_wait[i] = t - exe[i]
                        # À medida que o processo é totalmente 
                        # executado, faça seu tempo de rajada restante = 0
                        tot_bt[i] = 0
            if (done == True):
                break
    def t_retorno(processos, n, exe, t_wait, t_tot):
        for i in range(n):
            t_tot[i] = exe[i] + t_wait[i]
        
    def exe_rr(self, processos, n, exe, time):
        
        t_wait = [0] * n
        tot = [0] * n
 
        self.t_waiting(processos, n, exe,
                         t_wait, time)
 
        self.t_retorno(processos, n, exe,
                                t_wait, self.t_tot)
        print("Processes    Burst Time     Waiting",
                     "Time    Turn-Around Time")
        total_wait = 0
        total_tot = 0
        for i in range(n):
 
            total_wait = total_wait + t_wait[i]
            total_tot = total_tot + tot[i]
            print(" ", i + 1, "\t\t", exe[i],
            "\t\t", t_wait[i], "\t\t", tot[i])
 
        print("\nAverage waiting time = %.5f "%(total_wait /n) )
        print("Average turn around time = %.5f "% (total_tot / n))

#######################################################################################################################

# CODIGO MAIN:
# Iniciando as variáveis:
processos = [1, 2, 3, 4]

sort = dict() # Vai armazenar junto a processo referente e sua tempo de chegada e de execução
burst = [] 
arrival = []
list_sjf = []
p1 = []
p2 = []
p3 = []

for i in range(len(processos)):
        
    # Fazer um dicionário em que a chave é o processo e os valores são o tempo de entrada e de saída
     
    arr = int(input("Digite o tempo de chegada do processo "+ str(i + 1)+ ": "))
    exe = int(input("Digite o tempo de execução "+ str(i + 1)+ ": "))
    key = int(i+1) # id de cada processo
    a = [] # Armazena os tempo de chegada e de execução
    arrival.append(arr)
    burst.append(exe)

    a.append(arr)
    a.append(exe)
    sort[key] = a

lista = processos + burst + arrival
x = lista[0], lista[3], lista[6]
p1 = list(x)
y = lista[1], lista[4], lista[7]
p2 = list(y)
z = lista[2], lista[5], lista[8]
p3 = list(z)
u = lista[9], lista[10], lista[11]
p4 = list(u)

aux = p1, p2, p3, p4
list_sjf = list(aux)


print("\nLista do tempos de execução: ", burst)
print("Lista dos tempos de chegada: ", arrival)
print("Lista: ", list_sjf)


d = dict(sorted(sort.items(), key=lambda item: item[1][0])) # dicionário contendo a chave o id do processo e como valores o tempo de chegada e execução
sort = sorted(sort.items(), key=lambda item: item[1][0]) # lista contendo a chave o id do processo e como valores o tempo de chegada e execução

print("\nDicionários dos programas -> ", d)

# Organizar os vetores

print("\n RESULTADOS: \n")

print("==================================================")
print("Buffer dos processos: ", sort) 
print("Número de processos: ", len(sort))
print("==================================================")
        
# EXECUTANDO FIFO.....
scho1 = fifo
scho1(processos, sort)
scho1.exe_f()

# EXECUTANDO SORTEIO.....
scho2 = sorteio
scho2(processos, sort)
scho2.exe_s()

# EXECUTANDO RR....

n1 = len(sort)
time = 2
scho3 = RR(processos, sort)
scho3(processos, sort)
scho3.exe_rr(processos, n, exe, time)
scho3()

# EXECUTANDO SJF...

scho4 = sjf
scho4(processos, list_sjf)
scho4.t_medio(list_sjf, n) #findavgTime
scho4()
