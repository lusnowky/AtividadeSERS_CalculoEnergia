  ----------------------------------- -----------------------------------
  **User Story:**                     Implementar o cálculo da média do
                                      consumo mensal registrado em kWh.

  **Critérios de aceite**             Exibir o que está sendo calculado
                                      e como chegou na média mensal.

  **Componentes envolvidos.**         Interface/dados/resumo
                                      individual/resumo geral.

  **Dependência.**                    Análise do problema e da
                                      importância a ser resolvido; Ajuste
                                      na programação; análise final e
                                      entrega

  **Condição de conclusão.**          Testar o cálculo da média com
                                      diferentes quantidades.
  ----------------------------------- -----------------------------------

  ----------------------------------- -----------------------------------
  **User Story:**                     Quero entender exatamente o que
                                      significa o resultado apresentado,
                                      para saber o que está sendo
                                      calculado.

  **Critérios de aceite**             Exibir uma explicação indicando
                                      exatamente a quantidade de intens que estão sendo
                                      calculados e o que o resultado
                                      representa.

  **Componentes envolvidos**          Interface/resultado/explicação do
                                      cálculo.

  **Dependência**                     Análise do problema do resultado
                                      pouco claro; definição do cálculo e
                                      da informação que deverá ser
                                      apresentada.

  **Condição de conclusão**           Testar o resultado apresentado e
                                      verificar se a explicação permite
                                      compreender corretamente o cálculo.
  ----------------------------------- -----------------------------------

  ----------------------------------- -----------------------------------
  **User Story:**                     Quero informar meu consumo mensal
                                      real, para que o cálculo
                                      represente meu consumo de energia.

  **Critérios de aceite**             Permitir informar o consumo de cada item individualmente manualmente
                                      para um cálculo mais preciso.

  **Componentes envolvidos**          Interface/dados de consumo/cálculo.

  **Dependência**                     Análise da limitação do cálculo
                                      atual; ajuste da entrada de dados
                                      para receber o consumo mensal em
                                      kWh.

  **Condição de conclusão**           Testar o cadastro de diferentes
                                      valores de consumo mensal em kWh e
                                      verificar se eles são utilizados
                                      corretamente no cálculo.
  ----------------------------------- -----------------------------------

  ----------------------------------- -----------------------------------
  **User Story:**                     Quero saber qual foi meu maior
                                      consumo, para identificar
                                      automaticamente meu pior mês.

  **Critérios de aceite**             Identificar automaticamente o maior
                                      consumo registrado.

  **Componentes envolvidos**          Dados de consumo/cálculo/resumo
                                      individual.

  **Dependência**                     Cadastro de vários meses de
                                      consumo; cálculo e comparação dos
                                      valores registrados.

  **Condição de conclusão**           Testar com diferentes quantidades
                                      de consumo e verificar se o sistema
                                      identifica corretamente o maior
                                      valor.
  ----------------------------------- -----------------------------------

  ----------------------------------- -----------------------------------
  **User Story:**                     Quero saber em qual mês e ano mais
                                      consumi energia, para identificar o
                                      período de maior consumo.

  **Critérios de aceite**             Informar o mês/ano correspondente
                                      ao maior consumo registrado.

  **Componentes envolvidos**          Histórico de consumo/dados de mês e
                                      ano/cálculo/resumo.

  **Dependência**                     Cadastro de vários meses e
                                      identificação automática do maior
                                      consumo.

  **Condição de conclusão**           Testar registros de diferentes
                                      meses e anos e verificar se o
                                      sistema informa corretamente o
                                      mês/ano do maior consumo.
  ----------------------------------- -----------------------------------

  ----------------------------------- -----------------------------------
  **User Story:**                     Quero entender meu resultado
                                      rapidamente, para ter uma visão
                                      geral do meu consumo de energia.

  **Critérios de aceite**             Criar um resumo energético
                                      apresentando as principais
                                      informações do consumo.

  **Componentes envolvidos**          Interface/dados/resumo
                                      individual/resumo geral.

  **Dependência**                     Implementação dos cálculos de média
                                      e maior consumo e disponibilidade
                                      do histórico de consumo.

  **Condição de conclusão**           Testar diferentes registros de
                                      consumo e verificar se o resumo
                                      apresenta corretamente as
                                      informações calculadas.
  ----------------------------------- -----------------------------------

  ----------------------------------- -----------------------------------
  **User Story:**                     Quero visualizar meu consumo, para
                                      conseguir comparar os valores
                                      registrados ao longo dos meses.

  **Critérios de aceite**             Criar texto representando
                                      o consumo registrado.

  **Componentes envolvidos**          Interface/histórico de
                                      consumo/gráfico mensal/dados.

  **Dependência**                     Cadastro e registro de vários meses
                                      de consumo; organização dos dados
                                      para apresentação gráfica.

  **Condição de conclusão**           Testar diferentes quantidades de
                                      meses cadastrados e verificar se o
                                      gráfico representa corretamente os
                                      respectivos consumos.
  ----------------------------------- -----------------------------------

  ----------------------------------- -----------------------------------
  **User Story:**                     Quero receber uma validação quando
                                      informar 0 ou um valor inválido,
                                      para evitar erros no cálculo.

  **Critérios de aceite**             Criar validações para impedir
                                      entradas inválidas ou inadequadas.

  **Componentes envolvidos**          Interface/campos de
                                      entrada/validação/mensagens de
                                      erro.

  **Dependência**                     Definição dos valores aceitos para
                                      o consumo mensal e dos
                                      comportamentos para entradas
                                      inválidas.

  **Condição de conclusão**           Testar entradas com 0, valores
                                      inválidos e valores válidos e
                                      verificar se o sistema responde
                                      corretamente em cada situação.
  ----------------------------------- -----------------------------------
