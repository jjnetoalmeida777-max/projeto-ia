# Contrato de tarefas e projetos — RF-01

Estado: RASCUNHO TECNICO — sujeito a revisao e aprovacao.
Referencia: docs/REQUISITOS.md, docs/ARQUITETURA.md e docs/ORDENS_E_DECISOES.md.

## 1. Objetivo

Definir um contrato geral para representar, coordenar, acompanhar e recuperar tarefas executadas pelo Projeto IA.

O contrato deve atender programacao, desenvolvimento de software, sites, servidores, documentos, imagens, videos, audio, pesquisas, automacoes e workflows com multiplos agentes.

O contrato nao deve depender de um modelo, provedor ou ferramenta especifica.

## 2. Estrutura proposta de uma tarefa

Cada tarefa devera possuir:

- Identificador unico e estavel.
- Identificador do projeto associado, quando aplicavel.
- Objetivo e descricao.
- Tipo de capacidade solicitada.
- Entradas e referencias aos recursos necessarios.
- Resultados esperados e criterios de aceitacao.
- Estado atual e historico de transicoes.
- Prioridade e dependencias.
- Agente ou executor atribuido, quando houver.
- Permissoes aplicaveis e classificacao de risco.
- Referencias aos artefatos produzidos.
- Registros de tentativas, erros e resultados.
- Datas de criacao e atualizacao.

Campos obrigatorios, formatos e validacoes ainda precisam ser especificados.

## 3. Ciclo de vida proposto

Estados candidatos:

- criada
- em_validacao
- pronta
- em_execucao
- aguardando_aprovacao
- pausada
- concluida
- falhou
- cancelada

Transicoes permitidas, estados finais e regras de retomada permanecem pendentes de detalhamento.

## 4. Dependencias e coordenacao

- Uma tarefa podera depender da conclusao de outras tarefas.
- Dependencias invalidas e ciclos deverao ser detectados.
- Tarefas independentes poderao ser executadas em paralelo quando houver permissao e recursos suficientes.
- A falha de uma dependencia devera produzir comportamento explicito e rastreavel.
- Workflows deverao preservar o historico das tarefas participantes.

## 5. Autonomia supervisionada

Decisao ja aprovada pelo proprietario:

- Operacoes de baixo risco podem ser executadas automaticamente dentro das permissoes previamente concedidas.
- Operacoes importantes, sensiveis ou potencialmente perigosas exigem aprovacao explicita.
- Operacoes fora das permissoes concedidas nao podem ser executadas automaticamente.
- O proprietario mantem a autoridade final sobre decisoes importantes.

Pendente: definir classificacao objetiva de riscos, escopos de permissoes, expiracao, revogacao e fluxo de aprovacao.

## 6. Persistencia, interrupcao e recuperacao

- Estados e eventos relevantes deverao ser persistidos.
- Interrupcoes deverao ser identificaveis.
- Retomadas deverao considerar o ultimo estado confiavel.
- Operacoes com efeitos externos nao deverao ser repetidas sem verificacao de seguranca.
- Resultados parciais e falhas deverao permanecer rastreaveis.

Pendente: definir armazenamento, atomicidade, idempotencia e politica de repeticao.

## 7. Criterios de aceitacao propostos

- Criar uma tarefa valida com identificador unico.
- Rejeitar tarefas com dados obrigatorios invalidos.
- Consultar estado e historico de uma tarefa.
- Impedir transicoes de estado nao autorizadas.
- Detectar dependencias ciclicas.
- Bloquear operacoes fora das permissoes concedidas.
- Exigir aprovacao antes de operacoes classificadas como sensiveis.
- Registrar resultados, erros e artefatos.
- Recuperar uma tarefa interrompida sem repetir automaticamente efeitos externos perigosos.
- Permitir executores diferentes sem alterar o contrato central.

## 8. Decisoes tecnicas pendentes

- Esquema formal e versao do contrato.
- Campos obrigatorios e opcionais.
- Maquina de estados e transicoes permitidas.
- Modelo de dependencias e execucao paralela.
- Modelo de autorizacao e aprovacao.
- Estrategia de persistencia e recuperacao.
- Politica de tentativas, timeout e cancelamento.
- Estrutura de eventos e auditoria.
- Limites de recursos e custos.
- Testes detalhados de aceitacao.

## 9. Limites desta etapa

Este documento e uma proposta tecnica inicial, nao uma implementacao.

Nenhum modulo novo deve ser considerado concluido ou operacional com base apenas neste contrato.

As decisoes pendentes exigem revisao e aprovacao antes da implementacao.

## 10. Regras operacionais adicionais propostas

### 10.1. Tarefas compostas e subtarefas

- Uma tarefa podera ser dividida em subtarefas com identificadores proprios.
- Cada subtarefa devera manter referencia a tarefa de origem.
- Agentes diferentes poderao executar subtarefas distintas.
- O resultado da tarefa principal devera considerar os resultados e falhas de suas subtarefas.
- Dependencias entre tarefas e subtarefas deverao ser verificadas antes da execucao.

### 10.2. Limites de recursos

- Cada execucao devera respeitar os limites aplicaveis de tempo, custo e recursos computacionais.
- Limites de tentativas e de concorrencia deverao ser configuraveis.
- O esgotamento de limites devera gerar um estado ou evento rastreavel.
- A ampliacao de limites alem das permissoes concedidas devera exigir autorizacao.

### 10.3. Controle de transicoes

- Toda transicao de estado devera ser validada antes de sua aplicacao.
- Transicoes invalidas deverao ser rejeitadas e registradas.
- Mudancas de estado deverao preservar data, motivo e origem da alteracao.
- A definicao formal das transicoes permitidas permanece pendente.

### 10.4. Permissoes por operacao

- Cada operacao relevante devera ser autorizada antes da execucao.
- Uma autorizacao concedida para uma tarefa nao implica permissao irrestrita para todas as suas ferramentas.
- Acoes sensiveis deverao aguardar aprovacao explicita do proprietario.
- Permissoes revogadas deverao impedir novas operacoes dependentes delas.
- A classificacao de risco e o modelo de autorizacao permanecem pendentes.

### 10.5. Recuperacao e repeticao segura

- Operacoes sem efeitos externos poderao ser candidatas a repeticao automatica, conforme regras futuras.
- Operacoes com efeitos externos deverao exigir verificacao de seu resultado anterior antes de qualquer repeticao.
- Resultados desconhecidos nao deverao ser tratados automaticamente como falhas sem efeitos.
- Retomadas deverao preservar o historico e evitar duplicacao de artefatos ou acoes.
- Politicas de idempotencia, compensacao e recuperacao permanecem pendentes de especificacao.

Estas regras sao propostas tecnicas para revisao. Nao representam implementacao ou aprovacao definitiva.

## 11. Maquina de estados detalhada — proposta tecnica

Estado: PROPOSTA PARA REVISAO. As regras desta secao ainda nao representam aprovacao definitiva.

### 11.1. Separacao de responsabilidades

- Tarefa representa o objetivo, os requisitos, as dependencias e o resultado esperado.
- Execucao representa uma tentativa concreta de realizar uma tarefa.
- Subtarefa representa uma unidade de trabalho vinculada a uma tarefa principal.
- Uma tarefa podera possuir multiplas execucoes ao longo do tempo.
- Cada execucao devera preservar identificador, estado, executor, eventos e resultados.
- O estado da tarefa nao devera ser confundido com o estado de uma execucao individual.

### 11.2. Transicoes iniciais propostas

- criada -> em_validacao
- em_validacao -> pronta, falhou ou cancelada
- pronta -> em_execucao, pausada ou cancelada
- em_execucao -> aguardando_aprovacao, pausada, concluida, falhou ou cancelada
- aguardando_aprovacao -> em_execucao, pausada, falhou ou cancelada
- pausada -> pronta, em_validacao ou cancelada
- falhou -> em_validacao ou cancelada, somente mediante procedimento explicito de recuperacao
- concluida -> nenhuma transicao automatica
- cancelada -> nenhuma transicao automatica

Estas transicoes sao candidatas. A especificacao final devera considerar concorrencia, interrupcoes e operacoes externas em andamento.

### 11.3. Regras de seguranca

- Toda transicao devera ser validada e registrada.
- A entrada em em_execucao exigira verificacao das condicoes de execucao.
- A aprovacao de uma operacao nao concedera autorizacao irrestrita para outras operacoes.
- Uma aprovacao recusada ou expirada nao podera ser interpretada como permissao.
- Operacoes com resultado externo incerto nao deverao ser repetidas automaticamente.
- A conclusao exigira verificacao dos criterios de aceitacao aplicaveis.
- Cancelamentos e pausas deverao respeitar operacoes que nao podem ser interrompidas imediatamente.

### 11.4. Dependencias e subtarefas

- Uma tarefa dependente nao devera iniciar antes de satisfazer suas dependencias.
- A conclusao de uma tarefa principal devera considerar os resultados exigidos de suas subtarefas.
- Falhas de subtarefas deverao ser propagadas ou tratadas conforme politica explicita.
- Tarefas paralelas deverao preservar isolamento e rastreabilidade.
- Conflitos de atualizacao de estado deverao ser detectados.

### 11.5. Recuperacao e auditoria

- Eventos relevantes deverao registrar identificador, origem, instante e resultado.
- Tentativas de recuperacao deverao possuir historico proprio.
- A retomada devera verificar permissoes, dependencias e resultados anteriores.
- Efeitos externos deverao possuir mecanismos de verificacao ou reconciliacao.
- Estados inconsistentes deverao bloquear a continuidade automatica ate avaliacao segura.

### 11.6. Questoes ainda pendentes

- Definir formalmente as transicoes por evento e suas pre-condicoes.
- Especificar estados internos de execucao distintos dos estados de tarefa.
- Definir tratamento de aprovacao negada, expirada e revogada.
- Definir politicas de repeticao, timeout e recuperacao.
- Definir controle de concorrencia e persistencia atomica.
- Criar testes de aceitacao para transicoes validas e invalidas.

Nenhuma regra desta secao deve ser considerada implementada apenas por estar documentada.

## 12. Regras de seguranca e recuperacao — proposta tecnica

Estado: PROPOSTA PARA REVISAO.

### 12.1. Falhas e novas tentativas

- Cada tentativa de execucao devera possuir identificador proprio.
- Tentativas anteriores deverao preservar estados, eventos, erros e resultados.
- Uma nova tentativa nao devera apagar nem sobrescrever o historico anterior.
- A recuperacao devera verificar dependencias, permissoes e efeitos externos anteriores.
- Uma execucao interrompida com resultado incerto nao devera ser repetida automaticamente.

### 12.2. Aprovacoes

- Aprovacoes devem identificar a operacao autorizada e seu escopo.
- Aprovacoes recusadas, expiradas ou revogadas nao autorizam execucao.
- A tarefa nao deve continuar sem autorizacao valida.
- A autorizacao deve ser verificada novamente antes da operacao correspondente.
- Mudancas relevantes no escopo da operacao exigem nova avaliacao de permissao.

### 12.3. Pausa e cancelamento

- Solicitar pausa ou cancelamento nao significa que uma operacao externa foi interrompida.
- O sistema deve distinguir solicitacao, confirmacao e resultado da interrupcao.
- Operacoes nao interrompiveis devem ser acompanhadas ate um estado seguro conhecido.
- A tarefa nao deve ser declarada cancelada enquanto houver efeitos externos relevantes sem tratamento definido.
- Eventos de pausa, cancelamento e reconciliacao devem permanecer registrados.

### 12.4. Verificacao continua de permissoes

- Toda operacao relevante deve passar por verificacao de autorizacao antes da execucao.
- Permissoes concedidas anteriormente nao dispensam verificacoes posteriores.
- Revogacoes devem bloquear novas operacoes dependentes da permissao revogada.
- Operacoes importantes ou sensiveis devem exigir aprovacao explicita do proprietario.
- Na ausencia de autorizacao suficiente, a operacao deve permanecer bloqueada.

### 12.5. Pendencias para especificacao formal

- Definir eventos e estados intermediarios de interrupcao.
- Definir validade e escopo das aprovacoes.
- Definir mecanismos de reconciliacao de efeitos externos.
- Definir criterios de repeticao segura e idempotencia.
- Definir testes para falhas, revogacoes e cancelamentos concorrentes.

Estas regras complementam a secao 11 e permanecem sujeitas a revisao e aprovacao antes da implementacao.
