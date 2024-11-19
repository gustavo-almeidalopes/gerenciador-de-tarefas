import json
import os
from plyer import notification 
import tkinter as tk
from tkinter import messagebox

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def list_tasks(tasks):
    if not tasks:
        messagebox.showinfo("Lista de Tarefas", "Nenhuma tarefa encontrada.")
        return

    task_list = "\n".join([f"{idx + 1}. {task['title']} - {'Concluída' if task['completed'] else 'Pendente'} - {task.get('category', 'Sem Categoria')} - Prioridade: {task.get('priority', 'N/A')}"
                          for idx, task in enumerate(tasks)])

    notification.notify(
        title="Lista de Tarefas",
        message=f"Tarefas:\n{task_list}",
        timeout=8
    )
    messagebox.showinfo("Lista de Tarefas", task_list)

def add_task(tasks, title_entry, category_entry, priority_entry, due_date_entry):
    title = title_entry.get()
    category = category_entry.get()
    priority = priority_entry.get()
    due_date = due_date_entry.get()
    if title:
        tasks.append({'title': title, 'completed': False, 'category': category, 'priority': priority, 'due_date': due_date})
        save_tasks(tasks)
        messagebox.showinfo("Tarefa Adicionada", "Tarefa adicionada com sucesso.")
        title_entry.delete(0, tk.END)  # Limpa o campo de entrada
        category_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira um título para a tarefa.")

def edit_task(tasks, edit_index_entry, new_title_entry, new_category_entry, new_priority_entry, new_due_date_entry):
    try:
        index = int(edit_index_entry.get()) - 1
        if 0 <= index < len(tasks):
            new_title = new_title_entry.get()
            new_category = new_category_entry.get()
            new_priority = new_priority_entry.get()
            new_due_date = new_due_date_entry.get()
            if new_title:
                tasks[index]['title'] = new_title
            if new_category:
                tasks[index]['category'] = new_category
            if new_priority:
                tasks[index]['priority'] = new_priority
            if new_due_date:
                tasks[index]['due_date'] = new_due_date
            save_tasks(tasks)
            messagebox.showinfo("Tarefa Editada", "Tarefa editada com sucesso.")
            edit_index_entry.delete(0, tk.END)
            new_title_entry.delete(0, tk.END)
            new_category_entry.delete(0, tk.END)
            new_priority_entry.delete(0, tk.END)
            new_due_date_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Índice Inválido", "Número de tarefa inválido.")
    except ValueError:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira um número válido.")

def delete_task(tasks, delete_index_entry):
    try:
        index = int(delete_index_entry.get()) - 1
        if 0 <= index < len(tasks):
            if messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir a tarefa '{tasks[index]['title']}'?"):
                tasks.pop(index)
                save_tasks(tasks)
                messagebox.showinfo("Tarefa Excluída", "Tarefa excluída com sucesso.")
                delete_index_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Índice Inválido", "Número de tarefa inválido.")
    except ValueError:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira um número válido.")

def mark_task_completed(tasks, complete_index_entry):
    try:
        index = int(complete_index_entry.get()) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            save_tasks(tasks)
            messagebox.showinfo("Tarefa Concluída", f"Tarefa '{tasks[index]['title']}' marcada como concluída.")
            notification.notify(
                title="Tarefa Concluída!",
                message=f"Tarefa '{tasks[index]['title']}' foi marcada como concluída.",
                timeout=5  # duração da notificação
            )
            complete_index_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Índice Inválido", "Número de tarefa inválido.")
    except ValueError:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira um número válido.")

def search_tasks(tasks, search_entry):
    query = search_entry.get().lower()
    if query:
        filtered_tasks = [task for task in tasks if query in task['title'].lower()]
        if filtered_tasks:
            task_list = "\n".join([f"{idx + 1}. {task['title']} - {'Concluída' if task['completed'] else 'Pendente'} - {task.get('category', 'Sem Categoria')} - Prioridade: {task.get('priority', 'N/A')}"
                                  for idx, task in enumerate(filtered_tasks)])
            messagebox.showinfo("Resultado da Busca", task_list)
        else:
            messagebox.showinfo("Resultado da Busca", "Nenhuma tarefa encontrada para a busca.")
    else:
        messagebox.showwarning("Busca Vazia", "Por favor, insira um termo para buscar.")

def setup_gui():
    tasks = load_tasks()

    window = tk.Tk()
    window.title("Gerenciador de Tarefas")

    window.geometry("600x700")
    window.resizable(True, True)  # Permitir redimensionamento da janela

    tk.Label(window, text="Gerenciador de Tarefas", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(window, text="Buscar Tarefa:").grid(row=1, column=0, sticky='e', padx=10)
    search_entry = tk.Entry(window, width=50)
    search_entry.grid(row=1, column=1, pady=5)

    search_button = tk.Button(window, text="Buscar", command=lambda: search_tasks(tasks, search_entry))
    search_button.grid(row=2, column=0, columnspan=2, pady=10)

    tk.Label(window, text="Título da Tarefa:").grid(row=3, column=0, sticky='e', padx=10)
    title_entry = tk.Entry(window, width=50)
    title_entry.grid(row=3, column=1, pady=5)
    
    tk.Label(window, text="Categoria:").grid(row=4, column=0, sticky='e', padx=10)
    category_entry = tk.Entry(window, width=50)
    category_entry.grid(row=4, column=1, pady=5)
    
    tk.Label(window, text="Prioridade:").grid(row=5, column=0, sticky='e', padx=10)
    priority_entry = tk.Entry(window, width=50)
    priority_entry.grid(row=5, column=1, pady=5)
    
    tk.Label(window, text="Data de Vencimento (DD/MM/AAAA):").grid(row=6, column=0, sticky='e', padx=10)
    due_date_entry = tk.Entry(window, width=50)
    due_date_entry.grid(row=6, column=1, pady=5)

    add_button = tk.Button(window, text="Adicionar Tarefa", command=lambda: add_task(tasks, title_entry, category_entry, priority_entry, due_date_entry))
    add_button.grid(row=7, column=0, columnspan=2, pady=10)

    tk.Label(window, text="Número da Tarefa para Editar:").grid(row=8, column=0, sticky='e', padx=10)
    edit_index_entry = tk.Entry(window, width=50)
    edit_index_entry.grid(row=8, column=1, pady=5)

    tk.Label(window, text="Novo Título da Tarefa:").grid(row=9, column=0, sticky='e', padx=10)
    new_title_entry = tk.Entry(window, width=50)
    new_title_entry.grid(row=9, column=1, pady=5)
    
    tk.Label(window, text="Nova Categoria:").grid(row=10, column=0, sticky='e', padx=10)
    new_category_entry = tk.Entry(window, width=50)
    new_category_entry.grid(row=10, column=1, pady=5)
    
    tk.Label(window, text="Nova Prioridade:").grid(row=11, column=0, sticky='e', padx=10)
    new_priority_entry = tk.Entry(window, width=50)
    new_priority_entry.grid(row=11, column=1, pady=5)
    
    tk.Label(window, text="Nova Data de Vencimento (DD/MM/AAAA):").grid(row=12, column=0, sticky='e', padx=10)
    new_due_date_entry = tk.Entry(window, width=50)
    new_due_date_entry.grid(row=12, column=1, pady=5)

    edit_button = tk.Button(window, text="Editar Tarefa", command=lambda: edit_task(tasks, edit_index_entry, new_title_entry, new_category_entry, new_priority_entry, new_due_date_entry))
    edit_button.grid(row=13, column=0, columnspan=2, pady=10)

    tk.Label(window, text="Número da Tarefa para Excluir:").grid(row=14, column=0, sticky='e', padx=10)
    delete_index_entry = tk.Entry(window, width=50)
    delete_index_entry.grid(row=14, column=1, pady=5)

    delete_button = tk.Button(window, text="Excluir Tarefa", command=lambda: delete_task(tasks, delete_index_entry))
    delete_button.grid(row=15, column=0, columnspan=2, pady=10)

    tk.Label(window, text="Número da Tarefa para Concluir:").grid(row=16, column=0, sticky='e', padx=10)
    complete_index_entry = tk.Entry(window, width=50)
    complete_index_entry.grid(row=16, column=1, pady=5)

    complete_button = tk.Button(window, text="Concluir Tarefa", command=lambda: mark_task_completed(tasks, complete_index_entry))
    complete_button.grid(row=17, column=0, columnspan=2, pady=10)

    list_button = tk.Button(window, text="Listar Tarefas", command=lambda: list_tasks(tasks))
    list_button.grid(row=18, column=0, columnspan=2, pady=10)

    window.mainloop()

setup_gui()
