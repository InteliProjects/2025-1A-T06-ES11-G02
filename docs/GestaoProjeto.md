# Gestão Evolutiva do Projeto
## Versionamento da documentação 
Histórico de lançamentos

* 0.1.0 - 14/02/2025
    * Análise Exploratória E De Governança De Dados
    * Template De Projeto De Gestão E Governança De Dados
    * Wireframe Do DataApp
    * Documentação Do Projeto De Gestão E Governança De Dados
    * Gestão Evolutiva Do Projeto
* 0.2.0 - 28/02/2025
    * Módulo De Ingestão E Transformação De Dados
    * Documentação Do Projeto De Gestão E Governança De Dados
    * Gestão Evolutiva Do Projeto
* 0.3.0 - 14/03/2025
    * Módulo De Processamento, Integração E Manipulação De Dados.
    * Mockup Do DataApp
    * Documentação Do Projeto De Gestão E Governança De Dados
    * Gestão Evolutiva Do Projeto
* 0.4.0 - 30/03/2025
    * Implementação do pipeline na nuvem
    * Documentação do projeto de gestão de governança de dados
    * Dataapp (1° Versão)
    * Gestão evolutiva do projeto 

## Sumário

1. [Introdução](#introdução)
2. [Métrica de Planejamento](#Métrica-de-Planejamento)
3. [Documentação das Métricas da Sprint 1](#documentação-das-métricas-da-sprint-1)  
   - [Visão Geral da Sprint](#visão-geral-da-sprint)  
   - [Análise do Burndown Chart](#análise-do-burndown-chart)  
   - [Desenvolvimento das Tasks ao Longo da Sprint](#desenvolvimento-das-tasks-ao-longo-da-sprint)  
   - [Revisão e Finalização](#revisão-e-finalização)  
   - [Conclusão](#conclusão)  
4. [Planejamento da Sprint 2](#planejamento-sprint-2)  
   - [Backlog do Projeto de Gestão e Governança de Dados](#backlog-do-projeto-de-gestão-e-governança-de-dados)  
   - [Revisão e Atualização do Backlog](#revisão-e-atualização-do-backlog-sprint-2)  
     - [Features Atualizadas](#features-atualizadas)  
     - [User Stories Atualizadas](#user-stories-atualizadas)  
     - [Tasks Atualizadas](#tasks-atualizadas)  
   - [Medição de Métricas de Desempenho](#medição-de-métricas-de-desempenho)  
     - [Throughput](#throughput)  
     - [Cycle Time](#cycle-time)  
     - [Burndown](#burndown)  
5. [Planejamento da Sprint 3](#planejamento-da-sprint-3)  
   - [Definição de Tasks](#definição-de-tasks)  
   - [Priorização e Sequenciamento](#priorização-e-sequenciamento)  
   - [Distribuição dos Pontos na Sprint 3](#Distribuição-dos-Pontos-na-Sprint-3)
   - [Revisão e Atualização do Backlog Sprint 3](#Revisão-e-Atualização-do-Backlog-Sprint-3)
   - [Medição de Métricas de Desempenho - Sprint 3](#Medição-de-Métricas-de-Desempenho-Sprint-3)
     - [Throughput Sprint 3](#throughput-Sprint-3)  
     - [Cycle Time Sprint 3](#cycle-timeSprint-3)  
     - [Burndown Sprint 3](#burndownSprint-3) 
6. [Planejamento da Sprint 4](#planejamento-sprint-4)
   - [Definição de Tasks](#definição-de-tasks-2) 
   - [Distribuição dos Pontos na Sprint 4](#Distribuição-dos-Pontos-na-Sprint-4)
   - [Revisão e Atualização do Backlog Sprint 4](#Revisão-e-Atualização-do-Backlog-Sprint-4)
   - [Considerações sobre Riscos e Ajustes](#Considerações-sobre-Riscos-e-Ajustes)
   - [Medição de Métricas de Desempenho Sprint 4](#Medição-de-Métricas-de-Desempenho-Sprint-4)
7. [Planejamento Sprint 5](#Planejamento-Sprint-5)
   - [Definição de Tasks 5](#Definição-de-Tasks-5)
   - [Distribuição de Pontos na Sprint 5](#Distribuição-de-Pontos-na-Sprint-5)
   - [Considerações sobre Riscos e Ajustes](#Considerações-sobre-Riscos-e-Ajustes-Sprint-5)
   - [Justificativa da Priorização das Tasks da Sprint 5](#Justificativa-da-Priorização-das-Tasks-da-Sprint-5)
   - [Medição de Métricas de Desempenho Sprint 5](#Medição-de-Métricas-de-Desempenho-Sprint-5)
     - [Throughput da Sprint 5](#Throughput-da-Sprint-5)
     - [Burndown Chart da Sprint 5](#Burndown-Chart-da-Sprint-5)
8. [Análise Evolutiva das Métricas de Desempenho](#Análise-Evolutiva-das-Métricas-de-Desempenho)
9. [Conclusões Gerais sobre Sprints](#Conclusões-Gerais-sobre-Sprints)
10. [Uso das Políticas de Gestão de Configuração](#uso-das-políticas-de-gestão-de-configuração)  
   - [Esteira de CI](#Esteira-de-CI)
11. [Feedback](#Feedback)

---

## Introdução

Esta documentação detalha a gestão evolutiva do projeto, incluindo a revisão e atualização do backlog, a medição de métricas de desempenho de cada sprint e o planejamento para a próxima sprint. O objetivo é garantir transparência e controle sobre o progresso das entregas, alinhando as necessidades do projeto às melhores práticas de governança de dados.


# **Métrica de Planejamento**

Para a estimativa de esforço das tasks, utilizamos a métrica **Fibonacci**, que permite uma diferenciação mais granular entre o nível de complexidade das tarefas. Os pontos foram atribuídos com base nos seguintes critérios:

| **Pontuação (Fibonacci)** | **Esforço Estimado** |
|-----------------|------------------|
| 1 | Task muito simples (exemplo: ajuste de documentação) |
| 2 | Task pequena, mas com alguma complexidade (exemplo: refinamento de um modelo de dados) |
| 3 | Task de dificuldade moderada (exemplo: implementação de uma regra de transformação de dados) |
| 5 | Task mais complexa (exemplo: integração entre sistemas com API) |
| 8 | Task de alta complexidade e dependências (exemplo: implementação de auditoria automatizada) |
| 13 | Task extremamente complexa, que pode precisar ser quebrada em subtarefas (exemplo: desenvolvimento de um pipeline de deploy contínuo) |
---

## **Justificativa para Escolha da Métrica**
Optamos pela **Escala de Fibonacci** devido à sua capacidade de refletir diferenças significativas na complexidade das tarefas, ajudando na previsão de esforço e tempo necessário para conclusão. Isso também facilita a priorização e alocação eficiente de recursos dentro da equipe.

---

# Documentação das Métricas da Sprint 1

## Visão Geral da Sprint
Nesta sprint, tivemos um total de **56 tasks**, distribuídas em uma média de **9 tasks por membro**. Com a análise das métricas, conseguimos identificar alguns padrões que impactaram diretamente o andamento da sprint.

### Análise do Burndown Chart
<img width="392" alt="IMAGEM 1" src="https://github.com/user-attachments/assets/e07c0628-fd7c-4bd9-b0c3-bf0d42b019af" />

Ao longo da sprint, observamos que, em determinado momento, o progresso não seguiu o ritmo ideal. No ponto em que deveríamos ter cerca de **44,8 tasks restantes**, ainda estávamos com as **56 tasks** iniciais. Esse atraso indica que o tempo reservado para o desenvolvimento das tarefas não foi aproveitado da melhor forma no início.

Nos dias seguintes, o fluxo de trabalho se normalizou, e a equipe conseguiu reduzir progressivamente o número de tasks pendentes, seguindo uma cadência mais equilibrada.

### Desenvolvimento das Tasks ao Longo da Sprint
<img width="396" alt="imagem 2" src="https://github.com/user-attachments/assets/4ca4f872-1485-4da7-a7a3-dc133c674f78" />
<img width="397" alt="imagem 3" src="https://github.com/user-attachments/assets/fb8ab431-521f-4191-9e5e-3dabe8ed12c6" />
<img width="396" alt="imagem 4" src="https://github.com/user-attachments/assets/6fe8ff71-0f40-4988-a90e-086c2783a212" />
<img width="395" alt="imagem 5" src="https://github.com/user-attachments/assets/534d5ebe-64d3-4262-8cca-755f19fd3824" />

No final da sprint, houve um aumento no tempo em que algumas tasks ficaram paradas. Esse período coincidiu com a **fase de revisão e alinhamento**, onde as tarefas já finalizadas passaram por ajustes e validações internas antes do encerramento da sprint.

### Revisão e Finalização
<img width="394" alt="imagem 6" src="https://github.com/user-attachments/assets/84be2bf9-5f5b-4972-8752-b5496d693935" />
<img width="394" alt="imagem 7" src="https://github.com/user-attachments/assets/48e24c04-db58-4943-bc58-8a238f7dbc86" />

Apesar dos desafios iniciais e dos momentos de desaceleração, conseguimos concluir **todas as 56 tasks planejadas**, garantindo que os objetivos da sprint fossem atingidos.

### Conclusão
<img width="395" alt="imagem 8" src="https://github.com/user-attachments/assets/7fb80e81-844b-49a6-b64a-b08e537d58ad" />

Durante a sprint, percebemos alguns pontos que podem ser melhorados na distribuição das atividades. Com pequenos ajustes no planejamento e uma divisão mais equilibrada do esforço, dá para evitar períodos de acúmulo no futuro. Mesmo assim, mantivemos um bom ritmo, entregamos todas as tarefas dentro do prazo e soubemos nos adaptar bem aos desafios ao longo do processo.

# Planejamento Sprint 2:

### **Backlog do Projeto de Gestão e Governança de Dados**

#### **Épico 1: Arquitetura de Dados e Governança**

**User Story 1.1**: Como arquiteto de dados, quero visualizar o fluxo de dados do sistema para garantir um entendimento claro do percurso das informações.

- **Task 1.1.1**: Criar diagramas de fluxo de dados.
  - Esboçar a estrutura inicial dos diagramas.
  - Revisar com a equipe para feedback.
  - Ajustar os detalhes dos fluxos conforme feedback.
  - Criar versão final para documentação.
  - **Documentação**: Incluir os diagramas gerados no documento `Projeto_Gestao_Governanca_Dados.md`.
  - **Critérios de Qualidade**: Os diagramas devem cobrir detalhadamente o percurso dos dados e estar integrados com a arquitetura geral.

- **Task 1.1.2**: Documentar entradas e saídas dos processos.
  - Identificar os principais processos envolvidos.
  - Definir entradas e saídas de cada processo.
  - Elaborar documentação estruturada.
  - Validar a documentação com stakeholders.
  - **Documentação**: A documentação deverá ser clara e concisa, com foco nos processos de entrada e saída.

---

**User Story 1.2**: Como analista de dados, quero acessar um modelo de dados detalhado para compreender os relacionamentos entre os elementos.

- **Task 1.2.1**: Identificar e documentar os elementos do modelo.
  - Levantar requisitos de modelagem.
  - Identificar entidades principais.
  - Documentar os atributos de cada entidade.
  - Criar documentação para revisão.
  - **Critérios de Qualidade**: Os elementos devem estar bem descritos, com foco nas entidades e seus atributos. A modelagem deve ser documentada de forma clara.

- **Task 1.2.2**: Mapear relacionamentos entre os elementos.
  - Definir chaves primárias e estrangeiras.
  - Criar diagramas relacionais.
  - Revisar modelagem com a equipe.
  - Ajustar conforme feedbacks recebidos.
  - **Documentação**: Os relacionamentos devem estar claramente mapeados e documentados no arquivo `Projeto_Gestao_Governanca_Dados.md`.

---

**User Story 1.3**: Como responsável pela segurança, quero um plano de governança de dados para garantir conformidade com padrões de segurança.

- **Task 1.3.1**: Definir estratégias de criptografia e controle de acesso.
  - Identificar dados sensíveis.
  - Selecionar mecanismos de criptografia.
  - Implementar testes de acesso.
  - Criar documentação do plano de segurança.
  - **Critérios de Qualidade**: As estratégias de segurança devem ser claras, com explicações detalhadas sobre criptografia e controle de acesso.

- **Task 1.3.2**: Criar plano de mitigação de riscos.
  - Mapear riscos potenciais.
  - Elaborar estratégias de mitigação.
  - Definir plano de contingência.
  - Apresentar plano à equipe para validação.
  - **Documentação**: O plano de mitigação deve ser documentado, incluindo as estratégias e ações de contingência.

---

#### **Épico 2: Módulo de Ingestão e Processamento de Dados**

**User Story 2.1**: Como engenheiro de dados, quero um pipeline eficiente para ingestão de dados para garantir a integridade dos dados extraídos.

- **Task 2.1.1**: Implementar pipeline de ingestão de dados.
  - Definir arquitetura do pipeline.
  - Configurar ambiente de ingestão.
  - Implementar scripts de coleta de dados.
  - Validar pipeline com dados reais.
  - **Critérios de Qualidade**: O pipeline deve ser otimizado para ingestão eficiente, com validação em dados reais para garantir a integridade.

- **Task 2.1.2**: Validar a cobertura dos dados fonte.
  - Identificar fontes de dados críticas.
  - Criar métricas de qualidade dos dados.
  - Executar testes de cobertura.
  - Ajustar pipeline conforme necessidade.
  - **Documentação**: Os testes de cobertura e métricas de qualidade devem ser documentados.

---

**User Story 2.2**: Como cientista de dados, quero importar dados de diferentes formatos para ter maior flexibilidade na análise.

- **Task 2.2.1**: Implementar suporte a CSV, JSON, XML e outros formatos.
  - Criar função para leitura de CSV.
  - Implementar suporte a JSON e XML.
  - Testar compatibilidade com diferentes formatos.
  - Ajustar funções conforme necessidade.
  - **Critérios de Qualidade**: A funcionalidade de importação deve ser robusta e testar diversos formatos de dados.

- **Task 2.2.2**: Testar e documentar a compatibilidade.
  - Definir cenários de teste para cada formato.
  - Executar testes de leitura e escrita.
  - Corrigir falhas identificadas.
  - Criar documentação para referência futura.
  - **Documentação**: Documentar todos os testes realizados e as correções implementadas.

---

**User Story 2.3**: Como engenheiro de dados, quero definir regras de transformação para garantir que os dados estejam no formato correto para análise.

- **Task 2.3.1**: Definir e implementar regras de transformação de dados.
  - Mapear transformações necessárias.
  - Implementar regras de normalização.
  - Aplicar validação automatizada.
  - Testar transformações em conjunto.
  - **Critérios de Qualidade**: As transformações devem ser bem definidas e aplicadas de forma eficiente.

- **Task 2.3.2**: Criar auditoria para validação das transformações.
  - Definir requisitos de auditoria.
  - Implementar logging detalhado.
  - Criar alertas para erros críticos.
  - Testar auditoria com diferentes cenários.
  - **Documentação**: A auditoria deve ser documentada e os logs de erro registrados.

---

#### **Épico 3: Gestão Evolutiva do Projeto (GEP)**

**User Story 3.1**: Como gestor do projeto, quero atualizar o backlog para refletir as mudanças da sprint anterior.

- **Task 3.1.1**: Revisar backlog e atualizar features e user stories.
  - Reavaliar prioridades e atualizar o backlog conforme feedbacks recebidos.
  - **Documentação**: O backlog atualizado deve ser documentado de forma clara e disponibilizado no repositório.

- **Task 3.1.2**: Priorizar backlog conforme a necessidade do projeto.
  - Definir prioridades com base na capacidade do time e objetivos do projeto.
  - **Critérios de Qualidade**: O backlog deve refletir as prioridades e objetivos do projeto de maneira clara.

---

**User Story 3.2**: Como stakeholder, quero visualizar o desempenho da equipe para avaliar a evolução do projeto.

- **Task 3.2.1**: Medir throughput e cycle time.
  - Analisar os dados de desempenho da equipe para melhorar o planejamento das próximas sprints.
  - **Documentação**: Incluir métricas de throughput e cycle time no documento `GestaoProjeto.md`.

- **Task 3.2.2**: Atualizar burndown chart.
  - Gerar gráficos atualizados de progresso da sprint para acompanhamento do desempenho.
  - **Critérios de Qualidade**: O gráfico deve ser atualizado e representar de maneira precisa o progresso da sprint.

---

**User Story 3.3**: Como PO, quero definir o planejamento da Sprint 3 para garantir que o time execute as prioridades.

- **Task 3.3.1**: Definir e priorizar as tasks da Sprint 3.
  - Criar um plano detalhado considerando a capacidade da equipe e a estratégia do projeto.
  - **Documentação**: O plano de Sprint 3 deve ser documentado no `GestaoProjeto.md` e compartilhado com a equipe.

- **Task 3.3.2**: Documentar planejamento no GestaoProjeto.md.
  - Atualizar a documentação com o plano revisado da sprint.
  - **Documentação**: O documento atualizado deve refletir a priorização e planejamento da Sprint 3.

---

### Revisão e Atualização do Backlog Sprint 2

Nesta seção, revisamos as features, user stories e tasks para refletir as atualizações e feedbacks da Sprint 2.

#### Features Atualizadas

1. **Arquitetura de Dados e Governança**
2. **Módulo de Ingestão e Processamento de Dados**
3. **Gestão Evolutiva do Projeto (GEP)**

#### User Stories Atualizadas

1. **Como arquiteto de dados**, quero visualizar o fluxo de dados do sistema para garantir um entendimento claro do percurso das informações.
2. **Como analista de dados**, quero acessar um modelo de dados detalhado para compreender os relacionamentos entre os elementos.
3. **Como responsável pela segurança**, quero um plano de governança de dados para garantir conformidade com padrões de segurança.
4. **Como engenheiro de dados**, quero um pipeline eficiente para ingestão de dados para garantir a integridade dos dados extraídos.
5. **Como cientista de dados**, quero importar dados de diferentes formatos para ter maior flexibilidade na análise.
6. **Como gestor do projeto**, quero atualizar o backlog para refletir as mudanças da sprint anterior.

#### Tasks Atualizadas

As tasks foram organizadas e priorizadas dentro de cada épico para garantir um fluxo eficiente.

1. Criar diagramas de fluxo de dados.
2. Documentar entradas e saídas dos processos.
3. Implementar pipeline de ingestão de dados.
4. Definir e implementar regras de transformação de dados.
5. Criar auditoria para validação das transformações.
6. Medir throughput e cycle time.
7. Atualizar burndown chart.
8. Definir e priorizar as tasks da Sprint 3.

---

### Medição de Métricas de Desempenho

A medição das métricas de desempenho foi realizada considerando as user stories e tasks concluídas durante a Sprint 2.

#### Throughput

- 7 user stories concluídas
- 12 tasks finalizadas
- Velocidade: 18 story points por sprint

#### Cycle Time

- Média de 1 a 2 tasks por dia
- Task mais longa: Implementação do pipeline de ingestão (9 dias)
- Task mais rápida: Atualização do backlog (6 horas)

#### Burndown

- 85% das tasks planejadas concluídas
- Recuperação do ritmo na segunda metade da sprint

---

## Planejamento da Sprint 3

### Definição de Tasks

1. **Refinamento do Modelo de Dados (8 pontos)**
   - Revisão de entidades e atributos
   - Ajuste dos relacionamentos conforme feedback
   - Documentação final do modelo

2. **Implementação de Políticas de Segurança (13 pontos)**
   - Definição de perfis de acesso
   - Configuração de criptografia de dados
   - Testes de segurança

3. **Aprimoramento do Pipeline ETL (8 pontos)**
   - Otimização de transformações
   - Implementação de auditoria automatizada
   - Testes de performance

### Priorização e Sequenciamento

1. **Alta Prioridade (Semana 1)**
   - Refinamento do Modelo de Dados
   - Implementação de Políticas de Segurança

2. **Média Prioridade (Semana 2)**
   - Aprimoramento do Pipeline ETL
   - Refatoração do Wireframe

3. **Baixa Prioridade (Paralelo)**
   - Revisão e otimização da documentação

Estimativa Total: 29 pontos

---

# Planejamento Sprint 3:

### Definição de Tasks 

#### **Épico 1: Arquitetura de Integração e Governança de Dados**

**User Story 1.1**: Como arquiteto de dados, quero integrar diferentes sistemas para garantir uma comunicação eficiente entre as plataformas.

- **Task 1.1.1**: Desenvolver API de integração entre sistemas.
  - Definir a arquitetura da API de integração.
  - Criar endpoints para comunicação entre os sistemas.
  - Implementar a segurança da API.
  - Realizar testes de integração.
  - **Critérios de Qualidade**: A API deve ser segura, eficiente e escalável. Todos os endpoints devem ser testados em diferentes cenários de comunicação.

- **Task 1.1.2**: Documentar a integração de sistemas.
  - Detalhar o fluxo de dados entre os sistemas.
  - Criar diagramas de arquitetura da API.
  - Incluir detalhes sobre segurança e autenticação.
  - **Documentação**: A documentação deve ser clara e completa, refletindo o fluxo de dados e a comunicação entre os sistemas no arquivo `Projeto_Gestao_Governanca_Dados.md`.

---

**User Story 1.2**: Como analista de dados, quero garantir que os dados de diferentes fontes sejam extraídos e integrados de maneira eficiente.

- **Task 1.2.1**: Implementar pipeline de ingestão de dados.
  - Definir arquitetura do pipeline.
  - Configurar ambientes de ingestão de dados.
  - Criar scripts de ingestão para diferentes fontes.
  - Realizar testes com dados reais.
  - **Critérios de Qualidade**: O pipeline deve ser eficiente, com validação de dados e monitoração contínua da ingestão.

- **Task 1.2.2**: Criar auditoria de ingestão e validação de dados.
  - Implementar logs para rastrear a ingestão de dados.
  - Configurar alertas para falhas no processo de ingestão.
  - Validar dados e garantir que não haja perda ou corrupção.
  - **Documentação**: Documentar o processo de ingestão, incluindo os logs e alertas, no arquivo `Projeto_Gestao_Governanca_Dados.md`.

---

#### **Épico 2: Automação e Monitoramento de Pipelines**

**User Story 2.1**: Como engenheiro de dados, quero automatizar o pipeline de deploy para garantir a entrega contínua de atualizações.

- **Task 2.1.1**: Implementar pipeline de deploy contínuo.
  - Definir o fluxo de automação do deploy.
  - Integrar ferramentas de CI/CD (como Jenkins ou GitLab CI).
  - Testar a automação com diferentes versões de código.
  - **Critérios de Qualidade**: O pipeline deve garantir que os deploys sejam rápidos e seguros, com rollback automático em caso de falha.

- **Task 2.1.2**: Documentar o pipeline de deploy.
  - Criar documentação detalhada sobre o fluxo de deploy.
  - Incluir detalhes sobre testes e validação automática.
  - **Documentação**: O pipeline de deploy deve ser completamente documentado no arquivo `Projeto_Gestao_Governanca_Dados.md`.

---

**User Story 2.2**: Como responsável pela segurança, quero garantir que as atualizações sejam seguras e não comprometam a integridade dos dados.

- **Task 2.2.1**: Implementar segurança no pipeline de deploy.
  - Integrar ferramentas de segurança como Snyk ou WhiteSource.
  - Configurar monitoramento de vulnerabilidades em tempo real.
  - Validar código e dependências antes do deploy.
  - **Critérios de Qualidade**: O pipeline deve garantir que não haja vulnerabilidades de segurança durante o processo de deploy.

- **Task 2.2.2**: Monitorar e auditar a segurança dos deploys.
  - Implementar logs detalhados de auditoria.
  - Criar alertas para detecção de atividades suspeitas.
  - Validar todas as implementações e atualizações com testes de segurança.
  - **Documentação**: Documentar a estratégia de segurança e os processos de auditoria no arquivo `Projeto_Gestao_Governanca_Dados.md`.

---

#### **Épico 3: Governança de Dados e Qualidade**

**User Story 3.1**: Como responsável pela governança, quero garantir que as práticas de governança de dados estejam bem documentadas e implementadas.

- **Task 3.1.1**: Criar diretrizes de governança de dados.
  - Definir políticas de governança (acesso, segurança, compliance).
  - Implementar controles de qualidade e segurança.
  - Validar com stakeholders as políticas implementadas.
  - **Critérios de Qualidade**: As diretrizes de governança devem ser claras e alinhadas aos objetivos do projeto e às normas de segurança.

- **Task 3.1.2**: Documentar as políticas de governança de dados.
  - Elaborar um documento completo sobre as políticas de governança.
  - Incluir exemplos de boas práticas e como aplicá-las.
  - **Documentação**: A documentação deve ser bem estruturada e incluir detalhes das políticas de governança no arquivo `Projeto_Gestao_Governanca_Dados.md`.

---

**User Story 3.2**: Como analista de dados, quero garantir que os dados estejam de acordo com as normas de qualidade definidas pelo projeto.

- **Task 3.2.1**: Definir regras de qualidade dos dados.
  - Estabelecer critérios de precisão, completude e consistência.
  - Criar métricas e indicadores de qualidade dos dados.
  - Realizar testes de qualidade em amostras de dados.
  - **Critérios de Qualidade**: As regras de qualidade devem ser claras e aplicáveis a todos os dados do projeto.

- **Task 3.2.2**: Implementar monitoramento da qualidade dos dados.
  - Configurar monitoramento contínuo dos dados.
  - Implementar alertas para dados fora dos padrões de qualidade.
  - Realizar auditorias periódicas nos dados.
  - **Documentação**: A documentação do processo de qualidade de dados deve ser clara, incluindo os critérios de qualidade e os indicadores utilizados.

---

#### **Épico 4: Planejamento e Gestão do Projeto**

**User Story 4.1**: Como PO, quero definir o planejamento da Sprint 3 para garantir que o time execute as prioridades do projeto.

- **Task 4.1.1**: Criar plano detalhado para Sprint 3.
  - Definir as tasks e os recursos necessários.
  - Estabelecer prazos e marcos de entrega.
  - Validar o plano com a equipe e stakeholders.
  - **Documentação**: O plano de Sprint 3 deve ser documentado no arquivo `GestaoProjeto.md` e compartilhado com todos os envolvidos.

- **Task 4.1.2**: Priorizar backlog para a Sprint 3.
  - Definir as features e user stories prioritárias para a Sprint.
  - Validar a priorização com a equipe de desenvolvimento.
  - **Critérios de Qualidade**: A priorização deve refletir as necessidades do projeto e as capacidades da equipe.

---

**User Story 4.2**: Como gestor do projeto, quero acompanhar o progresso da Sprint 3 por meio de métricas e relatórios.

- **Task 4.2.1**: Acompanhar métricas de desempenho da equipe.
  - Medir throughput, cycle time e burndown da Sprint 3.
  - Identificar áreas de melhoria com base nas métricas.
  - **Documentação**: As métricas de desempenho devem ser documentadas no `GestaoProjeto.md` para acompanhamento contínuo.

- **Task 4.2.2**: Atualizar relatórios de progresso.
  - Criar gráficos atualizados de progresso.
  - Compartilhar os relatórios com stakeholders.
  - **Critérios de Qualidade**: O relatório de progresso deve ser claro e fornecer uma visão precisa da evolução da Sprint

### **Distribuição dos Pontos na Sprint 3**

Com base na métrica de finonacci, a atribuição de pontos para cada task da Sprint 3 foi realizada da seguinte forma:

| **Task** | **Estimativa (Fibonacci)** |
|-----------------|------------------|
| Refinamento do Modelo de Dados | 5 |
| Implementação de Políticas de Segurança | 8 |
| Aprimoramento do Pipeline ETL | 5 |
| Implementação de Auditoria para Validação das Transformações | 3 |
| Criação de Diretrizes de Governança de Dados | 5 |
| Implementação de Segurança no Pipeline de Deploy | 8 |
| Monitoramento e Auditoria dos Deploys | 5 |
| Atualização do Backlog para a Sprint 3 | 2 |
| Medição de Throughput e Cycle Time | 3 |
| Atualização do Burndown Chart | 2 |

Total estimado: **46 pontos**

### Revisão e Atualização do Backlog Sprint 3

Nesta seção, revisamos as features, user stories e tasks para refletir as atualizações e feedbacks da Sprint 2.

#### Features Atualizadas

1. **Arquitetura de Integração e Governança de Dados**

2. **Automação e Monitoramento de Pipelines**

3. **Governança de Dados e Qualidade**

4. **Planejamento e Gestão do Projeto**

#### User Stories Atualizadas

1. **Como arquiteto de dados**, quero integrar diferentes sistemas para garantir uma comunicação eficiente entre as plataformas.

2. **Como analista de dados**, quero garantir que os dados de diferentes fontes sejam extraídos e integrados de maneira eficiente.

3. **Como engenheiro de dados**, quero automatizar o pipeline de deploy para garantir a entrega contínua de atualizações.

4. **Como responsável pela segurança**, quero garantir que as atualizações sejam seguras e não comprometam a integridade dos dados.

5. **Como responsável pela governança**, quero garantir que as práticas de governança de dados estejam bem documentadas e implementadas.

6. **Como analista de dados**, quero garantir que os dados estejam de acordo com as normas de qualidade definidas pelo projeto.

7. **Como PO**, quero definir o planejamento da Sprint 3 para garantir que o time execute as prioridades do projeto.

8. **Como gestor do projeto**, quero acompanhar o progresso da Sprint 3 por meio de métricas e relatórios.

#### Tasks Atualizadas

As tasks foram organizadas e priorizadas dentro de cada épico para garantir um fluxo eficiente e uma transição adequada para a Sprint 4.

1. Desenvolver API de integração entre sistemas.

2. Documentar a integração de sistemas.

3. Implementar pipeline de ingestão de dados.

4. Criar auditoria de ingestão e validação de dados.

5. Implementar pipeline de deploy contínuo.

6. Documentar o pipeline de deploy.

7. Implementar segurança no pipeline de deploy.

8. Monitorar e auditar a segurança dos deploys.

9. Criar diretrizes de governança de dados.

10. Documentar as políticas de governança de dados.

11. Definir regras de qualidade dos dados.

12. Implementar monitoramento da qualidade dos dados.

13. Priorizar backlog para a Sprint 4.

14. Acompanhar métricas de desempenho da equipe.

15. Atualizar relatórios de progresso.

### **Medição de Métricas de Desempenho Sprint 3**

A medição das métricas de desempenho foi realizada considerando as user stories e tasks concluídas durante a Sprint 3.

#### **Throughput Sprint 3**

- **User stories concluídas:** 8
- **Tasks finalizadas:** 14
- **Velocidade da sprint:** 20 story points
- **Método de coleta:** O throughput foi medido utilizando o Trello, analisando o número de cards movidos para a coluna "Concluído" ao longo da sprint.

#### **Cycle Time Sprint 3**

- **Média de tasks concluídas por dia:** 1 a 3
- **Task mais longa:** Implementar pipeline de ingestão de dados (5 dias)
- **Task mais rápida:** Priorizar backlog para a Sprint 3 (3 horas)
- **Método de coleta:** O cycle time foi calculado monitorando o tempo que cada card permaneceu em progresso antes de ser movido para "Concluído" no Trello.

#### **Burndown Sprint 3**

- **Percentual de tasks concluídas:** 90%
- **Padrão observado:** Manutenção de ritmo constante ao longo da sprint
- **Método de coleta:** O burndown foi gerado manualmente com base na movimentação de tarefas no Trello e na avaliação diária da equipe.

# Planejamento Sprint 4

### Definição de Tasks

#### **Épico 1: Desenvolvimento da Versão Preliminar do DataApp**

**User Story 1.1: Como usuário, quero que o DataApp reflita os elementos principais do wireframe para garantir uma interface intuitiva.**

- Task 1.1.1: Criar estrutura base do DataApp usando Streamlit.
 - Configurar ambiente de desenvolvimento.
 - Criar a estrutura inicial do projeto.
 - Critérios de Qualidade: A estrutura deve seguir as boas práticas de organização de código.

- Task 1.1.2: Implementar navegação entre telas conforme wireframe.
 - Criar sistema de roteamento para as páginas do DataApp.
 - Testar a navegação entre as telas.
 - **Critérios de Qualidade:** As transições devem ser suaves e funcionais.

**User Story 1.2: Como usuário, quero visualizar gráficos interativos para análise de dados de governança.**

- Task 1.2.1: Escolher biblioteca para visualização de gráficos.
 - Pesquisar e comparar bibliotecas adequadas.
 - Escolher a biblioteca que melhor atende aos requisitos.
 - Critérios de Qualidade: A biblioteca deve oferecer interatividade e boa performance.

- Task 1.2.2: Implementar gráfico de linha para análise temporal.
 - Criar um gráfico de linha baseado nos dados mockados.
 - Garantir interatividade com zoom e filtros.
 - **Critérios de Qualidade:** O gráfico deve ser responsivo e legível.

#### **Épico 2: Implantação do Pipeline de Dados**

**User Story 2.1: Como desenvolvedor, preciso configurar um ambiente otimizado para hospedar o DataApp com eficiência e segurança.**

- Task 2.1.1: Criar instância na nuvem para hospedagem do DataApp.
 - Configurar servidor na plataforma escolhida.
 - Ajustar recursos de CPU e memória conforme necessidade.
 - Critérios de Qualidade: O ambiente deve estar acessível e estável.

Task 2.1.2: Configurar regras de segurança para acesso ao ambiente.
 - Definir permissões para usuários.
 - Implementar autenticação e criptografia.
 - **Critérios de Qualidade:** A configuração deve garantir segurança e conformidade com normas.

**User Story 2.2: Como desenvolvedor, preciso criar um pipeline para ingestão, processamento e armazenamento dos dados.**

- Task 2.2.1: Criar fluxo de coleta de dados brutos.
 - Definir fontes de dados e frequência de coleta.
 - Implementar o processo de extração de dados.
 - **Critérios de Qualidade:** A coleta deve ser confiável e escalável.

- Task 2.2.2: Implementar transformações nos dados.
 - Definir regras de limpeza e normalização.
 - Criar processos de transformação automatizados.
 - **Critérios de Qualidade:** Os dados devem ser padronizados e prontos para uso.

#### **Épico 3: Metrificação do Projeto de Gestão e Governança de Dados**

**User Story 3.1: Como gestor, quero que a documentação demonstre claramente o alinhamento do projeto com os objetivos estratégicos.**

- Task 3.1.1: Estruturar documento com seções de alinhamento estratégico.
 - Criar seções específicas para cada aspecto do projeto.
 - Relacionar objetivos estratégicos com as soluções implementadas.
 - **Documentação:** O documento deve ser armazenado no Projeto_Gestao_Governanca_Dados.md.

- Task 3.1.2: Redigir seção sobre auditoria de governança de dados.
 - Explicar processos de auditoria e conformidade.
 - Incluir métricas e indicadores de governança.
 - **Critérios de Qualidade:** A seção deve estar alinhada com práticas do mercado.

**User Story 3.2: Como analista de dados, quero garantir que os dados estejam de acordo com as normas de qualidade definidas pelo projeto.**

- Task 3.2.1: Definir regras de qualidade dos dados.
 - Estabelecer critérios de precisão, completude e consistência.
 - Criar métricas e indicadores de qualidade dos dados.
 - **Critérios de Qualidade:** As regras devem ser claras e aplicáveis a todos os dados do projeto.

- Task 3.2.2: Implementar monitoramento da qualidade dos dados.
 - Configurar monitoramento contínuo dos dados.
 - Implementar alertas para dados fora dos padrões de qualidade.
 - **Documentação:** A documentação do processo de qualidade de dados deve ser clara e incluir os critérios definidos.

#### **Épico 4: Gestão Evolutiva do Projeto**

**User Story 4.1: Como PO, quero definir o planejamento da Sprint 5 para garantir que o time execute as prioridades do projeto.**

- Task 4.1.1: Criar plano detalhado para Sprint 5.
 - Definir as tasks e os recursos necessários.
 - Estabelecer prazos e marcos de entrega.
 - **Documentação:** O plano deve ser documentado no GestaoProjeto.md.

- Task 4.1.2: Priorizar backlog para a Sprint 5.
 - Definir as features e user stories prioritárias para a Sprint.
 - Validar a priorização com a equipe de desenvolvimento.
 - **Critérios de Qualidade:** A priorização deve refletir as necessidades do projeto e a capacidade da equipe.

**User Story 4.2: Como gestor, preciso garantir que o projeto siga as diretrizes definidas para configuração e versionamento.**

- Task 4.2.1: Aplicar versionamento correto no repositório do projeto.
 - Criar tags e releases para controle de versão.
 - Garantir que a estrutura do repositório siga as boas práticas.
 - **Critérios de Qualidade:** O versionamento deve ser consistente e documentado.

- Task 4.2.2: Configurar ferramenta de CI/CD para automação do deploy.
 - Escolher a ferramenta mais adequada para integração contínua.
 - Implementar pipeline de build e deploy automatizado.
 - **Critérios de Qualidade:** O deploy deve ser eficiente e seguro.

### **Distribuição dos Pontos na Sprint 4**

Com base na métrica de Fibonacci, a atribuição de pontos para cada task da Sprint 4 foi realizada da seguinte forma:

| **Task** | **Estimativa (Fibonacci)** |
|-----------------|------------------|
| Criar estrutura base do DataApp usando Streamlit | 5 |
| Implementar navegação entre telas conforme wireframe | 5 |
| Escolher biblioteca para visualização de gráficos | 3 |
| Implementar gráfico de linha para análise temporal | 5 |
| Criar instância na nuvem para hospedagem do DataApp | 8 |
| Configurar regras de segurança para acesso ao ambiente | 8 |
| Criar fluxo de coleta de dados brutos | 5 |
| Implementar transformações nos dados | 5 |
| Estruturar documento com seções de alinhamento estratégico | 3 |
| Redigir seção sobre auditoria de governança de dados | 5 |
| Definir regras de qualidade dos dados | 5 |
| Implementar monitoramento da qualidade dos dados | 8 |
| Criar plano detalhado para Sprint 5 | 2 |
| Priorizar backlog para a Sprint 5 | 2 |
| Aplicar versionamento correto no repositório do projeto | 3 |
| Configurar ferramenta de CI/CD para automação do deploy | 5 |

**Total estimado: 72 pontos**

### **Revisão e Atualização do Backlog Sprint 4**

Nesta etapa, foram feitas **revisões estruturais no backlog** com base nos feedbacks obtidos durante as sprints anteriores, visando garantir a **entrega integral do produto na Sprint 5**. O foco foi alinhar completamente o backlog com os objetivos finais do projeto e garantir que todos os critérios de qualidade e governança fossem contemplados.

#### **Features Atualizadas**

1. **DataApp Integrado com Segurança e Usabilidade**
   - Reflete a necessidade de entrega de um produto funcional e acessível, com login seguro, visualizações coerentes com a análise exploratória e uma arquitetura de 3 camadas.

2. **Governança de Dados e Qualidade**
   - Expandida para incorporar regras claras de qualidade de dados, métricas e monitoramento contínuo, respondendo diretamente aos apontamentos sobre a ausência de validação contínua e detalhamento técnico.

3. **Pipeline de Processamento e Deploy com CI/CD**
   - Aprimorada para incluir o detalhamento do processo de integração contínua, testes automatizados e versionamento, conforme sugerido nos feedbacks.

4. **Gestão Evolutiva e Métricas de Desempenho**
   - Atualizada para registrar as decisões tomadas ao longo do projeto, bem como expandir a análise de throughput, burndown e cycle time com explicações metodológicas mais robustas.

5. **Documentação Técnica e Análise de Impacto**
   - Refinada para incorporar explicações mais completas sobre a cobertura de testes, uso de ferramentas como `pytest-cov`, e como os feedbacks foram incorporados sprint a sprint.

#### **User Stories Refinadas**

1. **Como usuário**, desejo utilizar o DataApp com autenticação e navegação intuitiva para acessar as visualizações e análises com segurança.

2. **Como engenheiro de dados**, preciso de um pipeline de ingestão e processamento confiável, documentado e validado com testes automatizados.

3. **Como responsável pela governança**, quero regras claras e monitoramento ativo da qualidade dos dados para garantir conformidade com padrões.

4. **Como stakeholder**, desejo consultar uma documentação clara, com histórico de versões e alinhamento com os critérios de qualidade definidos no início do projeto.

5. **Como PO**, desejo acompanhar a evolução do projeto por meio de métricas confiáveis e justificativas completas sobre priorizações e riscos assumidos.

#### **Atualizações Aplicadas**

- Todas as **tasks incompletas ou com baixa cobertura de testes** foram revistas e detalhadas.
- Adicionadas **subtasks** específicas para garantir:
  - Implementação de **docstrings e logs**.
  - Detalhamento da **arquitetura de 3 camadas no mockup**.
  - Justificativas para o uso das tecnologias escolhidas (ex: Streamlit x React).
  - Descrição de estratégias de **escalabilidade e resposta a incidentes**.
- Criado um histórico de mudanças mais **robusto no `GestaoProjeto.md`**, com anotações sobre cada versão entregue.
- Incorporados **feedbacks diretamente no planejamento da Sprint 5**, assegurando que todas as sugestões da banca fossem consideradas no encerramento do projeto.

### **Considerações sobre Riscos e Ajustes**

Para garantir flexibilidade caso as estimativas se provem imprecisas, os seguintes pontos foram considerados:

- **Riscos Identificados:**
  - Dependência de infraestrutura na nuvem para a implantação do DataApp, podendo gerar atrasos.
  - Escolha da biblioteca para visualização de gráficos pode impactar na performance e escalabilidade.
  - Implementação da segurança pode demandar ajustes dependendo da conformidade com políticas internas.

- **Planos de Ajuste:**
  - Caso a configuração do ambiente na nuvem demore mais que o esperado, vamos priorizar outras tasks como a estruturação do DataApp localmente.
  - Se a biblioteca escolhida não atender aos requisitos de interatividade e performance, haverá um plano de contingência com bibliotecas alternativas.
  - Revisões de segurança podem ser feitas de forma incremental, evitando bloqueios no desenvolvimento do pipeline.

### **Medição de Métricas de Desempenho Sprint 4**

A análise das métricas de desempenho da Sprint 4 permite avaliar a eficiência da equipe em relação ao planejamento, execução e entrega das tarefas.

#### **Throughput Sprint 4**

- **User stories concluídas:** 6
- **Tasks finalizadas:** 14
- **Velocidade da sprint: 21 s**tory points
- **Método de coleta:** O throughput foi medido com base na movimentação de cartões no Trello para a coluna "Concluído", contabilizando apenas os cards encerrados até o final da sprint.

#### **Cycle Time Sprint 4**

- **Média de tasks concluídas por dia:** 2
- **Task mais longa:** Implementar monitoramento da qualidade dos dados (7 dias)
- **Task mais rápida:** Priorizar backlog para a Sprint 5 (3 horas)
- **Método de coleta:** O cycle time foi obtido pela análise da permanência de cada tarefa na coluna "Em progresso", desde o início até sua conclusão no Trello.

#### **Burndown Sprint 4**

- **Percentual de tasks concluídas:** 87%
- **Padrão observado:** A equipe iniciou a sprint com ritmo moderado, acelerando na segunda metade da sprint para recuperar o progresso e atingir os objetivos.

# Planejamento Sprint 5 

### Definição de Tasks 5

#### **Épico 1: Finalização do DataApp**

**User Story 1.1: Como desenvolvedor, preciso garantir que o DataApp esteja corretamente integrado com a infraestrutura técnica para manter a conformidade arquitetural.**

- **Task 1.1.1: Revisar a arquitetura do sistema e documentar pontos de integração.**  
  - Analisar documentos de arquitetura e identificar pontos de melhoria.  
  - Atualizar diagramas conforme necessário.  
  - **Critérios de Qualidade:** O sistema deve estar documentado corretamente e alinhado com os padrões arquiteturais.

- **Task 1.1.2: Corrigir eventuais falhas na comunicação entre serviços.**  
  - Identificar erros de conexão e integração.  
  - Implementar soluções para correção.  
  - **Critérios de Qualidade:** A comunicação entre módulos deve ser estável e eficiente.

**User Story 1.2: Como usuário, desejo um processo de login seguro e eficiente para garantir proteção e boa experiência.**

- **Task 1.2.1: Configurar autenticação no ambiente de testes.**  
  - Integrar Auth0 com o sistema.  
  - Testar login e logout.  
  - **Critérios de Qualidade:** O login deve ser funcional e seguro.

- **Task 1.2.2: Ajustar a interface para melhor usabilidade na autenticação.**  
  - Melhorar layout e acessibilidade dos formulários.  
  - Validar a interface com testes de usabilidade.  
  - **Critérios de Qualidade:** A interface deve ser intuitiva e responsiva.

#### **Épico 2: Documentação Final do Projeto**

**User Story 2.1: Como stakeholder, desejo ter acesso a uma documentação clara e organizada para entender a evolução do projeto.**

- **Task 2.1.1: Organizar os arquivos de documentação existentes.**  
  - Revisar estrutura de arquivos no GitHub.  
  - Atualizar descrições conforme necessidade.  
  - **Critérios de Qualidade:** A documentação deve estar clara e acessível.

- **Task 2.1.2: Gerar análise de impacto e relato detalhado.**  
  - Coletar feedbacks e dados sobre a implementação.  
  - Redigir análise final do impacto do projeto.  
  - **Critérios de Qualidade:** O relato deve apresentar evidências e conclusões claras.

#### **Épico 3: Análise Evolutiva do Projeto**

**User Story 3.1: Como equipe, queremos entender os pontos fortes e fracos do projeto para melhorar futuras sprints.**

- **Task 3.1.1: Coletar e analisar o throughput do projeto.**  
  - Extrair dados das sprints anteriores.  
  - Identificar padrões e gargalos.  
  - **Critérios de Qualidade:** A análise deve ser baseada em dados reais.

- **Task 3.1.2: Gerar e interpretar gráficos de burndown.**  
  - Criar gráficos de desempenho.  
  - Avaliar ritmo de entrega da equipe.  
  - **Critérios de Qualidade:** Os gráficos devem ser claros e informativos.

### **Distribuição de Pontos na Sprint 5**
Baseado na métrica de **Fibonacci**, as estimativas para as tasks da Sprint 5 são as seguintes:

| Task                                                             | Estimativa (Fibonacci) |
|------------------------------------------------------------------|------------------------|
| Revisar a arquitetura do sistema e documentar pontos de integração | 5                      |
| Corrigir eventuais falhas na comunicação entre serviços           | 5                      |
| Configurar autenticação no ambiente de testes                     | 3                      |
| Ajustar a interface para melhor usabilidade na autenticação       | 3                      |
| Organizar os arquivos de documentação existentes                 | 2                      |
| Gerar análise de impacto e relato detalhado                       | 5                      |
| Coletar e analisar o throughput do projeto                        | 3                      |
| Gerar e interpretar gráficos de burndown                          | 5                      |
| Revisar diretrizes de governança de dados                         | 3                      |
| Documentar as novas políticas de governança de dados              | 5                      |
| Definir regras de qualidade dos dados                             | 5                      |
| Implementar monitoramento da qualidade dos dados                  | 8                      |

**Total estimado: 53 pontos**

### **Considerações sobre Riscos e Ajustes Sprint 5**

Para garantir a execução adequada do planejamento da Sprint 5, foram levantados os principais riscos relacionados às tarefas previstas e definidos planos de ajustes para mitigar possíveis impactos no cronograma e na qualidade das entregas.

- **Riscos Identificados:**

  - **Integração e arquitetura do sistema:**
A revisão da arquitetura e a correção de falhas de integração entre os serviços pode demandar tempo adicional caso dependam de infraestrutura externa ou documentação incompleta.

  - **Configuração de autenticação com Auth0:**
Problemas de compatibilidade com o ambiente de testes ou instabilidades na plataforma Auth0 podem atrasar a conclusão do processo de login.

  - **Organização da documentação final:**
A consolidação dos arquivos e a produção da análise de impacto podem ser prejudicadas caso a equipe não registre corretamente as decisões técnicas ao longo da sprint.

  - **Monitoramento da qualidade dos dados:**
A tarefa de implementar monitoramento contínuo pode sofrer atrasos se forem encontradas inconsistências nos dados ou limitações nas ferramentas de coleta e análise.

- **Planos de Ajuste:**

  - Caso a revisão da arquitetura exija tempo extra, priorizaremos primeiro a documentação dos pontos já validados, garantindo ao menos a entrega parcial da task com justificativa clara no relatório.

  - Em caso de dificuldade na autenticação com Auth0, será criado um login alternativo mockado no ambiente de testes, permitindo o avanço nas tarefas de interface e usabilidade até a resolução definitiva.

  - Se houver sobrecarga na tarefa de organização da documentação final, ela poderá ser dividida entre os membros da equipe por seção, otimizando tempo e melhorando a rastreabilidade das contribuições.

  - Caso o monitoramento da qualidade dos dados não possa ser completado integralmente, será priorizada a implementação de alertas e logs básicos, adiando para a próxima sprint a etapa de auditoria avançada e ajustes finos.

### **Justificativa da Priorização das Tasks da Sprint 5**

A priorização das atividades nesta sprint foi guiada pelo fato de que se trata da última sprint do projeto, sendo fundamental garantir a entrega final do produto, sua estabilidade técnica e a completude da documentação. Os critérios adotados foram:

- **Concluir a entrega do produto funcional**

As tarefas relacionadas ao DataApp e à sua autenticação foram priorizadas por representarem diretamente o produto final esperado. A integração entre os módulos, o funcionamento do login e a estabilidade da aplicação são essenciais para garantir uma entrega utilizável e validável pelo parceiro.

- **Assegurar a qualidade técnica e correção de falhas**

Como é a última sprint, eventuais falhas na comunicação entre serviços e ajustes arquiteturais precisam ser resolvidos agora, para evitar que o sistema apresente problemas após a entrega. Essas tarefas também viabilizam o funcionamento pleno de todas as funcionalidades integradas.

- **Consolidar documentação e entregáveis**

A organização dos arquivos, o relato de impacto e a documentação técnica são fundamentais para garantir transparência, rastreabilidade e entendimento futuro do projeto por stakeholders e avaliadores. Isso também facilita a manutenção e evolução do sistema após o encerramento do projeto.

- **Analisar e comunicar resultados da equipe** 

Por fim, a coleta de métricas como throughput e burndown nesta sprint é crucial para fechar o ciclo de monitoramento da evolução do projeto, gerar aprendizados e demonstrar a maturidade da equipe em gestão ágil e entregas contínuas.

### **Medição de Métricas de Desempenho Sprint 5**

A análise das métricas de desempenho da Sprint 5 permitiu avaliar a efetividade da equipe na execução das entregas finais do projeto, com foco em estabilidade, integração e documentação.

#### **Throughput da Sprint 5**

- **User Stories concluídas:** 3
  - Finalização do DataApp
  - Documentação Final do Projeto
  - Análise Evolutiva do Projeto
- **Tasks finalizadas:** 12  
  (Revisar arquitetura, corrigir integração, autenticação, usabilidade, organização documental, análise de impacto, análise de throughput, burndown, revisão de governança, documentação de políticas, definição e monitoramento de qualidade dos dados)
- **Velocidade da sprint:** 53 story points
- **Método de coleta:**  
  Os dados foram extraídos diretamente do Trello, considerando os cards movidos para a coluna **"Concluído"** durante a Sprint 5. Cada task foi vinculada à sua respectiva user story e pontuada com base na escala de Fibonacci previamente definida.

#### **Burndown Chart da Sprint 5**

- **Configuração da Sprint:**
  - Duração: 7 dias úteis
  - Total planejado: 53 pontos
- **Padrão observado:**
  - A equipe iniciou a sprint com ritmo constante, concluindo aproximadamente 8 pontos por dia.
  - Houve uma desaceleração leve no meio da sprint devido à complexidade da tarefa de monitoramento de dados (8 pontos), compensada por um esforço coletivo na reta final.
  - Ao final da sprint, todas as tasks planejadas foram concluídas, com exceção de ajustes de documentação que foram finalizados junto com o fechamento do relatório.

**Gráfico de burndown (sintético):**

| Dia | Pontos Restantes |
|-----|------------------|
| 1   | 53               |
| 2   | 48               |
| 3   | 40               |
| 4   | 35               |
| 5   | 24               |
| 6   | 5                |
| 7   | 3                |

- **Interpretação:**  
  O gráfico mostra uma **redução contínua do trabalho restante**, com uma leve queda na produtividade entre os dias 3 e 4 (decorrente de tarefas mais complexas), e uma forte recuperação no final da sprint. Isso indica uma boa capacidade de adaptação da equipe ao balancear tarefas técnicas críticas com entregas documentais.


## **Análise Evolutiva das Métricas de Desempenho**

### **Evolução do Throughput**

| Sprint | User Stories Concluídas | Tasks Finalizadas | Story Points Entregues |
|--------|--------------------------|--------------------|-------------------------|
| 1      | 3                        | 12                 | ~18 (estimado)          |
| 2      | 7                        | 12                 | 18                      |
| 3      | 8                        | 14                 | 20                      |
| 4      | 6                        | 14                 | 21                      |
| 5      | 3                        | 12                 | 53                      |

**Análise:**  
- Houve uma **curva ascendente** estável no throughput entre as Sprints 2 a 4, indicando maturidade crescente no ritmo de entregas.
- A **Sprint 5 apresentou um salto expressivo (53 pontos)**, refletindo um esforço concentrado para a finalização do projeto e fechamento de pendências críticas. Isso é comum em sprints finais, onde há um volume maior de tarefas de integração, testes, documentação e ajustes finos.


### **Evolução do Cycle Time**

| Sprint | Média de Tasks por Dia | Task Mais Rápida       | Task Mais Longa         |
|--------|------------------------|------------------------|--------------------------|
| 1      | ~1                     | Atualização de backlog | Implementação de pipeline (9 dias) |
| 2      | 1-2                    | 6 horas                | 9 dias                   |
| 3      | 1-3                    | 3 horas                | 5 dias                   |
| 4      | 2                      | 3 horas                | 7 dias                   |
| 5      | 2                      | 3 horas                | 5 dias                   |

**Análise:**  
- O **cycle time médio melhorou gradativamente**, com aumento de eficiência e organização das tarefas.
- Nas últimas sprints, o time passou a **quebrar melhor as tasks**, reduzindo o tempo médio de conclusão e mantendo o foco na agilidade, mesmo com tarefas de alta complexidade.
- O comportamento consistente na Sprint 5 mostra que a equipe conseguiu lidar com o **alto volume de entregas sem comprometer prazos**, fruto de um bom refinamento e distribuição de tarefas.


### **Evolução do Burndown**

| Sprint | % de Tasks Concluídas | Padrão Observado                              |
|--------|------------------------|-----------------------------------------------|
| 1      | 100%                   | Atraso inicial, recuperação no fim            |
| 2      | 85%                    | Atraso na 1ª metade, recuperação na 2ª        |
| 3      | 90%                    | Ritmo constante                               |
| 4      | 87%                    | Aceleração na 2ª metade                       |
| 5      | 100%                   | Ritmo regular com conclusão total planejada   |

**Análise:**  
- O **burndown foi um espelho do amadurecimento da equipe em planejamento e execução.**
- As primeiras sprints apresentaram **oscilações no ritmo**, com entregas concentradas nos últimos dias.
- Da Sprint 3 em diante, a equipe demonstrou **melhor gestão de tempo**, com burndowns mais lineares e conclusões mais previsíveis.
- A **Sprint 5 se destaca pela execução completa das tarefas dentro do ritmo planejado**, evidenciando o domínio do escopo e uma excelente coordenação final.


## **Conclusões Gerais sobre Sprints**

- **Melhoria contínua e consistente:** O time demonstrou evolução clara nas três métricas principais. A eficiência (throughput), velocidade de resposta (cycle time) e capacidade de prever o ritmo (burndown) foram aperfeiçoadas ao longo do projeto.
- **Aprendizado Sprint a Sprint:** As dificuldades iniciais de planejamento e execução foram sendo gradualmente superadas à medida que a equipe ajustava seu processo interno.
- **Sprint 5 como consolidação de maturidade ágil:** A última sprint foi decisiva para mostrar não apenas volume de entrega, mas qualidade no controle, visibilidade e organização do trabalho.


## Uso das Políticas de Gestão de Configuração

Mantemos um fluxo de trabalho estruturado para controle e rastreabilidade do código:

- **Sistema de Branches:** Segue padrão GitFlow
- **Conventional Commits:** Adotamos o padrão para clareza no histórico

### Esteira de CI 

A esteira de Integração Contínua (CI) tem como objetivo automatizar testes e builds do frontend sempre que houver um push ou um Pull Request (PR) para as branches dev ou main. Isso garante que possíveis quebras sejam identificadas antes da integração do código.

1. Fluxo da Esteira de CI
Evento Disparador
  ``Push para as branches dev ou main
  Abertura de Pull Request para dev ou main
  Execução do Pipeline`` 

  **Checkout do Código:** Clona o repositório e acessa a branch correspondente.

  **Instalação de Dependências:** Instala todas as bibliotecas e pacotes necessários.

  **Execução de Testes Automatizados:** Validações unitárias, integração e e2e (se aplicável).

  **Build do Frontend:** Gera o artefato final pronto para deploy.

  **Relatório de Status:** Indica sucesso ou falha nos testes/build.

2. **Configuração e Versionamento**
   
Arquivos de Configuração do Pipeline: ci-config.yml (ou equivalente no GitHub Actions, GitLab CI, Jenkins, etc.).
Controle de Versão: Todas as alterações na esteira devem ser versionadas e passar por revisão antes de serem aplicadas.
Variáveis de Ambiente: Definir e armazenar credenciais sensíveis em um cofre seguro, evitando exposição no código.

4. **Políticas de Aprovação**
   
Pull Requests: Devem ser aprovados por pelo menos um revisor antes de serem mesclados.
Build e Testes: O código só pode ser integrado se todos os testes forem aprovados.
Deploy Automatizado: Pode ser acionado após a aprovação da build para ambientes de staging.

6. **Monitoramento e Logs**
   
Logs do Pipeline: Devem estar acessíveis para debugging e rastreamento de falhas.
Notificações: Alertas via Slack, e-mail ou outro meio quando o pipeline falhar.
Métricas de CI: Tempo médio de execução, taxa de falhas e cobertura de testes.

## Feedback 

Nessa seção reunimos os feedbacks recebidos de cada artefato para melhor entendimento de erros e refatoração dos entregáveis.

### Relatório de Desempenho e Melhorias

#### Sprint 1: Desafios de Planejamento

Na Sprint 1, enfrentamos problemas de planejamento, o que resultou na ausência de notas em dois artefatos: **GESTÃO EVOLUTIVA DO PROJETO** e **ANÁLISE EXPLORATÓRIA E DE GOVERNANÇA DE DADOS**. Além disso, o desempenho nos artefatos **TEMPLATE DE PROJETO DE GESTÃO E GOVERNANÇA DE DADOS** e **DOCUMENTAÇÃO DO PROJETO DE GESTÃO E GOVERNANÇA DE DADOS** ficou abaixo do esperado.

#### Estratégia para Sprint 2
Diante desses desafios, na Sprint 2, adotamos uma estratégia de planejamento mais rigoroso, contemplando todas as exigências dos artefatos. Quebramos as tasks ao máximo para garantir que nenhum ponto fosse deixado de lado, o que resultou em um desempenho 80% superior em comparação com a Sprint 1. Para as próximas sprints, manteremos o mesmo esquema de planejamento da Sprint 2, ajustando as melhorias com base nos feedbacks recebidos.

---

#### Notas e Artefatos da Sprint 1

Artefato: **TEMPLATE DE PROJETO DE GESTÃO E GOVERNANÇA DE DADOS**

#### Arquitetura de Negócios e de Dados
- **Pontos positivos**:
  - O documento apresenta todas as seções requeridas.
  - As descrições estão bem estruturadas.
- **O que pode ser melhorado**:
  - Mais detalhes sobre como a governança de dados será implementada na prática.

#### Projeto de Gestão e Governança de Dados
- **Pontos positivos**:
  - Inclui uma visão detalhada da demanda do projeto.
- **O que pode ser melhorado**:
  - Os requisitos funcionais (RFs) e não funcionais (RNFs) não foram listados explicitamente com testes e matriz de rastreabilidade.
  - Falta o uso de um Data Product Canvas.

#### Conformidade com conteúdos das sprints do módulo
- **Pontos positivos**:
  - O documento prevê seções para cada sprint.
- **O que pode ser melhorado**:
  - Falta preenchimento detalhado dos entregáveis e ajustes feitos ao longo das sprints.

#### Conformidade com Padrões Oficiais de Engenharia de Dados
- **Pontos positivos**:
  - O documento menciona o TOGAF como modelo base.
- **O que pode ser melhorado**:
  - Não há menção a padrões como DMBOK, ISO 25012, ISO 38505 ou DataOps.
  - A justificativa para o uso do TOGAF poderia ser mais detalhada.

#### Qualidade, Organização e Navegação no Documento
- **Pontos positivos**:
  - A estrutura do documento é bem organizada, com sumário e divisão clara de seções.
- **O que pode ser melhorado**:
  - Faltam links internos para navegação facilitada.
  - Não há histórico de revisões nem glossário.

Artefato: **DOCUMENTAÇÃO DO PROJETO DE GESTÃO E GOVERNANÇA DE DADOS**

#### Visão geral do parceiro e do projeto
- **Pontos positivos**:
  - Apresenta um contexto claro sobre a Volkswagen Brasil.
- **O que pode ser melhorado**:
  - Maior profundidade na descrição das oportunidades relacionadas à digitalização e análise de dados.

#### Objetivos e Escopo do Projeto
- **Pontos positivos**:
  - Os objetivos foram definidos, com foco na implementação de um pipeline de dados em tempo real para análise de falhas.
- **O que pode ser melhorado**:
  - Faltou detalhamento das fontes de dados específicas e métodos de integração.

#### Alinhamento Estratégico
- **O que pode ser melhorado**:
  - O alinhamento estratégico foi mencionado, mas de forma superficial.

#### Processos, Objetivos e Metas
- **Pontos positivos**:
  - Os processos principais, objetivos e metas foram listados.
- **O que pode ser melhorado**:
  - Faltou maior profundidade. O uso do Data Product Canvas não foi mencionado.

#### Projeto de Gestão e Governança de Dados
- **O que pode ser melhorado**:
  - Os RFs e RNFs foram listados, mas sem muito detalhamento. A relação entre RFs e RNFs foi mencionada brevemente.

#### Estrutura da Governança de Dados
- **O que pode ser melhorado**:
  - A definição de governança de dados foi mencionada, mas sem muita profundidade.

#### Políticas de Uso dos Dados
- **O que pode ser melhorado**:
  - Falta consistência nas políticas de compartilhamento de dados e retenção de informações.

#### Medição da Qualidade dos Dados
- **O que pode ser melhorado**:
  - Faltaram detalhes sobre os processos de garantia de qualidade e validação de dados.

Artefato: **WIREFRAME DO DATAAPP**

#### Relações com a Arquitetura
- **O que pode ser melhorado**:
  - O wireframe está simplificado e não representa efetivamente o projeto como um todo.

#### Relações com a Análise Exploratória
- **O que pode ser melhorado**:
  - O projeto apresenta pontos que não condizem com o discutido em instrução.

#### Base de prospecção de tecnologia de DataApp
- **O que pode ser melhorado**:
  - A prospecção tem relação com o projeto, mas não está representada no wireframe.

#### Clareza e organização do design do wireframe
- **O que pode ser melhorado**:
  - O design está bem organizado, mas muito genérico.

---

#### Notas e Artefatos da Sprint 2

Artefato: **GESTÃO EVOLUTIVA DO PROJETO**

#### Medição de Métricas de Desempenho
- **Pontos positivos**:
  - Burndown foi analisado corretamente, com uma explicação clara sobre os padrões observados.
- **O que pode ser melhorado**:
  - Throughput e Cycle time: Apresentados sem um detalhamento mais preciso sobre como os dados foram coletados.

#### Planejamento da Sprint
- **Pontos positivos**:
  - O planejamento inclui tasks bem definidas, priorizadas e estimadas usando Fibonacci.
- **O que pode ser melhorado**:
  - Faltam considerações sobre riscos e ajustes caso as estimativas se provem imprecisas.

#### Atualização do Documento GestãoProjeto.md
- **Pontos positivos**:
  - O documento está atualizado e organizado corretamente.
- **O que pode ser melhorado**:
  - A seção de histórico de revisões poderia detalhar melhor as alterações realizadas.

#### Atendimento aos critérios do Escritório de Projeto
- **Pontos positivos**:
  - Os critérios foram considerados e mencionados no documento.
- **O que pode ser melhorado**:
  - Faltam evidências concretas sobre como os critérios foram atendidos.

Artefato: **DOCUMENTAÇÃO DO PROJETO DE GESTÃO E GOVERNANÇA DE DADOS**

#### Arquitetura (Diagramas) de Fluxo e Processos
- **Pontos positivos**:
  - O diagrama está bem detalhado e segue uma lógica clara.
- **O que pode ser melhorado**:
  - Poderiam incluir legendas mais visíveis para ressaltar a interação entre os módulos.

#### Modelagem dos Dados (Diagramas)
- **Pontos positivos**:
  - A modelagem de dados é consistente e reflete bem as entidades e seus relacionamentos.
- **O que pode ser melhorado**:
  - Faltam detalhes nos rótulos de chaves primárias e estrangeiras.

#### Considerações de Governança - Segurança
- **Pontos positivos**:
  - As estratégias de segurança são abordadas.
- **O que pode ser melhorado**:
  - Faltam detalhes sobre auditoria contínua e testes de invasão.

#### Monitoramento e Gerenciamento
- **Pontos positivos**:
  - A solução de logs e telemetria apresenta rastreabilidade consistente.
- **O que pode ser melhorado**:
  - Faltam detalhes sobre processos de escalonamento e respostas a incidentes.

#### Integridade de Dados
- **Pontos positivos**:
  - As táticas de normalização e auditoria reforçam a consistência.
- **O que pode ser melhorado**:
  - Faltam exemplos práticos de validações ao longo do pipeline.

#### Ferramentas de Arquitetura
- **Pontos positivos**:
  - A seleção de ferramentas está bem justificada.
- **O que pode ser melhorado**:
  - Mais detalhes sobre comparações com soluções concorrentes.

Artefato: **MÓDULO DE INGESTÃO E TRANSFORMAÇÃO DE DADOS**

#### Eficiência na Ingestão de Dados
- **Pontos positivos**:
  - O projeto apresentou uma estrutura bem definida.
- **O que pode ser melhorado**:
  - O tratamento de erros pode ser aprimorado para lidar melhor com formatos incorretos e campos ausentes.

#### Flexibilidade nos Formatos de Dados
- **Pontos positivos**:
  - Suporte a múltiplos formatos de dados é um diferencial positivo.
- **O que pode ser melhorado**:
  - A modularização pode ser melhorada para evitar repetição de código.

#### Processamento e Transformação de Dados
- **Pontos positivos**:
  - As transformações estão bem implementadas e há boa visualização de dados.
- **O que pode ser melhorado**:
  - Comentários excessivos e falta de modularização afetam a legibilidade e eficiência do código.

#### Notas e Artefatos da Sprint 3

Na Sprint 3, conseguimos alcançar uma média de nota 9 nos artefatos, o que demonstra uma clara evolução em relação às entregas anteriores, nas quais a média foi 4 na Sprint 1 e 8 na Sprint 2. Essa melhoria de desempenho reflete a efetividade das mudanças implementadas nas Sprints 1 e 2, com foco no planejamento mais rigoroso, maior atenção aos detalhes e integração dos feedbacks. O progresso contínuo nas entregas confirma a evolução do time e do processo ao longo das sprints e pretendemos seguir nesse ritmo.

---

Artefato: **MÓDULO DE PROCESSAMENTO, INTEGRAÇÃO E MANIPULAÇÃO DE DADOS**

- **Pontos positivos:**
  - **Pipeline de Deploy**: A implementação do pipeline de CI (.github/workflows/ci.yml) é um bom começo, indicando que há um processo de integração contínua bem estruturado no projeto.
  - **Testagem com Framework de Testes**: A utilização do framework Dash e a separação clara entre os componentes do projeto indicam uma tentativa de arquitetura de 3 camadas. Essa abordagem ajuda a organizar o código e torna o projeto mais modular.
  - **Utilização de Framework em uma Arquitetura de 3 Camadas**: Os testes usando pytest e unittest.mock estão bem aplicados, simulando exceções e conexões de maneira apropriada.
  - **Melhores Práticas de Código**: A estrutura organizacional do código é boa, e o uso de Dash facilita a construção do dashboard. Há uma tentativa de melhorar a legibilidade com a organização do código, mesmo que a documentação precise ser mais robusta.

- **O que pode ser melhorado:**
  - **Pipeline de Deploy**: O processo de deploy ainda carece de mais detalhes técnicos para garantir que todos os passos do pipeline estejam claros e compreendidos, como o processo de testes automáticos e a integração com o GitHub Actions.
  - **Testagem com Framework de Testes**: Embora o uso de pytest e unittest.mock seja adequado, a cobertura de testes é limitada. Seria interessante expandir os testes, incluindo cenários de erro e testes de integração mais completos.
  - **Utilização de Framework em uma Arquitetura de 3 Camadas**: A definição de camadas lógicas e de acesso a dados precisa ser mais robusta. É importante garantir que o código esteja realmente modularizado e a arquitetura esteja bem definida.
  - **Melhores Práticas de Código**: A documentação dos arquivos precisa ser aprimorada, principalmente em relação aos docstrings e ao uso de logs para garantir uma maior transparência e rastreabilidade do código.

---

Artefato: **DOCUMENTAÇÃO DO PROJETO DE GESTÃO E GOVERNANÇA DE DADOS**

- **Pontos positivos:**
  - **Abrangência da Documentação**: A documentação é bem completa e apresenta uma visão clara do projeto, incluindo arquitetura, fluxo de dados, governança e segurança.
  - **Integração de Aspectos de Governança e Escalabilidade**: A governança de dados é tratada com atenção, especialmente em relação à segurança, acesso e conformidade com a LGPD. A escalabilidade do sistema, com o uso de RabbitMQ e ClickHouse, é mencionada de forma adequada.
  - **Transparência, Colaboração e Manutenção da Documentação**: O documento é bem estruturado e inclui informações sobre o uso de ferramentas colaborativas (Google Drive, GitHub, Slack, Trello). A documentação é claramente atualizada com base nos feedbacks das sprints anteriores.

- **O que pode ser melhorado:**
  - **Abrangência da Documentação**: A documentação precisa incluir mais detalhes sobre a cobertura dos testes automatizados e a utilização de ferramentas como pytest-cov. Além disso, o pipeline CI/CD poderia ser documentado de maneira mais detalhada.
  - **Integração de Aspectos de Governança e Escalabilidade**: A descrição da escalabilidade poderia ser mais clara, detalhando como o sistema lida com aumentos massivos de dados. Além disso, o plano de resposta a incidentes poderia incluir revisões periódicas e métricas para avaliar sua eficácia.
  - **Transparência, Colaboração e Manutenção da Documentação**: Embora o uso do GitHub seja mencionado, seria interessante detalhar mais sobre o versionamento adequado, especialmente no arquivo do pipeline CI/CD. A documentação não deixa claro se é tratada como uma documentação viva, com atualizações frequentes. A falta de feedback integrado também precisa ser abordada, detalhando como os feedbacks das sprints anteriores foram incorporados.

---

Artefato: **MOCKUP DO DATAAPP**

- **Pontos positivos:**
  - **Relações com a Arquitetura**: O mockup está bem conectado à arquitetura geral do sistema, com uma boa representação visual das funcionalidades do DataApp.
  - **Relações com a Análise Exploratória**: O mockup traduz de maneira eficaz os insights da análise exploratória em representações visuais, facilitando a identificação de padrões e falhas no processo de dados.
  - **Base de Prospecção de Tecnologia de DataApp**: As tecnologias escolhidas para o DataApp estão bem apresentadas, com um bom raciocínio sobre como elas contribuem para a construção da aplicação.
  - **Clareza e Organização do Design do Mockup**: O design do mockup é claro, intuitivo e bem organizado, com boa consistência visual e alinhamento com a identidade Volkswagen.

- **O que pode ser melhorado:**
  - **Relações com a Arquitetura**: Faltou detalhar de forma mais explícita como cada visualização do dashboard interage diretamente com as camadas da arquitetura, especialmente em relação à integração com o pipeline de dados.
  - **Base de Prospecção de Tecnologia de DataApp**: Seria interessante detalhar mais sobre os aspectos técnicos que facilitam decisões tecnológicas futuras, como requisitos de desempenho, escalabilidade e critérios para a escolha de tecnologias como Streamlit versus React.

---

Artefato: **GESTÃO EVOLUTIVA DO PROJETO**

- **Pontos positivos:**
  - **Atualização do Backlog Completo**: O backlog está bem organizado e atualizado, refletindo as tarefas e metas do projeto de maneira clara.
  - **Planejamento da Sprint 4**: O planejamento está bem estruturado, com uma visão clara das tarefas e prioridades. As estimativas de esforço estão bem alinhadas com o progresso do projeto.
  - **Uso correto das políticas de gestão de configuração no projeto**: O uso das políticas de gestão de configuração foi bem documentado e está de acordo com os requisitos exigidos.

- **O que pode ser melhorado:**
  - **Medição de Métricas de Desempenho**: As métricas de throughput e cycle time precisam de mais detalhes metodológicos. Seria interessante explicar como os valores foram obtidos para aumentar a confiabilidade da análise e assegurar que os dados são representativos.
  - **Planejamento da Sprint 4**: Embora o planejamento esteja bem estruturado, ele poderia ser enriquecido com mais detalhes sobre as tasks, suas justificativas e prioridades. Isso ajudaria a melhorar a comunicação sobre as decisões tomadas.
  - **Atendimento aos critérios do Escritório de Projeto**: O documento menciona os critérios do Escritório de Projetos, mas seria interessante incluir uma seção detalhada explicando como cada critério foi atendido ao longo do processo de planejamento e execução.
  - **Atualização do Documento GestãoProjeto.md**: O documento foi atualizado corretamente, mas seria interessante detalhar mais sobre as alterações feitas nas versões anteriores, fornecendo um histórico de mudanças mais robusto.

# Análise Post Mortem

### Sucessos do Projeto

Durante o ciclo de desenvolvimento, o grupo alcançou diversos marcos importantes que demonstram maturidade técnica e organizacional:

- **Integração Tecnológica Robusta**: O uso coordenado de RabbitMQ, Supabase, ClickHouse, API Python e Streamlit resultou em um pipeline funcional, seguro e escalável.
- **Automação e Redução de Retrabalho**: A automação dos processos de ingestão e análise de falhas permitiu uma redução de 20% no retrabalho e aumentou a confiabilidade da produção.
- **Conformidade com LGPD e Governança**: A equipe aplicou com sucesso práticas de segurança, rastreabilidade e proteção de dados pessoais, atendendo integralmente os requisitos da LGPD.
- **Dashboard de Telemetria Eficiente**: O painel visual facilitou a análise de eventos e performance, sendo elogiado pelos stakeholders técnicos.
- **Colaboração do Grupo**: Boa divisão de tarefas e comunicação clara entre os membros, com entregas bem distribuídas ao longo das sprints.

### Oportunidades de Melhoria

Apesar dos resultados positivos, alguns pontos foram identificados como oportunidades de crescimento:

- **Planejamento Inicial Subestimado**: A complexidade do processamento e integração de dados foi subestimada, o que impactou prazos no início do projeto.
- **Documentação Técnica Parcialmente Atrasada**: Alguns registros importantes (como versionamento do Supabase) foram atualizados apenas nas sprints finais.
- **Validação com Usuário Final Limitada**: O projeto priorizou a eficiência técnica, mas teve poucas interações diretas com operadores de produção e usuários reais do dashboard.
- **Desempenho em Altos Volumes de Dados**: Apesar do bom desempenho atual, testes com grandes volumes foram limitados. A escalabilidade precisa ser testada em condições de stress.

### Lições Aprendidas

| Categoria            | Lição Aprendida                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Técnica**          | A modularização do ETL desde o início evita retrabalho e facilita a manutenção.|
| **Gestão de Projeto**| Detalhar melhor os riscos e reservar mais tempo para testes e validação.        |
| **Governança de Dados**| A rastreabilidade dos dados precisa ser pensada desde a concepção da arquitetura.|
| **Pessoal/Grupo**    | O trabalho em pares ajudou a reduzir bugs e a manter o alinhamento técnico.     |

### Recomendações para Projetos Futuros

- Incluir desde o início **entrevistas com usuários reais** para garantir aderência funcional.
- Realizar um **workshop técnico de alinhamento de arquitetura** na primeira semana.
- Aplicar **teste de carga automatizado** antes da entrega final.
- Implementar um **quadro de maturidade de governança de dados** para medir evolução do projeto ao longo das sprints.

---

Acreditamos que essa análise crítica e honesta fortalece a equipe para desafios futuros, contribuindo para uma cultura de melhoria contínua e excelência técnica.
