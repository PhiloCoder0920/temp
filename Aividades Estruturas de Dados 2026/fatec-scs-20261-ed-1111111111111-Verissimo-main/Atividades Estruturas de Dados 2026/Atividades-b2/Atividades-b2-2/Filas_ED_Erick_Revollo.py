"""
*********************************************************
*               Fatec Sâo Caetano do Sul
*                   Atividade B2-2
*           Autor: Erick Joshua Revollo
*                   RA: 1681432612008
*      Objetivo: Aprender a manipular filas em python
*                   Data: 30-04-26
*********************************************************
"""
from collections import deque

class SistemaImpressao:
    def __init__(self):
        self.fila_adm = deque()
        self.fila_aluno = deque()
        self.fila_execucao = deque()

    def adicionar(self):
        tipo = input("Tipo (adm/aluno): ").strip().lower()
        nome = input("Nome do arquivo: ")
        paginas = int(input("Total de páginas: "))

        doc = {"arquivo": nome, "paginas": paginas}

        if tipo == "adm":
            self.fila_adm.append(doc)
            print("Adicionado na fila ADM.")
        elif tipo == "aluno":
            self.fila_aluno.append(doc)
            print("Adicionado na fila ALUNO.")
        else:
            print("Tipo inválido!")

    def consumir(self):
        if self.fila_execucao:
            doc = self.fila_execucao.popleft()
            print(f"Imprimindo: {doc['arquivo']} ({doc['paginas']} páginas)")
        else:
            print("Fila de execução vazia!")

    def listar(self):
        print("\n--- FILA ADM ---")
        for doc in self.fila_adm:
            print(f"{doc['arquivo']} ({doc['paginas']} páginas)")
        print(f"Total: {len(self.fila_adm)}")

        print("\n--- FILA ALUNO ---")
        for doc in self.fila_aluno:
            print(f"{doc['arquivo']} ({doc['paginas']} páginas)")
        print(f"Total: {len(self.fila_aluno)}")

        print("\n--- FILA EXECUÇÃO ---")
        for doc in self.fila_execucao:
            print(f"{doc['arquivo']} ({doc['paginas']} páginas)")
        print(f"Total: {len(self.fila_execucao)}")

        print("----------------------\n")

    def reorganizar(self):
        if self.fila_execucao:
            print("Não é possível reorganizar: fila de execução ainda possui documentos!")
            return

        while self.fila_adm:
            self.fila_execucao.append(self.fila_adm.popleft())

        while self.fila_aluno:
            self.fila_execucao.append(self.fila_aluno.popleft())

        print("Fila de execução organizada com prioridade ADM > ALUNO.")

    def menu(self):
        while True:
            print("1 - Adicionar fila")
            print("2 - Consumir fila")
            print("3 - Listar filas")
            print("4 - Reorganizar fila")
            print("0 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.adicionar()
            elif opcao == "2":
                self.consumir()
            elif opcao == "3":
                self.listar()
            elif opcao == "4":
                self.reorganizar()
            elif opcao == "0":
                print("Encerrando...")
                break
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    sistema = SistemaImpressao()
    sistema.menu()