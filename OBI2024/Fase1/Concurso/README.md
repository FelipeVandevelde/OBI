<h1 align="center">Concurso</h1>
<p align="center">
  <i>Nome do arquivo:</i> <b>concurso.c, concurso.cpp, concurso.java, concurso.js <i>ou</i> concurso.py</b>
</p>

Cláudia trabalha na OBI (Organização dos Bons Informáticos), que recentemente realizou um concurso para contratar novos funcionários. Agora, Cláudia tem a tarefa de determinar a *nota de corte* para o concurso. Chamamos de nota de corte a nota mínima necessária para ser aprovado no concurso. Ou seja, se a nota de corte do concurso for *C*, então todos os participantes com uma nota maior ou igual a *C* serão aprovados no concurso e todos com nota menor que *C* serão reprovados.

Seu chefe pediu para que Cláudia aprove no mínimo *K* candidatos do concurso para a próxima fase, mas ela também não quer que a nota de corte seja muito baixa. Por isso, Cláudia decidiu que a nota de corte deverá ser a maior nota *C* que faz com que no mínimo *K* candidatos sejam aprovados.

Sua tarefa é: dados o número *N* de candidatos, as notas *A_1, A_2, ..., A_N* dos candidatos e a quantidade mínima de aprovados *K*, diga qual deve ser a maior nota de corte *C* para que pelo menos *K* candidatos sejam aprovados.

## Entrada

A primeira linha da entrada contém dois inteiros, *N* e *K*, representando, respectivamente, o número de participantes e o número mínimo de candidatos que devem ser aprovados. 

A segunda linha da entrada contém *N* inteiros *A_i*, representando as notas dos participantes.

## Saída

Seu programa deve imprimir uma linha contendo um único inteiro *C*, a nota de corte que deve ser escolhida por Cláudia.

## Restrições

* *1 ≤ K ≤ N ≤ 500*
* *1 ≤ A_i ≤ * 100 para todo *1 ≤ i ≤ N*

## Infromações sobre a pontuação

A tarefa vale 100 pontos. Estes pontos estão distribuídos em subtarefas, cada uma com suas **restrições adicionais** às definidas acima.
* **Subtarefa 1 (0 pontos):** Esta subtarefa é composta apenas pelos exemplos mostrados abaixo. Ela não vale pontos, serve apenas para que você verifique se o seu programa imprime o resultado correto para os exemplos.
* **Subtarefa 2 (20 pontos):** *K = 1*.
* **Subtarefa 3 (20 pontos):** *K = 3*.
* **Subtarefa 4 (20 pontos):** *A_i ≤ 2*.
* **Subtarefa 5 (40 pontos):** Sem restrições adicionais.

Seu programa pode resolver corretamente todas ou algumas das subtarefas acima (*elas não precisam ser resolvidas em ordem*). Sua pontuação final na tarefa é a soma dos pontos de todas as subtarefas resolvidas corretamente por qualquer uma das suas submissões

## Exemplos


|Exemplo de entrada          |Exemplo de saída|
|:---------------------------|:---------------|
|3 1<br>92 83 98             | 98             |
|4 2<br>1 2 3 4              | 3              |
|5 3<br>20 20 10 20 30       | 20             |
|10 5<br>1 2 2 1 2 2 1 1 1 1 | 3              |