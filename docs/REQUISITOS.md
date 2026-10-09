# Requisitos — Projeto IA

## 1. Finalidade

Especificar os requisitos da plataforma privada, modular, extensível e multifuncional de inteligência artificial denominada Projeto IA.

Este documento complementa `docs/ARQUITETURA.md`, `docs/ORDENS_E_DECISOES.md` e `docs/CHECKPOINTS.md`.

## 2. Estado das decisões

- APROVADO: objetivo multifuncional completo, uso privado, supervisão humana e arquitetura de referência.
- OBJETIVO APROVADO: capacidades previstas para implementação progressiva.
- PROPOSTO: detalhamento dos requisitos e critérios de aceitação abaixo.
- PENDENTE: contratos técnicos, tecnologias adicionais, prioridades de implementação e validação detalhada.

A inclusão de um requisito neste documento não significa que a funcionalidade esteja implementada.

## 3. Requisitos funcionais

### RF-01 — Gerenciamento de tarefas e projetos

- RF-01.1: Criar tarefas com identificação, objetivo, entradas e resultados esperados.
- RF-01.2: Permitir tarefas com múltiplas etapas e dependências.
- RF-01.3: Acompanhar estados, progresso, resultados e falhas.
- RF-01.4: Prever interrupção, retomada e recuperação de tarefas.
- RF-01.5: Registrar artefatos produzidos e suas origens.

### RF-02 — Agentes e workflows

- RF-02.1: Permitir agentes especializados em diferentes capacidades.
- RF-02.2: Coordenar múltiplos agentes em uma mesma tarefa.
- RF-02.3: Permitir colaboração supervisionada entre agentes.
- RF-02.4: Organizar workflows com etapas, dependências e verificações.
- RF-02.5: Registrar decisões, ações e resultados relevantes dos agentes.

### RF-03 — Modelos e provedores

- RF-03.1: Integrar diferentes modelos e provedores por contratos explícitos.
- RF-03.2: Preservar a independência do núcleo em relação aos SDKs externos.
- RF-03.3: Permitir seleção de modelos conforme capacidade, qualidade, custo e privacidade.
- RF-03.4: Prever integração com OpenAI, Gemini, Claude e alternativas locais.
- RF-03.5: Tratar falhas e indisponibilidade de provedores.

### RF-04 — Desenvolvimento e automação

- RF-04.1: Planejar e produzir programas, aplicativos, sites, APIs, servidores e jogos.
- RF-04.2: Produzir e executar scripts mediante permissões adequadas.
- RF-04.3: Permitir testes, inspeções, correções propostas e manutenção de software.
- RF-04.4: Integrar ferramentas e serviços externos de maneira controlada.
- RF-04.5: Exigir autorização para operações importantes ou potencialmente perigosas.

### RF-05 — Documentos e multimídia

- RF-05.1: Produzir e revisar textos, artigos, relatórios e documentos.
- RF-05.2: Permitir criação e edição de imagens.
- RF-05.3: Permitir geração e processamento de vídeos.
- RF-05.4: Permitir geração e processamento de áudio e voz.
- RF-05.5: Registrar arquivos produzidos, formatos, versões e procedência.

### RF-06 — Pesquisa, memória e aprendizagem

- RF-06.1: Pesquisar, organizar, comparar e avaliar informações.
- RF-06.2: Registrar fontes, resultados, experiências e soluções verificadas.
- RF-06.3: Recuperar conhecimentos relevantes para novas tarefas.
- RF-06.4: Permitir aprofundamento encadeado de pesquisas sob limites controlados.
- RF-06.5: Distinguir informações verificadas, hipóteses e conteúdo não confiável.
- RF-06.6: Permitir correção, revisão e descarte de conhecimentos inadequados.

### RF-07 — Segurança e supervisão

- RF-07.1: Manter o proprietário como autoridade final sobre decisões importantes.
- RF-07.2: Aplicar permissões conforme o risco de cada operação.
- RF-07.3: Proteger credenciais, arquivos e informações sensíveis.
- RF-07.4: Prever isolamento e limites para ferramentas e scripts.
- RF-07.5: Registrar operações relevantes para auditoria.
- RF-07.6: Exigir aprovação antes de alterações sensíveis.
- RF-07.7: Tratar informações externas como dados não confiáveis até sua avaliação.

### RF-08 — Avaliação e acompanhamento

- RF-08.1: Registrar resultados de testes, tarefas, erros e melhorias.
- RF-08.2: Permitir comparação histórica de desempenho dos agentes.
- RF-08.3: Apresentar indicadores e percentuais baseados em critérios mensuráveis.
- RF-08.4: Registrar limitações, riscos e evidências das avaliações.
- RF-08.5: Permitir acompanhamento do progresso pelo proprietário.

## 4. Requisitos não funcionais

- RNF-01 — Segurança: proteger operações, dados, credenciais e recursos.
- RNF-02 — Modularidade: separar responsabilidades por contratos definidos.
- RNF-03 — Extensibilidade: permitir novas capacidades e provedores.
- RNF-04 — Confiabilidade: prever tratamento de erros e recuperação.
- RNF-05 — Rastreabilidade: identificar tarefas, decisões, resultados e origens.
- RNF-06 — Testabilidade: estabelecer verificações automatizadas e reproduzíveis.
- RNF-07 — Privacidade: manter o sistema orientado ao uso pessoal e privado.
- RNF-08 — Manutenibilidade: preservar organização e documentação técnica.
- RNF-09 — Eficiência: controlar consumo de recursos, tempo e custos.
- RNF-10 — Transparência: comunicar falhas, riscos e limitações relevantes.
- RNF-11 — Portabilidade: avaliar compatibilidade antes de introduzir dependências de ambiente.
- RNF-12 — Recuperabilidade: prever retomada consistente após interrupções.

## 5. Critérios gerais de aceitação propostos

Um requisito somente poderá ser considerado implementado quando:

1. Seu comportamento esperado estiver especificado.
2. Suas dependências e permissões estiverem identificadas.
3. Existirem verificações adequadas ao seu risco.
4. Os resultados das verificações estiverem registrados.
5. As limitações conhecidas estiverem documentadas.
6. O proprietário tiver aprovado as mudanças importantes aplicáveis.

A existência de código, dependências ou configurações não constitui, isoladamente, comprovação de funcionamento.

## 6. Matriz inicial de rastreabilidade

| Grupo | Componente principal previsto | Estado |
| --- | --- | --- |
| RF-01 | Núcleo e persistência | Especificação proposta |
| RF-02 | Orquestração e agentes | Especificação proposta |
| RF-03 | Provedores | Especificação proposta |
| RF-04 | Capacidades e ferramentas | Especificação proposta |
| RF-05 | Capacidades e artefatos | Especificação proposta |
| RF-06 | Memória e pesquisa | Especificação proposta |
| RF-07 | Segurança e supervisão | Especificação proposta |
| RF-08 | Avaliação e observabilidade | Especificação proposta |

## 7. Questões técnicas pendentes

- Contratos e formatos de entrada e saída dos componentes.
- Estados válidos das tarefas e transições permitidas.
- Políticas detalhadas de aprovação, permissões e isolamento.
- Persistência, versionamento e recuperação de artefatos.
- Estratégias de execução concorrente e distribuída.
- Métricas específicas para cada capacidade e agente.
- Limites de custo, tempo, armazenamento e recursos.
- Prioridades, fases e critérios de entrega por funcionalidade.

## 8. Próximas verificações

- Revisar este documento contra a arquitetura aprovada.
- Identificar lacunas, ambiguidades e requisitos conflitantes.
- Definir critérios de aceitação específicos e testáveis.
- Elaborar contratos e fluxos arquiteturais.
- Registrar decisões aprovadas e novos checkpoints.
- Não iniciar novos módulos antes de validar as especificações necessárias.

## 9. Preservação do objetivo

Nenhuma decisão técnica deverá reduzir o Projeto IA a uma única capacidade, provedor ou modalidade.

A plataforma deverá continuar preparada para integrar novas tecnologias e executar diferentes categorias de tarefas, preservando segurança, transparência, rastreabilidade e controle do proprietário.
