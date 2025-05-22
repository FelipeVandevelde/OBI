<h1 align="center">Placas de Carro</h1>
<p align="center">
  <i>Nome do arquivo:</i> <b>placas.c, placas.cpp, placas.java, placas.js <i>ou</i> placas.py</b>
</p>

As placas usadas nos carros em circulação no Brasil possuem dois padrões com formatos diferentes: algumas placas estão no antigo padrão Brasileiro, enquanto outras estão no novo padrão Mercosul.

O antigo padrão Brasileiro é sempre formado por 8 caracteres:

* os três primeiros caracteres são letras maiúsculas (de **A** a **Z**);
* o quarto caractere é um hífen (-);
* os últimos quatro caracteres são dígitos (de **0** a **9**).

Por exemplo, OBI-2024 é uma placa válida no antigo padrão Brasileiro.

O novo padrão Mercosul, por sua vez, é sempre formado por 7 caracteres:

* os três primeiros caracteres são letras maiúsculas;
* o quarto caractere é um dígito;
* o quinto caractere é uma letra maiúscula;
* os últimos dois caracteres são dígitos.

Assim, **OBI2P24** é uma placa válida no novo padrão Mercosul.

Há também um grande contigente de carros em situação irregular – carros com placas falsificadas que não estão nem no antigo padrão Brasileiro, nem no novo padrão Mercosul. Por exemplo, um carro com a placa **OBI-24** está em situação irregular, pois a placa não é válida em nenhum dos dois padrões.


O Departamento Nacional de Trânsito identificou que seus funcionários gastam muito tempo verificando manualmente quais placas estão em qual padrão e quais são falsificadas. Por isso, eles pediram sua ajuda para automatizar o processo: dada uma placa formada por uma sequência de letras maiúsculas, dígitos e hífens, determine se a placa está no antigo padrão Brasileiro, está no
novo padrão Mercosul, ou é uma placa falsificada.

## Entrada

A entrada é composta de uma única linha, contendo uma sequência de caracteres representando a placa a ser analisada.

## Saída

Seu programa deverá imprimir uma linha contendo um único número inteiro:

* 1, se a placa está no antigo padrão Brasileiro;
* 2, se a placa está no novo padrão Mercosul;
* 0, se a placa é falsificada.

## Restrições

* A placa possui entre 6 e 10 caracteres.
* Cada caractere da placa é uma letra maiúscula (de **A** a **Z**), um dígito (de **0** a **9**) ou um hífen
(o caractere -).

## Infromações sobre a pontuação

A tarefa vale 100 pontos. Estes pontos estão distribuídos em subtarefas, cada uma com suas **restrições adicionais** às definidas acima.
* **Subtarefa 1 (0 pontos):** Esta subtarefa é composta apenas pelos exemplos mostrados abaixo. Ela não vale pontos, serve apenas para que você verifique se o seu programa imprime o resultado correto para os exemplos.
* **Subtarefa 2 (40 pontos):** É garantido que a placa está ou no antigo padrão Brasileiro, ou no novo padrão Mercosul (ou seja, ela não é falsificada).
* **Subtarefa 3 (60 pontos):** Sem restrições adicionais.

Seu programa pode resolver corretamente todas ou algumas das subtarefas acima (*elas não precisam ser resolvidas em ordem*). Sua pontuação final na tarefa é a soma dos pontos de todas as subtarefas resolvidas corretamente por qualquer uma das suas submissões

## Exemplos


|Exemplo de entrada|Exemplo de saída|
|:-----------------|:---------------|
|OBI-2024          | 1              |
|OBI2P24           | 2              |
|OBI-24            | 0              |
|XYZ-1234          | 1              |
|A1B2C3D4E5        | 0              |