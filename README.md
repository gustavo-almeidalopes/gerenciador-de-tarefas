# Gerenciador de Tarefas

Este é um gerenciador de tarefas simples, criado com Python e a biblioteca Tkinter para a interface gráfica. Ele permite que o usuário adicione, edite, exclua, busque e marque tarefas como concluídas. Além disso, ele usa o arquivo `tasks.json` para armazenar as tarefas, e notifica o usuário sobre as ações realizadas através de notificações do sistema.

## Funcionalidades

- **Adicionar Tarefa**: Insira um título, categoria, prioridade e data de vencimento para uma nova tarefa.
- **Editar Tarefa**: Altere as informações de uma tarefa existente.
- **Excluir Tarefa**: Exclua uma tarefa existente após confirmação.
- **Marcar como Concluída**: Marque uma tarefa como concluída.
- **Listar Tarefas**: Exibe todas as tarefas e suas informações, com um status de conclusão.
- **Buscar Tarefas**: Pesquise tarefas pelo título.
- **Notificações**: Receba notificações quando uma tarefa for adicionada, concluída ou editada.

## Requisitos

Para rodar este projeto, é necessário ter o Python instalado em sua máquina. Além disso, o projeto utiliza a biblioteca `plyer` para notificações e `tkinter` para a interface gráfica.

### Instalando as dependências

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
   cd gerenciador-de-tarefas

2. Instale as dependências necessárias:
   ```bash
   pip install plyer

---

## Como usar

1. Execute o script main.pypara abrir uma interface gráfica:
   ```bash
     python main.py
   
3. Utilize uma interface gráfica para:
  <pre>
    • Adicionar novas tarefas
    • Editar tarefas existentes
    • Excluir tarefas
    • Marcar tarefas como concluídas
    • Pesquisar tarefas específicas
    • Visualizar uma lista de todas as tarefas
  </pre>
  
3. O arquivo tasks.jsonserá criado automaticamente e armazenará suas tarefas.

---

## Estrutura do Projeto

<pre>
  • main.py: O código principal que executa o gerenciador de tarefas.
  • tasks.json: Arquivo JSON que armazena as tarefas.
</pre>

---

##Contribuições

Sinta-se à vontade para contribuir para este projeto. Caso tenha sugestões de melhorias ou correções, abra um issue ou envie um pull request .
