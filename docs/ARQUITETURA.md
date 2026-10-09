# Arquitetura de Referência — Projeto IA

## 1. Objetivo definitivo

O Projeto IA é uma plataforma privada e multifuncional de inteligência artificial, destinada ao uso pessoal de seu proprietário.

Seu objetivo inclui criar e manter softwares, sites, aplicativos, servidores, APIs e jogos; produzir documentos, imagens, vídeos e áudios; executar scripts e automações; realizar pesquisas; coordenar agentes especializados; integrar diferentes modelos e provedores; e desenvolver memória e aprendizagem controladas.

A arquitetura deve preservar esse objetivo completo durante toda a evolução do projeto.

## 2. Decisão arquitetural

Adotar como arquitetura de referência um monólito modular, orientado a tarefas, capacidades e agentes, com núcleo independente de provedores e componentes substituíveis por meio de contratos explícitos.

A implementação será gradual. A arquitetura deverá permitir expansão futura sem exigir reconstruções desnecessárias.

## 3. Componentes previstos

- Núcleo de domínio: contratos, tarefas, estados, resultados e artefatos.
- Orquestração: planejamento, coordenação de agentes e workflows.
- Agentes: execução especializada e colaboração supervisionada.
- Provedores: adaptadores para OpenAI, Gemini, Claude e outros.
- Capacidades: programação, documentos, imagens, vídeos, áudios e outras.
- Ferramentas: execução controlada de scripts, APIs e serviços.
- Persistência: armazenamento de tarefas, estados e resultados.
- Memória: conhecimentos, fontes, experiências e recuperação.
- Avaliação: testes, métricas, qualidade e evolução.
- Segurança: permissões, aprovações, isolamento e auditoria.
- Observabilidade: registros, erros, desempenho e rastreabilidade.
- Interfaces: interação, acompanhamento, controle e supervisão humana.

## 4. Princípios obrigatórios

1. Preservar o objetivo final da plataforma.
2. Evitar dependência exclusiva de qualquer provedor ou SDK.
3. Separar regras do núcleo das integrações externas.
4. Permitir expansão por módulos e contratos versionados.
5. Tratar tarefas como operações identificáveis e rastreáveis.
6. Registrar resultados e artefatos com suas origens.
7. Controlar permissões e operações potencialmente perigosas.
8. Exigir aprovação humana para mudanças importantes.
9. Projetar interrupção, recuperação e tratamento de falhas.
10. Distinguir fatos verificados, propostas e pendências.
11. Medir a evolução dos agentes por critérios verificáveis.
12. Evitar complexidade e infraestrutura prematuras.

## 5. Decisões de implementação

- Preservar a fundação Python existente.
- Manter o OpenAI Agents SDK como integração inicial, sem torná-lo dependência obrigatória do núcleo futuro.
- Preparar contratos para múltiplos provedores, agentes e ferramentas.
- Prever execução paralela e distribuída sem implementá-la prematuramente.
- Não escolher antecipadamente microsserviços, Kubernetes, filas ou bancos específicos sem requisitos e evidências suficientes.
- Implementar novas capacidades progressivamente, acompanhadas de testes e verificações.

## 6. Segurança e supervisão

O sistema deverá operar sob controle de seu proprietário.

Operações importantes seguirão, conforme o risco, o fluxo de identificar, explicar, propor, verificar, solicitar aprovação, executar, testar e registrar.

Informações externas e memórias recuperadas não serão automaticamente tratadas como instruções confiáveis.

A execução de ferramentas deverá respeitar permissões, limites e mecanismos de auditoria.

## 7. Estado confirmado em 09/10/2026

O repositório possui uma fundação Python com configuração de ambiente, um agente inicial, testes automatizados, Ruff, pre-commit e configuração de CI.

Os arquivos técnicos foram examinados estaticamente. Isso não comprova execução real de múltiplos provedores, orquestração avançada, memória persistente, produção multimídia ou isolamento de ferramentas.

O último commit previamente confirmado e sincronizado é 5d173c9.

## 8. Pendências antes de novos módulos

- Consolidar requisitos funcionais e não funcionais.
- Definir contratos, responsabilidades e fluxos entre componentes.
- Especificar estados, persistência e recuperação de tarefas.
- Definir modelo de permissões, aprovações e isolamento.
- Estabelecer critérios de aceitação e matriz de rastreabilidade.
- Validar as decisões contra o código existente e testes.

## 9. Preservação das decisões

Este documento registra a arquitetura de referência aprovada.

Mudanças importantes deverão ser justificadas, analisadas quanto ao impacto no objetivo final, submetidas à aprovação do proprietário e registradas em documentos versionados.

A arquitetura de referência está escolhida, mas seus contratos técnicos detalhados permanecem sujeitos a especificação e validação.
