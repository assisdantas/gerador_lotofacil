# Gerador Lotofácil
Gerador de jogos da lotofácil

Gerador de jogos da lotofácil usando pesos estátisticos obtidos dos 2.707 resultados anteriores. Cada bola tem uma dezena com maior e menor probalidade de ser sorteado, estas foram mapeadas e pesadas usando estátisca. Cada dezena tem um peso específico que é levado em conta na hora da escolha pseudo-aleatória para geração dos jogos.

Caso necessário é possível atualizar os resultados para processamento dos dados usando PowerBI, baixe o arquivo contendo os resultados em formato de planilha e prepare o arquivo conforme o arquivo de modelo na pasta do repositório. Para visualizar os dados, abra a pasta de trabalho do PowerBI e use os dados obtidos para alimentar as listas de pesos no código Python do projeto. O motivo do trabalho manual era aprender algumas funcionalidades do PowerBI. Resultados podem ser baixados em: https://asloterias.com.br/download-todos-resultados-lotofacil

Para executar, rode o comando no seu terminal

```
python joga.py
```

### Número de jogos
Escolha a quantidade de jogos que deseja que o script gere, quanto maior a quantidade maior o tempo e memória utilizada.

### Número de dezenas [15 ou 16]
Escolha quantas dezenas o script deve colocar em cada jogo. O limite é 16 devido a verificação das estátisticas que são mais difíceis de alcançar caso o jogo possua mais de 16 dezenas por jogo. As estatísticas limitam-se a 15 dezenas pois todos os resultados anteriores possuem 15 dezenas.

### Número de dezenas por passo [Entre 10 e 20]
Escolha quantas dezenas o script deve eleger para que seja selecionado aleatóriamente 1 e adicionado ao jogo por passo.
