# Classe de criação dos elementos da lista  - Trabalho de Geovanna Melo
class Pacientes:

    def __init__(self, cor, numero):
       self.cor = cor
       self.numero = numero
       self.proximo = None

    def __repr__(self):
        return f"Pacientes({self.cor},{self.numero})"

# CLasse de criação de lista encadeada simples
class ListaDePacientes:
    def __init__(self):
        self.head = None

    def inserirComPrioridade(self, nodo):
        if not self.head:
            self.head = nodo

        else:
            nodo_atual = self.head
            anterior = None
            while nodo_atual and nodo_atual.cor == 'A':
                anterior = nodo_atual
                nodo_atual = nodo_atual.proximo

            if not anterior:
                nodo.proximo = self.head
                self.head = nodo

            else:
                nodo.proximo = nodo_atual
                anterior.proximo = nodo

    def inserirSemPrioridade(self, nodo):

        if not self.head:
            self.head = nodo

        else:
            nodo_atual = self.head
            while nodo_atual.proximo:
                nodo_atual = nodo_atual.proximo

            nodo_atual.proximo = nodo
    def inserir(self):

        cor = input("Informe a cor do cartão (A/V):")
        numero = int(input("Informe o número do cartão:"))
        nodo = Pacientes(cor, numero)

        if not self.head:
            self.head = nodo

        elif cor == 'V':
            self.inserirSemPrioridade(nodo)

        elif cor == 'A':
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):

        if not self.head:
            print("Nenhum paciente na fila.")
            return

        lista_pacientes = []
        nodo_atual = self.head

        while nodo_atual:
            lista_pacientes.append(f"[{nodo_atual.cor},{nodo_atual.numero}]")
            nodo_atual = nodo_atual.proximo
        print("Lista ->" + ",".join(lista_pacientes))

    def atenderPaciente(self):

        if not self.head:
            print("Nenhum paciente na fila.")

        else:
            paciente_atendido = self.head
            self.head = self.head.proximo
            print(f"Atendendo o paciente cartão cor {paciente_atendido.cor} e número {paciente_atendido.numero}")

# Chama o programa principal
Programa = ListaDePacientes()

while True:
    print('Menu:')
    print('1 - Adicionar paciente a fila')
    print('2 - Mostrar pacientes na fila')
    print('3 - Chamar paciente')
    print('4 - Sair')

# Lê as opções digitadas pelo usuario
    op = int(input("Escolha uma opção:"))

    if op == 1:
        Programa.inserir()

    elif op == 2:
        Programa.imprimirListaEspera()

    elif op == 3:
        Programa.atenderPaciente()

    elif op == 4:
        print("Encerrando programa.")
        break

    else:
        print("Opção inválida, tente novamente.")

