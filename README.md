# Projeto IA

**Plataforma privada, modular, extensível e multifuncional de inteligência artificial.**

O **Projeto IA** é um projeto pessoal desenvolvido em Python, destinado à criação de uma plataforma capaz de integrar diferentes modelos de inteligência artificial, agentes especializados, ferramentas e processos automatizados.

Seu objetivo é permitir que múltiplas IAs trabalhem individualmente ou de maneira coordenada para realizar tarefas digitais de diferentes níveis de complexidade, mantendo segurança, transparência, rastreabilidade e controle do proprietário.

**Estado atual:** fundação técnica inicial construída, com auditoria e planejamento arquitetural em andamento.

**Versão inicial:** `0.1.0`.

> **Importante:** este README apresenta a visão completa do projeto, mas não afirma que todas as capacidades descritas já estejam implementadas. Funcionalidades existentes, planejadas e ainda não verificadas devem permanecer claramente diferenciadas.

---

## 1. Propósito do projeto

Construir uma plataforma geral de produção, desenvolvimento, pesquisa, criação e automação com inteligência artificial.

A plataforma deverá permitir que diferentes agentes, modelos, prompts, scripts e ferramentas sejam utilizados de forma coordenada para planejar, executar, verificar e aperfeiçoar tarefas.

O Projeto IA não será limitado a um chatbot, gerador de código ou auditor de software. Essas funções representam apenas partes de um sistema muito mais abrangente.

O desenvolvimento deverá preservar a possibilidade de incorporar novas capacidades, tecnologias e modalidades de IA sem comprometer a estabilidade, a segurança ou a organização da plataforma.

### Capacidades previstas

* **Desenvolvimento de software:** programas, aplicativos, sites, sistemas, servidores, APIs, jogos, scripts e automações.
* **Produção de documentos:** artigos, relatórios, documentos técnicos, textos e outros materiais.
* **Criação multimídia:** imagens, vídeos, áudios, voz e conteúdos gráficos.
* **Pesquisa e análise:** coleta, organização, comparação e avaliação de informações.
* **Execução de tarefas:** workflows com múltiplas etapas, ferramentas, prompts e agentes.
* **Auditoria e manutenção:** identificação de problemas, avaliação de riscos, testes e propostas de correção.
* **Aprendizagem controlada:** memória, registro de experiências, recuperação de informações e evolução das capacidades dos agentes.
* **Integração de tecnologias:** conexão com diferentes modelos, provedores, serviços e ferramentas.

Essas capacidades serão desenvolvidas progressivamente, conforme requisitos, viabilidade técnica, segurança e testes.

## 2. Princípios fundamentais

O desenvolvimento deverá seguir os seguintes princípios:

1. **Uso privado:** plataforma destinada ao proprietário, sem obrigação de disponibilização pública.
2. **Controle humano:** o proprietário mantém a autoridade final sobre decisões e operações importantes.
3. **Modularidade:** componentes separados por responsabilidades e interfaces bem definidas.
4. **Extensibilidade:** possibilidade de adicionar, atualizar ou substituir capacidades sem reestruturar desnecessariamente o sistema.
5. **Independência de fornecedores:** evitar dependência exclusiva de um único modelo, provedor ou serviço.
6. **Segurança por projeto:** proteger credenciais, arquivos, recursos e operações.
7. **Transparência:** apresentar descobertas, ações, resultados, erros e limitações relevantes.
8. **Verificabilidade:** utilizar testes, evidências e avaliações para sustentar conclusões.
9. **Aprendizagem controlada:** preservar informações úteis sem tratar automaticamente todo conteúdo obtido como confiável.
10. **Evolução gradual:** implementar funcionalidades em etapas verificáveis, preservando a fundação existente.

A escolha de tecnologias deverá ser orientada por necessidade, compatibilidade, confiabilidade, manutenção, segurança, custo e benefício real.

## 3. Arquitetura geral prevista

O Projeto IA deverá evoluir para uma arquitetura modular, composta por responsabilidades como:

| Componente      | Responsabilidade                                |
| --------------- | ----------------------------------------------- |
| Núcleo          | Inicialização, configuração e coordenação geral |
| Orquestrador    | Planejamento e distribuição de tarefas          |
| Agentes         | Execução de funções especializadas              |
| Provedores      | Integração com modelos de IA                    |
| Ferramentas     | Acesso controlado a recursos e serviços         |
| Workflows       | Execução de processos com múltiplas etapas      |
| Memória         | Armazenamento e recuperação de informações      |
| Avaliação       | Testes, análise de qualidade e validação        |
| Segurança       | Permissões, isolamento e controle de operações  |
| Observabilidade | Logs, métricas, histórico e acompanhamento      |
| Interface       | Interação e supervisão pelo proprietário        |

Esta é uma **proposta de responsabilidades arquiteturais**, não uma declaração de módulos já implementados.

As tecnologias, interfaces e dependências concretas deverão ser definidas mediante avaliação técnica.

## 4. Agentes, modelos e ferramentas

A plataforma deverá permitir que múltiplos agentes especializados colaborem na realização de tarefas.

Um agente poderá planejar uma atividade, outro executar partes específicas, outro verificar resultados e outro propor melhorias, conforme a arquitetura e as permissões disponíveis.

A integração com diferentes provedores deverá permitir selecionar modelos de acordo com suas capacidades, disponibilidade, custo, qualidade, requisitos de privacidade e adequação à tarefa.

Entre os provedores considerados inicialmente estão:

* OpenAI.
* Google Gemini.
* Anthropic Claude.
* Outros modelos e provedores compatíveis, incluindo alternativas locais quando apropriado.

O **OpenAI Agents SDK** integra a fundação atual, mas sua utilização não deve impedir avaliações futuras de outras tecnologias.

Ferramentas, APIs, scripts, serviços externos e protocolos como MCP poderão ser integrados quando houver necessidade técnica demonstrada.

A existência de bibliotecas instaladas ou variáveis de ambiente configuradas não comprova, por si só, o funcionamento dessas integrações.

## 5. Memória, aprendizagem e evolução

Um objetivo de longo prazo é permitir que os agentes preservem experiências e informações relevantes obtidas durante suas atividades.

O sistema deverá ser capaz de registrar, recuperar e avaliar conhecimentos úteis, incluindo:

* Informações pesquisadas e suas origens.
* Resultados de tarefas.
* Decisões e justificativas.
* Problemas encontrados.
* Soluções verificadas.
* Resultados de testes.
* Experiências anteriores.
* Informações relacionadas para estudos posteriores.

A aprendizagem deverá ser **controlada, rastreável e passível de correção**.

Os agentes poderão aprofundar pesquisas e explorar assuntos relacionados, mas deverão respeitar limites de tempo, recursos, custo, permissões e qualidade das informações.

### Acompanhamento da evolução

A plataforma deverá oferecer indicadores e histórico de desempenho dos agentes, incluindo métricas verificáveis de tarefas, testes, erros e melhorias.

Barras e percentuais de evolução deverão representar critérios mensuráveis, não uma porcentagem arbitrária de todo o conhecimento existente.

Não haverá um limite artificial de conhecimento definido como objetivo final; entretanto, a execução e o armazenamento deverão permanecer sujeitos a controles técnicos.

## 6. Segurança, auditoria e aprovação humana

A segurança e a transparência são requisitos centrais do Projeto IA.

Os agentes deverão ser capazes de identificar problemas, riscos e inconsistências, apresentar evidências, propor soluções e realizar verificações autorizadas.

A auditoria de código é uma das capacidades da plataforma, **não seu objetivo exclusivo**.

### Fluxo de alterações importantes

**Identificar → Explicar → Propor → Verificar → Solicitar aprovação → Aplicar → Testar → Registrar.**

O sistema deverá distinguir:

* Fatos confirmados.
* Inferências e hipóteses.
* Riscos potenciais.
* Erros comprovados.
* Informações pendentes de verificação.

Entre os controles previstos estão proteção de credenciais, permissões mínimas, isolamento de ferramentas, validação de entradas, defesa contra instruções maliciosas, limites de execução e custos, registros de auditoria, mecanismos de interrupção e recuperação de falhas.

Ações sensíveis ou de maior impacto deverão exigir aprovação do proprietário conforme políticas de risco definidas.

Os agentes deverão comunicar descobertas relevantes, sem ocultar problemas ou resultados importantes, respeitando a proteção de informações sensíveis.

Nenhuma auditoria deverá ser declarada completa sem evidências suficientes para o escopo analisado.

## 7. Tecnologias atuais

A fundação inicial utiliza:

* Python 3.13 ou superior.
* OpenAI Agents SDK.
* python-dotenv.
* pytest.
* Ruff.
* pre-commit.
* setuptools.
* Git e GitHub.

O ambiente de desenvolvimento atualmente utilizado é Windows com Git Bash e ambiente virtual Python.

Novas tecnologias deverão ser introduzidas gradualmente, após análise de necessidade, compatibilidade, segurança e manutenção.

## 8. Estrutura atual

```text
projeto-ia/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── README.md
├── main.py
├── pyproject.toml
├── src/
│   └── projeto_ia/
│       ├── __init__.py
│       ├── agent.py
│       └── config.py
└── tests/
    ├── test_agent.py
    └── test_config.py
```

Esta estrutura corresponde aos arquivos rastreados na última auditoria registrada.

Os diretórios de ambiente virtual, caches, builds e outros artefatos gerados permanecem excluídos do controle de versão conforme as regras verificadas.

## 9. Ambiente e desenvolvimento

O projeto utiliza um ambiente virtual Python e mantém credenciais locais fora do controle de versão.

O arquivo `.env.example` serve como referência para as variáveis de ambiente:

* `OPENAI_API_KEY`
* `GEMINI_API_KEY`
* `ANTHROPIC_API_KEY`

As dependências principais e as ferramentas de desenvolvimento são declaradas no `pyproject.toml`.

### Executar testes

```bash
python -m pytest
```

### Verificar qualidade do código

```bash
python -m ruff check .
```

### Verificar formatação

```bash
python -m ruff format --check .
```

### Executar verificações do pre-commit

```bash
python -m pre_commit run --all-files
```

### Verificar dependências instaladas

```bash
python -m pip check
```

O repositório também contém um workflow de integração contínua em `.github/workflows/ci.yml`.

A existência desse workflow não substitui a verificação de suas execuções remotas.

## 10. Estado atual do desenvolvimento

### Implementado e verificado localmente

* Estrutura inicial de pacote Python.
* Configuração de dependências.
* Ambiente virtual de desenvolvimento.
* Carregamento básico de variáveis de ambiente.
* Definição inicial de um agente.
* Testes automatizados básicos.
* Análise e formatação com Ruff.
* Hooks de pre-commit.
* Workflow inicial de integração contínua.
* Controle de versão e sincronização com GitHub.
* Regras de exclusão de arquivos gerados do versionamento.

### Parcialmente implementado ou ainda não validado integralmente

* Execução de agentes em cenários reais.
* Cobertura abrangente de testes.
* Segurança de todas as dependências.
* Validação da execução remota do CI.
* Tratamento robusto de falhas.
* Observabilidade e monitoramento operacional.

### Planejado

* Orquestração multiagente.
* Integração operacional de múltiplos provedores.
* Ferramentas e workflows avançados.
* Desenvolvimento automatizado de software.
* Produção de documentos e conteúdo multimídia.
* Memória persistente e aprendizagem controlada.
* Avaliação contínua de agentes.
* Interface de supervisão.
* Controle granular de permissões e custos.
* Auditoria automatizada ampliada.

## 11. Estratégia de evolução

O desenvolvimento será organizado em etapas, considerando dependências técnicas e prioridades.

**Fundação:** estrutura, configuração, testes, qualidade de código e controle de versão.

**Arquitetura:** definição de responsabilidades, módulos, contratos, segurança e mecanismos de coordenação.

**Agentes e provedores:** implementação e validação gradual de agentes especializados e modelos integrados.

**Ferramentas e workflows:** execução controlada de tarefas e processos automatizados.

**Memória e avaliação:** registro de experiências, recuperação de informações e acompanhamento da evolução.

**Expansão de capacidades:** desenvolvimento progressivo de funcionalidades de programação, pesquisa, documentos, imagens, vídeos, áudio e outras modalidades.

**Robustez operacional:** aperfeiçoamento contínuo de segurança, desempenho, recuperação de falhas, observabilidade e manutenção.

Essas etapas poderão ser refinadas ou reorganizadas mediante justificativa técnica e aprovação, sem alterar o objetivo original da plataforma.

## 12. Documentação complementar planejada

Para evitar que o README concentre especificações excessivamente extensas, os detalhes poderão ser organizados futuramente em documentos próprios:

| Documento                        | Finalidade                                       |
| -------------------------------- | ------------------------------------------------ |
| `docs/VISAO_DO_PROJETO.md`       | Objetivos completos, requisitos e limites        |
| `docs/ARQUITETURA.md`            | Componentes, interfaces e decisões técnicas      |
| `docs/SEGURANCA.md`              | Políticas de segurança, permissões e aprovações  |
| `docs/AGENTES_E_WORKFLOWS.md`    | Agentes, ferramentas, provedores e orquestração  |
| `docs/MEMORIA_E_APRENDIZAGEM.md` | Memória, avaliações e evolução                   |
| `docs/ROADMAP.md`                | Prioridades, entregas e critérios de conclusão   |
| `docs/CHECKPOINTS.md`            | Estado técnico, evidências, decisões e retomadas |
| `docs/ORDENS_E_DECISOES.md`      | Instruções ativas, substituídas e revogadas      |

**Esses arquivos são planejados e ainda não fazem parte da estrutura atual.**

A documentação deverá preservar as decisões anteriores, registrar alterações de requisitos e impedir que instruções antigas sejam aplicadas indevidamente.

## 13. Método de desenvolvimento

O trabalho no projeto deverá seguir um processo cuidadoso:

* Verificar o estado real antes de propor alterações.
* Aproveitar evidências e verificações anteriores quando ainda forem válidas.
* Planejar antecipadamente quais arquivos e informações serão necessários.
* Executar um comando por vez durante as etapas interativas no terminal.
* Conferir a sintaxe dos comandos antes de fornecê-los.
* Aguardar o resultado de cada comando antes de prosseguir.
* Não aplicar mudanças importantes sem autorização.
* Preservar checkpoints detalhados.
* Distinguir funcionalidades existentes, propostas e planejadas.
* Registrar decisões técnicas, justificativas e resultados.
* Priorizar correções comprovadamente necessárias.
* Evitar dependências, migrações e complexidade sem benefício demonstrado.
* Manter o usuário informado sobre riscos, falhas e limitações.

## 14. Checkpoint técnico de referência

**Data:** 09/10/2026.

**Branch:** `main`.

**Commit de referência:** `1efe6c9` — `Corrigir portabilidade do hook pytest`.

Na última verificação registrada:

* A branch local estava sincronizada com `origin/main`.
* A árvore de trabalho estava limpa.
* Os hooks de Ruff e pytest passaram localmente.
* Os arquivos gerados estavam ignorados pelo Git.
* O pacote `projeto-ia==0.1.0` estava instalado em modo editável.
* O inventário de dependências instaladas havia sido obtido.

Esse checkpoint representa o estado observado naquela data e não substitui verificações futuras quando necessárias.

---

## Objetivo de longo prazo

Desenvolver uma plataforma privada de inteligência artificial capaz de integrar e coordenar diferentes modelos, agentes, ferramentas e processos para realizar uma ampla variedade de tarefas digitais.

A plataforma deverá evoluir continuamente, ampliando suas capacidades de criação, desenvolvimento, automação, pesquisa, análise e aprendizagem, sempre com segurança, transparência, rastreabilidade, avaliação de resultados e supervisão humana.

**O objetivo é construir um sistema cada vez mais capaz e confiável, preservando o controle do proprietário e a possibilidade de expansão futura.**
