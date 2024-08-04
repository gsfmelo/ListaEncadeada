class Pacientes:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

    def __repr__(self):
        return f"Pacientes({self.cor}, {self.numero})"


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
        cor = input("Informe a cor do cartão (A/V): ").strip().upper()
        numero = int(input("Informe o número do cartão: ").strip())
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
        print("\nLista de Espera:")
        print("Cor  | Número")
        print("---- | ------")
        nodo_atual = self.head
        while nodo_atual:
            print(f" {nodo_atual.cor}   | {nodo_atual.numero}")
            nodo_atual = nodo_atual.proximo

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
        else:
            paciente_atendido = self.head
            self.head = self.head.proximo
            print(f"Atendendo o paciente com cartão cor {paciente_atendido.cor} e número {paciente_atendido.numero}")


def menu():
    programa = ListaDePacientes()
    while True:
        print('\nMenu:')
        print('1 - Adicionar paciente à fila')
        print('2 - Mostrar pacientes na fila')
        print('3 - Chamar paciente')
        print('4 - Sair')

        op = input("Escolha uma opção: ").strip()
        if op == '1':
            programa.inserir()
        elif op == '2':
            programa.imprimirListaEspera()
        elif op == '3':
            programa.atenderPaciente()
        elif op == '4':
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida, tente novamente.")


# Chamando o menu para iniciar o programa
menu()
