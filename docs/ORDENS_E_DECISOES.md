# Ordens e Decisões — Projeto IA

## 1. Finalidade

Preservar as ordens do proprietário, as decisões arquiteturais e o histórico de mudanças do Projeto IA.

Este documento deve distinguir decisões ativas, propostas pendentes, decisões substituídas e decisões revogadas.

Nenhuma orientação antiga deve prevalecer sobre uma decisão posterior explicitamente aprovada.

## 2. Objetivo definitivo — ATIVO

O Projeto IA será uma plataforma privada e multifuncional de inteligência artificial.

Deverá permitir desenvolver softwares, sites, aplicativos, servidores, APIs e jogos; produzir documentos, imagens, vídeos e áudios; realizar pesquisas; executar scripts e automações; coordenar agentes especializados e workflows; integrar diferentes modelos e provedores; e desenvolver memória e aprendizagem controladas.

Esse objetivo está estabelecido e não deve ser reduzido ou redefinido sem autorização expressa do proprietário.

## 3. Arquitetura de referência — APROVADA

Adotar inicialmente um monólito modular, orientado a tarefas, capacidades e agentes.

O núcleo deverá ser independente de provedores, com interfaces e contratos que permitam substituir ou acrescentar integrações.

Preservar a fundação Python existente e evitar infraestrutura complexa antes de sua necessidade ser demonstrada.

A arquitetura de referência está aprovada. Seus contratos e mecanismos detalhados ainda precisam ser especificados e validados.

Documento principal: docs/ARQUITETURA.md.

## 4. Ordens de desenvolvimento — ATIVAS

1. Considerar sempre o objetivo final completo antes de tomar decisões técnicas.
2. Priorizar estruturas extensíveis para minimizar reconstruções futuras.
3. Não implementar novos módulos antes de consolidar requisitos e arquitetura.
4. Analisar os arquivos necessários de forma planejada, solicitando o conjunto completo quando possível.
5. Fornecer um comando de terminal por vez, pronto para copiar e executar.
6. Verificar o resultado de cada comando antes de avançar.
7. Preservar arquivos e alterações existentes, evitando exclusões desnecessárias.
8. Distinguir fatos comprovados, inferências, propostas e pendências.
9. Não declarar testes, auditorias ou integrações concluídos sem evidências.
10. Manter checkpoints frequentes com decisões, resultados e próximo passo.
11. Exigir aprovação humana para mudanças importantes e operações de risco.
12. Manter transparência sobre problemas, riscos e limitações identificados.

## 5. Requisitos futuros — ATIVOS COMO OBJETIVOS

- Orquestração de múltiplos agentes, prompts, ferramentas e workflows.
- Integração com OpenAI, Gemini, Claude e outros provedores.
- Produção de código, documentos, imagens, vídeos e áudios.
- Memória persistente, recuperação de conhecimentos e aprendizagem controlada.
- Acompanhamento histórico de desempenho, qualidade e evolução.
- Pesquisa aprofundada e encadeada, respeitando limites e supervisão.
- Segurança, permissões, isolamento, auditoria e rastreabilidade.
- Controle exclusivo do proprietário sobre decisões importantes.

Esses itens representam objetivos aprovados, não funcionalidades já implementadas.

## 6. Decisões técnicas pendentes

- Contratos entre componentes.
- Ciclo de vida e persistência das tarefas.
- Estratégia de execução paralela e recuperação.
- Modelo detalhado de permissões e isolamento.
- Armazenamento de artefatos e memória.
- Critérios de avaliação e aceitação dos requisitos.
- Escolha de tecnologias adicionais conforme necessidade comprovada.

## 7. Orientações substituídas ou revogadas

A orientação de tratar auditoria de código como possível finalidade central está SUBSTITUÍDA pela visão multifuncional completa. Auditoria permanece uma capacidade da plataforma, não seu objetivo exclusivo.

Não há outras revogações formalmente confirmadas neste registro inicial.

Novas substituições e revogações deverão identificar a decisão anterior, a nova decisão, a data e a justificativa.

## 8. Controle de alterações

Data de referência: 09/10/2026.

Estado: registro inicial das ordens e decisões aprovadas.

Toda alteração importante deverá preservar o histórico, registrar sua justificativa e obter aprovação do proprietário antes de mudar a direção estabelecida.

## 9. Autonomia supervisionada — APROVADA

Data: 10/10/2026.

Decisao expressamente aprovada pelo proprietario: adotar o modelo inicial de autonomia supervisionada para os agentes do Projeto IA.

### Regras aprovadas

- Agentes podem executar automaticamente tarefas de baixo risco dentro de permissoes previamente autorizadas.
- Operacoes importantes, sensiveis ou potencialmente perigosas exigem aprovacao explicita do proprietario.
- Operacoes fora das permissoes concedidas nao podem ser executadas automaticamente.
- Falhas, riscos e decisoes relevantes devem ser registrados e comunicados conforme sua importancia.
- O proprietario mantem a autoridade final sobre decisoes importantes.

### Detalhamento pendente

- Definir niveis de risco e criterios objetivos de classificacao.
- Definir escopos, validade e revogacao de permissoes.
- Especificar solicitacoes de aprovacao, recusas e expiracao.
- Definir comportamento seguro diante de falhas, interrupcoes e incertezas.
- Integrar essas regras aos contratos de tarefas, agentes e ferramentas.

Esta decisao nao representa implementacao concluida. Sua especificacao e validacao tecnica permanecem pendentes.
