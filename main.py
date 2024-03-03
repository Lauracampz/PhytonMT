import json
import sys
import os


#class Transicao:
 #   def getSimbolosIni(self, numFitas, conjTransicoes):






class MaquinaT:
    def __init__(self, num_fitas, num_estados, alfa_entrada, alfa_fita, inicio_fita, branco, func_transition,
                 estado_inicial, estados_finais, palavra):
        # Inicialização das informações da Máquina de Turing
        self.num_fitas = num_fitas
        self.num_estados = num_estados
        self.alfa_entrada = alfa_entrada
        self.alfa_fita = alfa_fita
        self.inicio_fita = inicio_fita
        self.branco = branco
        self.func_transition = func_transition
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

        self.estado_atual = estado_inicial

        self.fitas = [[inicio_fita] + list(palavra)] + [[inicio_fita] + ['_'] * len(palavra) for _ in range(num_fitas-1)]
        # Posições iniciais das cabeças de leitura em cada fita
        self.cabecas_leitura = [1] * num_fitas
        print(f"Cabeças de leitura: {self.cabecas_leitura}")
        for i, fita in enumerate(self.fitas):
            print(f"Fita {i + 1}: {''.join(fita)}")

        while self.estado_atual not in self.estados_finais:
            # Obtenha os símbolos na posição atual das cabeças de leitura em cada fita
            for i in range(self.num_fitas):
                print(f"Index {i}: cabecas_leitura={(self.cabecas_leitura[i])}, fitas[i] length={len(self.fitas[i])}")

            symbols = [self.fitas[d][self.cabecas_leitura[d]] for d in range(self.num_fitas)]
            print(f"Símbolos lidos: {symbols}")

            # Verifica a transição com base nos símbolos e no estado atual
            transicao = None

            for t in self.func_transition:
                aux=num_fitas
                estado_atual_transicao = t[0]

                simbolos_transicao = [lista[0] for lista in t[2]]
                simbolos_escrito = [lista[1] for lista in t[2]]
                simbolos_direcao = [lista[2] for lista in t[2]]

               # print(f"Símbolos escrito: {simbolos_escrito}")
                #print(f"Direcao: {simbolos_direcao}")
                print(f"Estado transicao: {estado_atual_transicao}")
                print(f"Estado atual: {self.estado_atual}")
                print(f"simbolos_transicao: {simbolos_transicao}")
                print(f"simbolos: {symbols}")
                # print(f"Símbolos lidos: {simbolos_transicao}")
                if estado_atual_transicao == self.estado_atual and simbolos_transicao == [self.fitas[d][self.cabecas_leitura[d]] for d in range(self.num_fitas)]:

                    transicao = t
                    break
                print(f"transicao: {transicao}")

            if transicao is not None:
                # Se encontrarmos uma transição correspondente, 'transicao' conterá as informações necessárias

                for i in range(self.num_fitas):
                    novos_simbolos = transicao[2][i][1]
                    direcao_movimento = transicao[2][i][2]

                    # Atualiza os símbolos na fita
                    self.fitas[i][self.cabecas_leitura[i]] = novos_simbolos
                    for j, fita in enumerate(self.fitas):
                        print(f"Fita {j + 1}: {''.join(fita)}")

                    # Move a cabeça de leitura na fita
                    if direcao_movimento == '>' :
                        self.cabecas_leitura[i] += 1
                    elif direcao_movimento == '<'and self.cabecas_leitura[i] > 1:
                        self.cabecas_leitura[i] -= 1
                print(f"Cabeças de leitura: {self.cabecas_leitura}")
                # Atualiza o estado atual
                self.estado_atual = transicao[1]

                # Mostre o estado atual das fitas
                for i, fita in enumerate(self.fitas):
                    print(f"Fita {i + 1}: {''.join(fita)}")

                # Mostre o estado atual da máquina de Turing
                print(f"Estado atual: {self.estado_atual}")

            else:
                # Se não encontrarmos uma transição correspondente, 'transicao' será None
                print("Transição indefinida. A máquina parou.")
                break






# Leitura de Entrada
nome_json = input("Digite o nome do arquivo JSON: ")

# Verificar se o arquivo existe
if not os.path.exists(nome_json):
    print("Arquivo não encontrado.")
    sys.exit()

# Ler arquivo JSON incluso na pasta do projeto
with open(nome_json, 'r') as arquivo:
    dic = json.load(arquivo)

# Inicialização da Máquina de Turing
numFitas = dic["mt"][0]
numEstados = dic["mt"][1]
alfaEntrada = dic["mt"][2]
alfaFita = dic["mt"][3]
inicioFita = dic["mt"][4]
branco = dic["mt"][5]
funcTransition = dic["mt"][6]
estadoInicial = dic["mt"][7]
estadosFinais = dic["mt"][8]

print("Número de Fitas:", numFitas)
print("Número de Estados:", numEstados)
print("Alfabeto de Entrada:", alfaEntrada)
print("Alfabeto da Fita:", alfaFita)
print("Configuração Inicial da Fita:", inicioFita)
print("Símbolo em Branco:", branco)
print("Funções de Transição:", funcTransition)
print("Estado Inicial:", estadoInicial)
print("Estados Finais:", estadosFinais)
print("Exemplos :", funcTransition[6][2][0][2] )

mt = MaquinaT(numFitas, numEstados, alfaEntrada, alfaFita, inicioFita, branco, funcTransition, estadoInicial, estadosFinais, "001100001")

# Execução da Máquina de Turing
#mt.run()

# Verificação do Estado Final
#if result:
 #   print("Sim")
#else:
 #   print("Não")
