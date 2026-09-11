# Sistema de Dimensionamento Energético Residencial
## MVP v2 — User Stories e Tasks (com base no feedback de uso)

---

## 1. Problemas identificados na versão anterior

| ID | Problema | Relato do usuário | Prioridade |
|----|---|---|---|
| P01 | Resultado pouco claro | "Não sei o que significa essa média." | Alta |
| P02 | Cálculo limitado | "Meu consumo não depende apenas da quantidade de aparelhos." | Alta |
| P03 | Não existe histórico | "Não consigo comparar meu consumo ao longo dos meses." | Alta |
| P04 | Não mostra maior consumo | "Quero saber qual foi meu pior mês." | Alta |
| P05 | Não mostra o mês do pico | "Quando eu mais consumi energia?" | Média |
| P06 | Não há resumo | "Quero entender meu resultado rapidamente." | Alta |
| P07 | Não há gráfico | "Queria visualizar meu consumo." | Baixa |
| P08 | Entradas podem gerar erro | "E se eu colocar 0 ou um valor inválido?" | Alta |
| P09 | Dados são perdidos | "Se eu fechar o programa, perdi tudo?" | Alta |
| P10 | Não há usuário/imóvel | "Onde ficam salvos meus dados?" | Alta |
| P11 | Não há visibilidade | "Queria visualizar meu consumo." | Baixa |
| P12 | Entradas podem gerar erro | "E se eu colocar 0 ou um valor inválido?" | Alta |

## 2. Mudança de abordagem no cálculo

A versão anterior estimava o consumo a partir de equipamentos cadastrados
(potência × quantidade × tempo de uso). O feedback (P02) mostrou que isso
não reflete o consumo real do usuário. **A partir desta versão, o consumo
mensal é informado diretamente pelo usuário, em kWh**, mês a mês, e o
sistema passa a trabalhar sobre esse histórico.

---

## 3. Novo Product Backlog

| ID | Prioridade | User Story | Problema(s) atendido(s) |
|----|---|---|---|
| PB01 | Alta | Cadastro do imóvel e do usuário responsável | P10 |
| PB02 | Alta | Registro do consumo mensal real, mês a mês | P02, P03 |
| PB03 | Alta | Cálculo do consumo médio mensal, com explicação clara do cálculo | P01, P06 |
| PB04 | Alta | Identificação automática do maior consumo mensal registrado | P04 |
| PB05 | Média | Identificação do mês/ano em que ocorreu o maior consumo | P05 |
| PB06 | Alta | Resumo energético completo do imóvel | P06 |
| PB07 | Alta | Validação de todas as entradas de consumo | P08, P12 |
| PB08 | Baixa | Representação visual (gráfico em texto) do consumo mensal | P07, P11 |
| PB09 | Alta (implementada por último) | Persistência dos dados do imóvel/usuário e do histórico de consumo | P09 |

> PB01 cobre o cadastro básico do imóvel/usuário em memória, necessário
> desde o início para que os demais itens funcionem. PB09 cobre tornar
> esses dados **persistentes** entre execuções (arquivo/banco de dados) —
> por decisão da equipe, essa parte é implementada por último, depois que
> o cálculo, a validação e a visualização estiverem estáveis.

---
