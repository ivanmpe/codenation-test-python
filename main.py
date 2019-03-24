from datetime import datetime
import csv
# coding: utf-8
# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.
#

def readCSV():
    with open('data.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            line_count +=1
            rows.append(row)        
        print('Processado {} linhas.' .format(line_count))
        
    del rows[0]
    return rows

def days(birth):

    d2 = datetime.today().strftime('%Y-%m-%d')
    d2 = datetime.strptime(d2,'%Y-%m-%d')
    
    d1 = datetime.strptime(birth, '%Y-%m-%d')
    days = abs((d2 - d1).days)
    return days


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
    
    data = readCSV()
    nationalities_dif = []
    for i in data:
        nationalities_dif.append(i[14])
        
    print("Existem {} nacionalidades diferentes. " .format(len(set(nationalities_dif))))
    print(sorted(set(nationalities_dif)))
    
    return len(set(nationalities_dif))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    data = readCSV()
    clubs_dif = []
    for i in data:
        clubs_dif.append(i[3])

    print("Existem {} clubes diferentes. " .format(len(set(clubs_dif))))
    print(sorted(set(clubs_dif)))
    return len(clubs_dif)

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    data = readCSV()
    twenty_players = []
    count = 1
    for i in data:
        if count <= 20:
            twenty_players.append(i[2])
            count+=1
        else:
            break
    print("Esses são os 20 primeiros jogadores: ")
    count=1
    for i in twenty_players:
        print("{} : {}" .format(count, i))
        count+=1
    return twenty_players
   

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    data = readCSV()
    eur_wages = []
    for i in data:
        eur_wages.append(float(i[17]))
    
    ten_eur_wages = sorted(eur_wages, reverse=True)
    del(ten_eur_wages[10:len(ten_eur_wages)])    
    players = []
    for i in data:
        if float(i[17]) in ten_eur_wages:
           print("O {} é um jogadores que ganham mais dinheiro da lista com {} euros . " .format(i[2],i[17] )) 
           players.append(str(i[2]))
    
    return players 

   

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    data = readCSV()
    count_days = []
    for i in data:
        count_days.append(days(i[8]))
                
    ten_old = sorted(count_days , reverse=True)
    print("Os 10 mais velhos tem esses dias: ")
    for i in range(0,10):
        print("{} : {} dias. " .format(i, ten_old[i]))
    
    del(ten_old[10:len(ten_old)])    
    
    players = []
    for i in data:
        if days(i[8]) in ten_old:
           print("O {} é um dos mais velhos da lista com {} dias. " .format(i[2], days(i[8]))) 
           players.append(str(i[2]))
        
    return players

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    
    data = readCSV()
    count_ages = []
    for i in data:
        count_ages.append(i[6])
                
    maxAge = max(count_ages, key=int)
    minAge = min(count_ages, key=int)
    print("Idade maxima : {} , Idade minima: {} " .format(maxAge, minAge))
    dictionary_ages = {}    
    print
    for i in range(int(minAge), int(maxAge)+1):
        
        dictionary_ages[i] = count_ages.count(str(i))
    
    print(dictionary_ages)
        
    return dictionary_ages
