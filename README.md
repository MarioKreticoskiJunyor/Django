# Cadastro de Usuários com Django

Aplicação web simples de cadastro e listagem de usuários, feita como meu primeiro
projeto com Django (2023).

## Funcionalidades

- Página inicial com formulário de cadastro (nome e idade)
- Gravação do usuário no banco SQLite
- Página de listagem com todos os usuários cadastrados

Edição e exclusão de usuários **não** estão implementadas.

## Tecnologias

- Python 3.11
- Django 4.2
- SQLite
- Templates do Django com Bootstrap 5

## Estrutura

```text
projeto_cad_usuarios/   # configurações do projeto (settings, urls, wsgi/asgi)
app_cadastro_usua/      # app de cadastro
├── models.py           # modelo usuario (id_usuario, nome, idade)
├── views.py            # views home e usuarios
├── migrations/
└── templates/usuarios/ # base.html, home.html, usuarios.html
manage.py
```

Rotas:

| URL | View | Descrição |
|---|---|---|
| `/` | `home` | formulário de cadastro |
| `/usuarios/` | `usuarios` | grava o usuário enviado (POST) e lista os cadastrados |

## Como executar

```bash
python -m venv venv
venv\Scripts\activate          # Windows  ·  Linux/macOS: source venv/bin/activate
pip install "django>=4.2,<5.0"
python manage.py migrate
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/`.

## Testes

O projeto não possui testes automatizados (`app_cadastro_usua/tests.py` está vazio).

## Estado atual

Projeto de estudo concluído, mantido como registro do meu primeiro contato com Django.
A configuração é de desenvolvimento (`DEBUG = True` e chave secreta local) e não
deve ser usada em produção.

## Melhorias planejadas

*Ainda não implementadas:*

- Editar e excluir usuários
- Validar os dados do formulário com Django Forms
- Adicionar `requirements.txt` e testes
- Ler a `SECRET_KEY` de variável de ambiente
