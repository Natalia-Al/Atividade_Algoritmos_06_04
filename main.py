"""
Natalia Alves bernardo-UTF-8
"""

# Exercícios 
#a)Usuário digite seu nome completo for() imprima cada letra do nome 
nome=""
try:
  nome= input('Digite seu nome:')
  print()
  if nome.isalpha and len( str(nome))>=1:
      for letra in nome: 
          print('f A letra do nome digitado foi: {letra}')
except ValueError:
  print('Digite apenas caracteres')
finally: 
  pass

#b) Usuário digite o nome da disciplina e valores 
try:
  disciplina= input('Digite o nome da disciplina:')
  print()
  if disciplina.isalpha and len (str(disciplina))>=1:
    for indice_letra in enumerate(disciplina):
      if (indice_letra[0]%2) !=0:
        print(indice_letra)
except ValueError: 
  print('Digite apenas caracteres')
finally:
 pass

  #c) Usuário digita o nome curso respeintando maiusculas e minusculas e usando a função for() imprima apenas os valores que forem vogais 
try:  
  nome_curso= input ('Digite o nome do curso:')
  print()
  if nome_curso.isalpha and len(str(nome_curso))>0:

    for indice_letra in enumerate(nome_curso):
      
      if ((indice_letra[1].upper()))in'AEIOU':
        print(indice_letra[1].upper())

except ValueError:
  print('Digite apenas caracteres')
finally:
  pass 

#d) Digite cidade em que nasceu respeitando Maiúsculas e Minúsculas 
try:
  cidade_nasceu= input('Digite o nome da cidade onde nasceu:')
  print()
  if cidade_nasceu.isalpha and len(str(cidade_nasceu))>0:
    for indice_letra in enumerate(cidade_nasceu):
      if ((indice_letra[1].upper())) in 'BCDFGHJKLMNPQRSTXWZÇ':
        print (indice_letra[1].upper())
except ValueError:
  print('Digite apenas caracteres')
finally:
  pass

  
#e) Faça um script, usando o comando for que retorne os código ASC e na frente do código o respectivo caráter da tabela ASC, considerando que a tabela inicia em 0 (zero) e vai até 123).
import time 
for tabela in range(124):
  print(f' O código da tabela ASC é: (tabela)-e a letra correspondente é {chr(tabela)}')


#f) range(), onde o usuário digite o número de índices que ele deseja que apareça na tela. Após apresente os índices na do range na tela, e na última linha o total de índices mostrados na tela.
import time 
nr=0
for i in range (8):
  print(f'Indices:{i}')
  nr+=1
  time.sleep(0.005)
print(f'O total de indices mostrados na tela é: {nr}')



#g) Função range() usuário digite indice final que ira aparecer na tela, proxima linha apresente na tela os indices contidos no intervalo. ultima linha total de indices que contem o intervalo. atenção o numero do indice inicial não pode ser menor que zero. nem maior ou igual ao número do indice final.

try:
  nr=0
  indice_inicial = int(input('Digite o índice inicial:'))
  indice_final = int(input('Digite o índice final...:'))
  print()

  if indice_inicial <0 and indice_inicial==indice_final:
     print(f'Indice inicial:{indice_inicial} não pode ser menor que zero ou igual ao indice final:{indice_final}')
  elif indice_inicial<0:
    print(f'Indice inicial:{indice_inicial} não pode ser menor que 0')

  elif indice_final< indice_inicial:
     print(f'Indice final{indice_final} não pode ser maior que indice inicial:{indice_final}')
  else:
    for i in range(indice_inicial,indice_final):
     print(f'intervalo de índices {i}')
     nr+=1
  if nr>0:
    print(f' O total de índices nostrados na tela é:{nr}')
except ValueError:
   print('Digite apenas números inteiros...')
finally:
  pass

    
# H e I) Função range(), usuário digita o número do índice inicial e depois digite o número do indice final, índice inicial, com passos de 5 liste os indices na tela. próxima linha apresente o total de indices apresentados na tela, índice inicial não pode ser menor que zero nem maior ou igual ao numero do indice final, Cfritério verdadeiro apresentar mensagem, número do índice inicial não pode ser menor que zero ou maior ou igual ao indice final, programa encerrado. Deve ser apresentado no mínimo 4 elementos na tela: e critério verdadeiro apresentar mensagem = "quantidade de índices incompativel com os critérios pedidos no script":

try:
  nr=0
  indice_inicial = int(input('Digite o índice inicial:'))
  indice_final = int(input('Digite o indice final:'))

  print()
  if indice_inicial <0 and indice_inicial== indice_final:
    print (f'indice inicial:{indice_inicial} não pode ser 0 ou igual ao indice final:{indice_final}')

  elif indice_inicial <0:
    print (f' indice inicial:{indice_inicial} não pode ser menor que 0')

  elif indice_final<indice_inicial:
    print(f' indice final:{indice_final} não pode ser maior que indice incial:{indice_inicial}, programa encerrado')

  elif indice_inicial<indice_final:
    for i in range(indice_inicial,indice_final,5):
      print(f' intervalo de índices {i}')
      nr+=1
  if nr<=4:
    print(f' quantidade de índices incompatível com os critérios pedidos no script: pedidos=4, intervalo tem apenas:{nr}')
  else:
    print(f' O total de índices mostrados na tela é :{nr}')
except ValueError:
  print(f'Digite apenas números inteiros...')
finally:
  pass


# H e J) Função range(), usuário digita o número do índice inicial e depois digite o número do indice final, índice inicial, com passos de 5 liste os indices na tela. próxima linha apresente o total de indices apresentados na tela, índice inicial não pode ser menor que zero nem maior ou igual ao numero do indice final, Cfritério verdadeiro apresentar mensagem, número do índice inicial não pode ser menor que zero ou maior ou igual ao indice final, ignorar três valores definidos pelo usuário
  try:
    nr=0
    indice_inicial= int(input('Digite o índice inicial:'))
    indice_final = int(input('Digite o índice final:'))
    print()
    ignora_1 = int(input('Digite o 1° número a ser ignorado'))
    ignora_2 = int(input('Digite o 2° número a ser ignorado'))
    ignora_3 = int(input('Digite o 3° número a ser ignorado'))
    print()
    if indice_inicial<=0 and indice_inicial== indice_final:
      print(f'Indice inicial:{indice_inicial} não pode ser 0 ou igual ao indice final:{indice_final}')
    elif indice_inicial<0:
      print(f'Indice inicial:{indice_inicial}não pode ser menor que 0')
    elif indice_final<indice_final:
      print(f'Indice final:{indice_final}não pode ser maior que indice inicial:{indice_inicial}, programa encerrado')
    elif indice_inicial<indice_final:

      for i in range(indice_inicial,indice_final):
        if (i== ignora_1) or i == ignora_2 or i==ignora_3:
          pass
        else:
          print(f' Intervalo de indices{i}')
          nr=+1

      if nr<=4:
        print(f' quantidade de indices incompatível com os critérios pedidos no script: pedidos =4, intervalo tem apenas:{nr}')
      else:
        print(f'O total de indices mostrados na tela é:{nr}')
  except ValueError:
       print('Digite apenas números inteiros...')
  finally:
      pass


#k) aça um script que imprima a frase "estou em looping" e, em seguida, peça para o usuário digitar uma letra. Critérios: se a letra digitada for a ‘q’ finalize o script, senão, apresente na tela a mesma frase até que a letra ‘q’ seja enviada:
for i in range (100000000):
  print('Estou em looping...')
  letra = input('Digite a letra q para sair...')
  if letra.upper()== 'Q':
    print('programa encerrado...')
    break
    