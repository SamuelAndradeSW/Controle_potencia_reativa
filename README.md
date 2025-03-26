
# Fluxo de Potência Não-Linear com controle de geração de potência reativa em Barra PV para o Sistema IEEE 24 Barras.

Este trabalho abordou o cálculo do fluxo de potência em sistemas de potência, utilizando o método de Newton-Raphson com controles de limites nas barras PQ e PV. Foram apresentados os fundamentos teóricos do cálculo de fluxo de potência não linear e a importância dos controles de limites para garantir a estabilidade e segurança operacional do sistema elétrico.

A metodologia adotada envolveu a revisão bibliográfica, a formulação das equações de fluxo de potência não lineares e a implementação computacional do método de Newton-Raphson em Python. Os controles de limites foram incorporados ao processo de cálculo, com o objetivo de evitar violações dos limites de potência ativa e reativa nas barras PQ e PV.

Através da simulação e análise dos resultados, foi possível verificar a eficácia do método de Newton-Raphson com os controles de limites. O método demonstrou sua capacidade de convergência rápida e precisão na obtenção da solução do fluxo de potência. Os controles de limites mostraram-se essenciais para garantir a estabilidade do sistema elétrico, evitando sobrecargas e instabilidades nas barras PQ e PV.

A implementação do método de Newton-Raphson em Python proporcionou uma solução
eficiente e flexível, permitindo a análise de casos de estudo de forma rápida e precisa. A programação computacional facilitou a tomada de decisões e o gerenciamento do sistema elétrico, contribuindo para uma operação confiável e segura.

Em conclusão, este trabalho destacou a importância do cálculo do fluxo de potência com
controles de limites nas barras PQ e PV. O método de Newton-Raphson, aliado aos controles de limites, é uma abordagem efetiva para garantir a estabilidade e segurança operacional de sistemas de potência complexos. Os resultados obtidos fornecem uma base sólida para futuras pesquisas e desenvolvimento de técnicas avançadas de controle e operação de sistemas elétricos.




## 1 - Introdução

A análise do fluxo de potência é uma ferramenta fundamental em sistemas de potência, pois
visa garantir sua estabilidade e segurança operacional. O fluxo de potência é calculado levando em consideração as características dos elementos do sistema e as condições de carga. Existem abordagens lineares e não lineares para o cálculo do fluxo de potência, sendo que as abordagens não lineares são aplicáveis a sistemas de potência mais complexos.

Dentre as técnicas iterativas disponíveis, destaca-se o método de Newton-Raphson, ampla-
mente utilizado na resolução de cálculos de fluxo de potência não lineares. Esse método é
conhecido por sua rápida convergência e precisão na obtenção da solução. Para implementar
o método de Newton-Raphson, é necessário construir um modelo matemático do sistema de
potência, considerando as equações de fluxo de potência e restrições. Uma opção comumente
utilizada para essa implementação é a linguagem de programação Python.

Este trabalho tem como objetivo apresentar os fundamentos teóricos do cálculo de fluxo de
potência em sistemas de potência, com ênfase nos cálculos não lineares e na implementação
prática do método de Newton-Raphson utilizando Python. Será abordada a importância do
cálculo de fluxo de potência para garantir a estabilidade e segurança do sistema elétrico, além de demonstrar uma aplicação prática do método de Newton-Raphson em Python para resolver problemas de fluxo de potência não lineares.

Além disso, neste estudo, será incorporado o controle de limites nas barras PQ (Potência
Reativa e Potência Ativa Constantes) e PV (Potência Ativa Constante e Tensão Variável). Esses controles de limites são essenciais para evitar sobrecargas e instabilidades nas barras do sistema de potência, garantindo um funcionamento adequado e seguro.
Por meio deste estudo, será possível compreender os conceitos essenciais do cálculo de fluxo de potência, a importância de sua aplicação em sistemas de potência e a utilização do método de Newton-Raphson como uma ferramenta eficaz para solucionar problemas de fluxo de potência não lineares com o auxílio da programação em Python, incluindo a implementação de controles de limites nas barras PQ e PV.
## 3 - Desenvolvimento

O cálculo do fluxo de potência não linear é um problema matemático fundamental em
sistemas de potência, que envolve a solução de um sistema de equações não lineares. No contexto deste trabalho, consideramos um sistema elétrico de potência com n barras. As equações de fluxo de potência descrevem as relações entre as variáveis de potência ativa e reativa, tensões e ângulos de fase das barras. Para as barras PQ e PV, as equações de fluxo de potência podem ser representadas como:

![equações](https://github.com/SamuelAndradeSW/fluxo_de_potencia/blob/main/fluxo%20de%20potencia/data/equa%C3%A7%C3%B5es%20de%20fluxo%20de%20pot%C3%AAncia.png)

onde Pk e Qk são as componentes ativas e reativas da potência na barra k, Vk é a magnitude da tensão na barra k, Gkm e Bkm são as partes real e imaginária da admitância entre as barras k e m, respectivamente, e θkm é a diferença de fase entre as barras k e m.

A solução do sistema de equações não lineares pode ser obtida por meio de métodos numéricos, como o método de Newton-Raphson. O método de Newton-Raphson é um método iterativo que busca a solução do sistema de equações a partir de um valor inicial. A cada iteração, o método calcula a matriz jacobiana do sistema de equações, que é uma matriz n × n cujos elementos são as derivadas parciais das equações em relação às variáveis do sistema. Em seguida, o método calcula a solução aproximada do sistema de equações por meio de um processo de correção iterativo.

Para incorporar os controles de limites no cálculo do fluxo de potência, é necessário adicionar restrições às variáveis do sistema. Nas barras PQ, os limites são definidos para a potência ativa e reativa, enquanto nas barras PV, os limites são estabelecidos para a potência ativa e a magnitude da tensão. Durante a execução do método de Newton-Raphson, são realizadas verificações para garantir que as variáveis estejam dentro dos limites permitidos. Caso alguma violação seja identificada, são aplicados mecanismos de ajuste para manter as variáveis dentro dos limites operacionais.

Neste trabalho, a metodologia adotada envolve a revisão bibliográfica sobre o cálculo do fluxo de potência em sistemas de potência, com ênfase nas técnicas de controle de limites. Em seguida, foram formuladas as equações de fluxo de potência não lineares considerando os controles de limites para as barras PQ e PV. A implementação computacional foi realizada utilizando a linguagem de programação Python, incorporando os mecanismos de controle de limites durante a execução do método de Newton-Raphson. foram realizadas simulações utilizando dados fornecidos do sistema de 24 barras para avaliar a eficácia dos controles de limites na estabilidade e segurança operacional do sistema elétrico de potência.

Por meio deste estudo, obtem-se uma compreensão aprofundada dos aspectos teóricos
e práticos do cálculo do fluxo de potência com controles de limites. A análise dos resultados permitirá verificar a eficácia desses controles na garantia da estabilidade e segurança operacional dos sistemas de potência, contribuindo para o avanço da área e fornecendo insights para aplicações práticas em sistemas elétricos reais.


## 4 Resultados:

Os resultados obtidos mostraram uma convergência do método em um número satisfatório
de iterações, indicando que o algoritmo foi bem-sucedido em calcular o fluxo de potência no sistema elétrico em questão.

## 5 Conclusão

Neste trabalho, foi realizado um estudo sobre o cálculo do fluxo de potência em sistemas de potência utilizando o método de Newton-Raphson, com o objetivo de incorporar controles de limites nas barras PQ e PV. A partir da revisão bibliográfica e da implementação computacional, foram obtidos resultados relevantes que contribuem para a compreensão e aplicação prática desse método.

Ao analisar os resultados, verificou-se que o método de Newton-Raphson é eficaz na determi- nação do fluxo de potência em sistemas de potência não lineares. Através da implementação dos controles de limites, foi possível garantir a estabilidade e a segurança operacional do sistema elétrico, evitando violações dos limites de potência ativa e reativa nas barras PQ e PV.

Observou-se que o controle de limites desempenha um papel crucial na operação confiável
do sistema elétrico. Ao monitorar e ajustar as variáveis de fase e magnitude, é possível evitar sobrecargas, instabilidades e outros problemas que possam comprometer a operação adequada do sistema.

Além disso, a utilização da linguagem de programação Python proporcionou uma implemen-
tação eficiente e flexível do método de Newton-Raphson com os controles de limites. Portanto,  este estudo evidencia a importância do cálculo do fluxo de potência com controles de limites nas barras PQ e PV. A aplicação do método de Newton-Raphson, aliado à implementação dos controles de limites, é uma abordagem efetiva para garantir a estabilidade e segurança operacional de sistemas de potência complexos.

Este trabalho contribui para o avanço do conhecimento na área de sistemas de potência,
fornecendo uma base sólida para futuras pesquisas e desenvolvimento de técnicas mais avançadas de controle e operação de sistemas elétricos. A partir desses resultados, é possível aprimorar ainda mais as técnicas de controle de limites e explorar outros métodos e algoritmos para análise e gerenciamento de sistemas de potência de grande porte.

## Referência

Monticelli, Alcir José. Fluxo de carga em redes de energia elétrica. São Paulo: Editora
Blucher, 1983.
