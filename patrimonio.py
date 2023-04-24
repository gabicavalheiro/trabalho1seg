import os
instrumento = []
marca = []
valor = []


def carregar_dados_do_arquivo():
  if not os.path.isfile("instrumentos.csv"):
    return
  
  with open("instrumentos.csv", "r") as arq:
    linhas = arq.readlines()

    for linha in linhas:
      partes = linha.split(";")
      instrumento.append(partes[0])
      marca.append(partes[1])
      valor.append(float(partes[2][0:-1]))    

def salvar_dados_no_arquivo():
  with open("instrumentos.csv", "w") as arq:
    
  
    for (instrumentos, marcas, valores) in zip(instrumento, marca, valor):
      arq.write(f"{instrumentos};{marcas};{valores}\n")



def titulo(texto, sublinhado="-"):
  print()
  print(texto)
  print(sublinhado*40)

def incluir():
  titulo("Incluir instrumento")
  instrumentos = input("Desc do Instrumento: ") 
  marcas = input("Marca: ")
  valores = float(input("Valor em R$: "))

  instrumento.append(instrumentos)
  marca.append(marcas)
  valor.append(valores)  
  print("Ok! Instrumento Cadastrado")

  
def listar():
  titulo("Lista de instrumentos")
  print("Nº Nome do instrumento....... Marca Valor.....")
  for x, (instrumentos, marcas, valores) in enumerate(zip(instrumento, marca, valor), start=1):
    print(f"{x:2} {instrumentos:20}  {marcas:3}  {valores}")

def pesquisar():
  titulo("Pesquisa por marca")

  pesq = input("Marca: ")

  print("Nº Nome do instrumento....... Marca Valor.....")
  
  for x, (instrumentos, marcas, valores) in enumerate(zip(instrumento, marca, valor), start=1):
    if pesq.upper() in marcas.upper():
      print(f"{x:2} {instrumentos:20}  {marcas:3}  {valores}")


def excluir():
  listar() 

  titulo("Exclusão de instrumento")
  num = int(input("Nº do instrumento a Excluir: "))

  if num <= 0 or num > len(instrumento):
    print("Número inválido")
    return
  
  instrumento.pop(num-1)
  marca.pop(num-1)
  valor.pop(num-1)

# def totalizacao():
#   titulo("Pesquisa por instrumento")

#   pesq = input("Instrumento: ")

# #   print("Nº Nome do instrumento....... Marca Valor.....")
  
#   for x, (instrumentos, marcas, valores) in enumerate(zip(instrumento, marca, valor), start=1):
#     if pesq.upper() in instrumentos.upper():
#       print(f"{x:2} {instrumentos:20}  {marcas:3}  {valores}")
#       num = len(instrumento)
#       total = sum(valor)

#       print(f"Nº de instrumentos: {num}")
#       print(f"Valor total dos instrumentos R$: {total:9.2f}")
  
def totalizacao():
  descricao = input("Digite a descrição do instrumento: ")
  if descricao in instrumento:
    total_descricao = instrumento[instrumento]["preco"]
    total_outros = sum([dados["preco"] for dsc, dados in instrumento.items() if dsc != descricao])
    print(f"{descricao} - Total: R${total_descricao:.2f}")
    print(f"Outros instrumentos - Total: R${total_outros:.2f}")
  else:
    print("Instrumento não encontrado")

  

carregar_dados_do_arquivo()

while True:
  titulo("Cadastro de instrumentos musicais", "=")
  print("1. Incluir instrumento")
  print("2. Listar instrumentos")
  print("3. Pesquisar por marca do instrumento")
  print("4. Excluir instrumento (por número)")
  print("5. Pesquisa com totalização")
  print("6. Finalizar")
  opcao = int(input("Opção: "))  
  if opcao == 1:
    incluir()
  elif opcao == 2:
    listar()
  elif opcao == 3:
    pesquisar()
  elif opcao == 4:
    excluir()
  elif opcao == 5:
    totalizacao()
  else:
   
    salvar_dados_no_arquivo()
    break