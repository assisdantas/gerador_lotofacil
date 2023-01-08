# Gerador Lotofácil
Gerador de jogos da lotofácil

Gerador de jogos da lotofácil usando pesos estátisticos obtidos de 2.707 resultados anteriores. Cada bola tem uma dezena com maior e menor probalidade de ser sorteada, estas foram mapeadas e assim, atribuído um peso específico para cada qual, que é levado em conta na hora da escolha pseudo-aleatória para geração dos jogos. É possível utilizar dezenas dos jogos anteriores, conforme estátisticas, pelo menos 5 números do concurso anterior se repetem no concurso seguinte.

Caso necessário é possível atualizar os resultados para processamento dos dados usando PowerBI, baixe o arquivo contendo os resultados em formato de planilha e prepare o arquivo conforme o arquivo de modelo na pasta do repositório. Para visualizar os dados, abra a pasta de trabalho do PowerBI e use os dados obtidos para alimentar as listas de pesos no código Python do projeto. O motivo do trabalho manual era aprender algumas funcionalidades do PowerBI. Resultados podem ser baixados em: https://asloterias.com.br/download-todos-resultados-lotofacil

Para executar, rode o comando no seu terminal

```
python joga.py
```

### Número de jogos
Escolha a quantidade de jogos que deseja que o script gere, quanto maior a quantidade maior o tempo e memória utilizada.

### Usar concurso anterior [Sim ou Não]
Você também pode selecionar números que saíram no concurso anterior, estatisticamente pelo menos 5 das dezenas do concurso anterior se repetirão no próximo concurso.

### Entre com o resultado anterior
Se você optou por usar o último concurso como base, insira as dezenas do último sorteio separadas por vírgula e sem espaço. Para os números 1 a 9 não utilize 0 na frente. Exemplo: 1,2,3,5,6,13,14,16,18,19,21,22,23,24,25

### Quantas dezenas utilizar do último sorteio [entre 6 e 12 ou 0]
Informe quantas dezenas você deseja utilizar do último sorteio, geralmente entre 7 e 11 dezenas repetidas são uma boa escolha, você pode consultar as estátisticas em: https://www.lotodicas.com.br/lotofacil/estatisticas. Se você optar por não utilizar o concurso anterior, ainda poderá digitar 0.

### Número de dezenas [15 ou 16]
Escolha quantas dezenas o script deve colocar em cada jogo. O limite é 16 devido a verificação das estátisticas que são mais difíceis de alcançar caso o jogo possua mais de 16 dezenas por jogo. As estatísticas limitam-se a 15 dezenas pois todos os resultados anteriores possuem 15 dezenas.

### Número de dezenas por passo [Entre 10 e 20]
Escolha quantas dezenas o script deve eleger para que seja selecionado aleatóriamente 1 e adicionado ao jogo por passo.

Resultados obtidos em 06 de Janeiro de 2023
