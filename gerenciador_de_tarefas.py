import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QLabel

class GerenciadorDeTarefas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerenciador de Tarefas")  # Define o título da janela
        self.setGeometry(100, 100, 400, 300)  # Define a posição e o tamanho da janela

        central_widget = QWidget(self)  # Cria um widget central para a janela
        self.setCentralWidget(central_widget)  # Define o widget central

        layout = QVBoxLayout(central_widget)  # Cria um layout de grade vertical para organizar os elementos

        self.tarefa_input = QLineEdit(self)  # Cria uma caixa de entrada de texto para inserir tarefas
        self.adicionar_button = QPushButton("Adicionar", self)  # Cria um botão para adicionar tarefas
        self.adicionar_button.clicked.connect(self.adicionar_tarefa)  # Conecta o botão a um método

        self.tarefas_list = QListWidget(self)  # Cria uma lista para exibir as tarefas
        self.tarefas_list.setSelectionMode(QListWidget.SelectionMode.SingleSelection)  # Define o modo de seleção
        self.tarefas_list.itemClicked.connect(self.exibir_tarefa)  # Conecta o evento de clique a um método

        self.atualizar_button = QPushButton("Atualizar", self)  # Cria um botão para atualizar tarefas
        self.atualizar_button.clicked.connect(self.atualizar_tarefa)  # Conecta o botão a um método

        self.excluir_button = QPushButton("Excluir", self)  # Cria um botão para excluir tarefas
        self.excluir_button.clicked.connect(self.excluir_tarefa)  # Conecta o botão a um método

        self.result_label = QLabel(self)  # Cria uma etiqueta para exibir mensagens de resultado

        layout.addWidget(self.tarefa_input)  # Adiciona a caixa de entrada ao layout
        layout.addWidget(self.adicionar_button)  # Adiciona o botão "Adicionar" ao layout
        layout.addWidget(self.tarefas_list)  # Adiciona a lista de tarefas ao layout
        layout.addWidget(self.atualizar_button)  # Adiciona o botão "Atualizar" ao layout
        layout.addWidget(self.excluir_button)  # Adiciona o botão "Excluir" ao layout
        layout.addWidget(self.result_label)  # Adiciona a etiqueta de resultado ao layout

        self.tarefas = []  # Inicializa uma lista vazia para armazenar as tarefas

    def adicionar_tarefa(self):
        tarefa = self.tarefa_input.text()  # Obtém o texto da caixa de entrada
        if tarefa:
            self.tarefas.append(tarefa)  # Adiciona a tarefa à lista
            self.tarefa_input.clear()  # Limpa a caixa de entrada
            self.atualizar_lista_tarefas()  # Atualiza a lista de tarefas

    def atualizar_lista_tarefas(self):
        self.tarefas_list.clear()  # Limpa a lista de tarefas
        self.tarefas_list.addItems(self.tarefas)  # Adiciona as tarefas da lista à lista de exibição

    def exibir_tarefa(self, item):
        tarefa_selecionada = item.text()  # Obtém a tarefa selecionada da lista
        self.tarefa_input.setText(tarefa_selecionada)  # Exibe a tarefa na caixa de entrada

    def atualizar_tarefa(self):
        tarefa_atualizada = self.tarefa_input.text()  # Obtém o texto da caixa de entrada
        if tarefa_atualizada:
            indice = self.tarefas_list.currentRow()  # Obtém o índice da tarefa selecionada na lista
            if indice != -1:
                self.tarefas[indice] = tarefa_atualizada  # Atualiza a tarefa na lista
                self.atualizar_lista_tarefas()  # Atualiza a lista de tarefas
                self.result_label.setText("Tarefa atualizada com sucesso!")  # Exibe uma mensagem de sucesso

    def excluir_tarefa(self):
        indice = self.tarefas_list.currentRow()  # Obtém o índice da tarefa selecionada na lista
        if indice != -1:
            del self.tarefas[indice]  # Remove a tarefa da lista
            self.atualizar_lista_tarefas()  # Atualiza a lista de tarefas
            self.result_label.setText("Tarefa excluída com sucesso!")  # Exibe uma mensagem de sucesso

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Inicializa a aplicação Qt
    gerenciador = GerenciadorDeTarefas()  # Cria uma instância da classe 'GerenciadorDeTarefas'
    gerenciador.show()  # Exibe a janela da aplicação
    sys.exit(app.exec())  # Executa o loop de eventos da aplicação
