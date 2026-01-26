# Sistema Lista de Tarefas

Este é um aplicativo web desenvolvido em Django como parte de um desafio de desenvolvimento. O sistema permite que usuários gerenciem suas tarefas de forma simples, oferecendo funcionalidades de CRUD (criar, ler, atualizar e excluir) e organização prática da lista de tarefas.


## Installation and Setup

### 1. Clone the repository:

```bash
git clone kenzokomati/lista-de-tarefas-fatto
cd todo-list
```

### 2. Create a virtual environment:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On MacOS:
source venv/bin/activate 
```

### 3. Install dependencies:

```bash
uv sync
```
  
### 4. Apply database migrations:

```bash
python manage.py migrate
```

### 5. Run the development server:

```bash
python manage.py runserver  
```
