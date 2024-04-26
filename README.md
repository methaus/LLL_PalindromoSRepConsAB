# LLL_PalindromoSRepConsAB
a) Construa uma GLC para uma linguagem específica de sua escolha:
  A Gramática Livre de Contexto (GLC) fornecida é para a linguagem de palíndromos sem repetição consecutiva de 'a' e 'b'

b) Identifique e explique a LLC gerada pela GLC construída.
   A Linguagem Livre de Contexto (LLC) gerada pela GLC é composta por todas as strings que são palíndromos e não possuem 'a' ou 'b' consecutivos. Ou seja, cada 'a' ou 'b' na string é seguido por um caractere diferente. Por exemplo, algumas strings na LLC gerada por esta GLC seriam: "", "a", "aba", "ababa", "abababa"

c) Discuta as propriedades da GLC e da LLC encontradas na sua atividade.
   A maquina utiliza recursão para aplicar as regras de produção da GLC em cada caractere da string até que a string final seja gerada. O parâmetro limite é uma condição de parada que limita o tamanho da string de saída para a geração recursiva. Ela é não-ambigua devido a definição de "§" para derivação à esquerda.
