# Projeto IA

Projeto pessoal de Inteligência Artificial desenvolvido em Python.

## Objetivo

Construir uma aplicação de IA com uma base organizada, testável e segura, evoluindo gradualmente para workflows com agentes, ferramentas e integrações.

Um dos principais objetivos deste projeto é permitir que agentes auditem o projeto, encontrem problemas, riscos e inconsistências, expliquem suas descobertas, proponham soluções e realizem testes e verificações. Mudanças importantes devem aguardar a aprovação do usuário antes de serem aplicadas.

## Tecnologias

- Python 3.13+
- OpenAI Agents SDK
- python-dotenv
- pytest
- Ruff
- pre-commit

## Estrutura

```text
projeto-ia/
├── src/
│   └── projeto_ia/
│       ├── __init__.py
│       ├── agent.py
│       └── config.py
├── tests/
│   ├── test_agent.py
│   └── test_config.py
├── main.py
├── pyproject.toml
├── README.md
└── .env.example
```

## Ambiente

O projeto utiliza um ambiente virtual Python e mantém as credenciais de ambiente fora do controle de versão.

O arquivo `.env.example` serve como modelo para as variáveis de ambiente utilizadas pelo projeto.

## Desenvolvimento

As ferramentas de desenvolvimento são declaradas no grupo `dev` do `pyproject.toml`.

### Pre-commit

Após instalar as dependências de desenvolvimento, ative os hooks do Git:

```bash
pre-commit install
```

Os hooks executam verificações de qualidade e testes automaticamente durante os commits.

### Testes

```bash
python -m pytest
```

### Verificação de qualidade

```bash
ruff check .
```

### Verificação de formatação

```bash
ruff format --check .
```

## Status

O projeto está em fase de construção da fundação técnica.

A implementação de agentes, ferramentas, integrações e demais componentes da aplicação será adicionada gradualmente, sempre acompanhada de testes e validações.
