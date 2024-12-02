# Livro: Artificial Intelligence: A Modern Approach (4th Global Edition)

# Capítulo 2
- agentes racionais
- aplicação de racionalidade (agente <-> ambientes)
- sistemas inteligentes
- agente
- ambiente
- acoplamento de agente e ambiente
- observação
- agente depende da natureza do ambiente
- categorização de ambientes
- propriedades do ambiente (influenciam o projeto de agentes)

Observe a importância da natureza do ambiente mencionada pelo autor. Por que ela é tão importante para observar o comportamento do agente?

Observe também a ênfase ao acoplamento de Agente e Ambiente, entendendo-os como elementos fundamentais ao longo da nossa disciplina.

## Tópico 2.1
Observe a Figura 2.1 e considere-a como uma arquitetura básica onde elementos serão adicionados ao longo de nossa disciplina, dando origem a novas arquiteturas. Quais elementos fazem parte dessa arquitetura agora?

Ainda no início desse tópico, um agente deve escolher a ação a realizar. É importante identificar de que depende a escolha da ação do agente, isto é, quais são os dois elementos considerados pelo autor?

Observe que o autor indica que o comportamento do agente pode ser descrito por uma “função de agente”, matematicamente falando uma função (portanto, estamos falando de um pseudocódigo também). É necessário entender: o que ela mapeia?


Na sequência, é necessário entender que, embora exista uma relação entre “função de agente” e “programa de agente”, estes são diferentes em termos práticos. Entenda essas diferenças. (Verifique o exemplo do aspirador de pó indicado pelo autor).
Observe a Figura 2.3 e entenda o propósito dela. Ela poderia ser de tamanho infinito?, argumente sua resposta.

## Tópico 2.2
Entenda a definição de consequencialismo, onde se avalia o comportamento de um agente por suas consequências. Ainda nesse contexto, está associada à sequência de estados (do ambiente) gerados no processo de busca almejando um estado final (do ambiente), este último considerado uma solução.

Aqui é onde entra a medida de desempenho (*performance measure*) que avalia qualquer sequência de estados de ambiente. É importante observar onde entra a medida de desempenho neste processo de busca.

Observar que essa medida de desempenho é proposta pelo projetista do agente racional ou é repassada ao usuário que utiliza o agente racional. Isso significa que nós somos responsáveis pela elaboração dessa medida de desempenho do agente racional. Leia o exemplo colocado para o agente aspirador de pó.

O autor menciona como regra geral: é melhor projetar medidas de desempenho considerando o que se deseja alcançar dentro do ambiente, em vez de pensar como o agente deve se comportar. Você poderia imaginar o impacto disso no momento de implementar em uma linguagem de programação?

Por outro lado, em relação à racionalidade, o autor menciona que esta depende de quatro “coisas” (página 58), e como o livro se centra em agentes racionais, é importante lembrar sempre desses pré-requisitos de racionalidade em agentes. Por fim, isso leva à definição de um agente racional!.

Leia o exemplo do agente aspirador de pó e saiba se ele é considerado racional ou não.

Em seguida, precisamos saber o que procuramos ao criar/projetar um agente, racionalidade ou onisciência?

O autor também menciona que um agente racional não somente coleta informações, mas também aprende com suas percepções. Leia os exemplos que consideram aprendizagem.

Finalmente, um agente racional deve ter como característica ser autônomo para poder ser independente ou se independizar de seu conhecimento prévio.

## Tópico 2.3

Antes de construir agentes racionais é necessário pensar primeiro no ambiente (de tarefas), isto é o problema. De fato o ambiente afeta diretamente o projeto do programa de agente.

Na sequencia é comentado a especificação de ambiente de tarefas, observar que essa especificação é uma descrição como em engenharia de software ao momento de especificar o software antes de construir/programar.

O acrônimo PEAS é o ponto chave na especificação. Além do aspirador de pó, na Figura 2.4 mostra outros exemplo. Leia a descrição detalhada deste último exemplo. Já na Figura 2.5 Mostra outros tipos de agentes e o PEAS correspondente. Assim como na engenharia de software isto pode passar naturalmente por ajustes cíclicos com o objetivo de que esta especificação seja o mais específico possível.

Por outro lado cada ambiente de tarefa tem diferentes propriedades que vão auxiliar na implementação dos agentes que estarão nestes ambientes. Estas propriedades se referem a:
* O ambiente de tarefa é totalmente/parcialmente/não observável pelo agente ?
* o ambiente de tarefas considera um agente ou múltiplos agentes ?
* O ambiente de tarefa é determinístico ou não ?
* O ambiente de tarefa é episódico ou sequencial? vale a pena ler esta propriedade e encontrar maiores detalhes
* O ambiente é estático ou dinâmico ?
* O ambiente é discreto ou contínuo ?
* O conhecimento/desconhecimento do agente sobre como funciona o ambiente de tarefas onde se encontra.

Figura 2.6 mostra vários exemplos de ambientes de tarefa e suas propriedades definidas.

## Tópico 2.4 

Finalmente neste tópico mostra qual a estrutura de agente a considerar quando formos implementar. 
Observe que literalmente se afirma que o trabalho de IA é : projetar um programa de agente que implemente a função de agente", isto é como vamos mapear das percepções para as ações.

Neste tópico ainda deixa claro que neste livro se concentra projetar esses programas de agentes.

### Tópico 2.4.1

Todos os programas de agente tem o mesmo esqueleto padrão: recebe as percepções dos sensores e retorna uma ação para os atuadores.

Apêndice B mostra o padrão do pseudocódigo utilizado no livro.

A Figura 2.7 é um exemplo de programa de agente dirigido por tabela para o problema do aspirador de pó da Figura 2.3

Leia o exemplo do táxi automatizado e como é feita a análise das percepções, P, e o tempo de vida, T, do agente. Qual é conclusão ?

Para finalizar este tópico é mostrado 4 tipos básicos de programas de agente:
* *Simple reflex agent* (o mais simples, ver Figura 2.3 e Figura 2.8, ignora o histórico de percepções, if-then-else, regra condição-ação, Figura 2.8 é específico e Figura 2.9 é uma abordagem geral ou mais genérica e seu programa de agente é mostrado na Figura 2.10. *observar na figura 2.10 a função RULE-MATCH pode ser o if-then-else ou poder ser uma tabela hash ou poder uma *Deep Learning* - rede neural artificial- !, trabalha muito bem em ambientes totalmente observáveis, em outros ambientes podem existir sérios problemas ou *loops* onde aleatoriedade pode ser uma alternativa);
* *Model-based reflex agents* (existe um estado interno do ambiente, é necessário saber como as mudanças estão acontecendo no ambiente -modelo de transição- e como o estado do ambiente é percebido pelo agente -modelo sensorial-, ver Figura 2.11, seu programa de agente está na Figura 2.12, lida bem em ambientes parcialmente observáveis, consegue dar seu melhor alternativa/shute para uma dada situação.);
* *Goal-based agents*; (O agente precissa alguma informação sobre o objetivo e combina essa informação com o modelo para escolher a ação que alcance o objetivo, ver Figura 2.13, envolve outros tópicos como busca e planejamento que procuram por uma sequencia de ações, tipo de agente mais flexível) 
* *Utility-based agents* (é utilizada uma medida de desempenho mais genérica  que irá permitir a comparação de diferentes estados de mundo/ambiente e determinar qual é mais útil!, utilizado quando existem conflito de objetivos, 'a utilidade fornece uma maneira pela qual a probabilidade de sucesso pode ser ponderada em relação à importância dos objetivos', ver Figura 2.14).

Nesse ponto é importante destacar que os autores do livro indicam que é possível construir todos esses agentes como '*learning agents*'. Ver Figura 2.15.

### Tópico 2.4.7

Observar na Figura 2.16 três formas de representar estados e transições entre esses estados.
* Atômico
* Fatorada
* Estruturada

