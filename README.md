# Projeto: Gerenciador de Tarefas

## Autor: Michael Douglas P Lima
## Contato: michaelsjmvr@hotmail.com
## LinkedIn: [michael-douglas-640a11180](https://www.linkedin.com/in/michael-douglas-640a11180/)

## Descrição do Projeto
O projeto "Gerenciador de Tarefas" é uma aplicação de desktop simples desenvolvida usando PySide6, uma biblioteca para criar interfaces gráficas em Python. O objetivo desta aplicação é permitir que os usuários adicionem, atualizem e excluam tarefas de uma lista de tarefas.

## Interface Gráfica
A aplicação "Gerenciador de Tarefas" possui uma interface amigável para gerenciar tarefas de forma eficiente. A interface inclui os seguintes elementos:

- **Janela Principal:** Exibe o título "Gerenciador de Tarefas" e tem um tamanho fixo de 400x300 pixels, posicionada na tela.

- **Interface de Usuário:** Organizada verticalmente, inclui os seguintes componentes:

  - **Caixa de Entrada de Tarefas:** Uma caixa de entrada de texto onde os usuários podem digitar uma nova tarefa que desejam adicionar. Os usuários podem inserir uma descrição da tarefa nesta caixa de entrada.

  - **Botão "Adicionar":** Permite aos usuários adicionar a tarefa digitada na caixa de entrada à lista de tarefas. Quando o botão é clicado, a tarefa é adicionada à lista e a caixa de entrada é limpa.

  - **Lista de Tarefas:** Exibe todas as tarefas adicionadas pelos usuários. Os usuários podem selecionar uma tarefa na lista, e a descrição da tarefa selecionada é exibida na caixa de entrada para possível edição.

  - **Botão "Atualizar":** Permite aos usuários atualizar a descrição de uma tarefa selecionada na lista. Quando o botão é clicado, a descrição da tarefa selecionada na lista é atualizada com o texto na caixa de entrada.

  - **Botão "Excluir":** Permite aos usuários excluir uma tarefa selecionada na lista. Quando o botão é clicado, a tarefa selecionada é removida da lista.

  - **Etiqueta de Resultado:** Uma etiqueta que exibe mensagens de resultado, como "Tarefa atualizada com sucesso!" ou "Tarefa excluída com sucesso!".

## Funcionalidades
A aplicação oferece as seguintes funcionalidades:

- Inserção de tarefas digitando uma descrição na caixa de entrada e clicando no botão "Adicionar".
- Exibição das tarefas adicionadas na lista de tarefas.
- Seleção de uma tarefa na lista para exibir sua descrição na caixa de entrada.
- Atualização da descrição de uma tarefa selecionada clicando no botão "Atualizar".
- Exclusão de uma tarefa selecionada clicando no botão "Excluir".
- Exibição de mensagens de resultado na etiqueta de resultado para indicar o sucesso das operações.

## Executando a Aplicação
Para executar a aplicação:

1. Certifique-se de ter Python instalado.

2. Instale a biblioteca PySide6, se ainda não estiver instalada, usando o comando `pip install PySide6`.

3. Execute o código a partir da definição da classe GerenciadorDeTarefas até o final do arquivo.

4. A interface gráfica da aplicação será exibida, permitindo o gerenciamento das tarefas.

## Contribuição
Este projeto é de código aberto e está aberto a contribuições. Você pode melhorar a aplicação ou adicionar novos recursos conforme necessário.

Este projeto fornece uma interface gráfica simples para gerenciar tarefas de forma eficiente. É uma aplicação básica, mas funcional, adequada para tarefas de organização pessoal.
