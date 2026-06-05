# Aula 09 — Decoradores e Logs

Continuação da aula 08, onde o pipeline ETL foi construído. Aqui o foco foi adicionar **decoradores** e **logs estruturados** ao projeto existente.

## O que veio da aula 08

O `etl.py` e o `pipeline.py` já existiam — o ETL lê arquivos JSON da pasta `data/`, calcula a coluna `Receita` e salva em `.csv` e `.parquet`. O `pipeline.py` orquestra essas etapas em sequência.

## O que foi adicionado aqui

- `utils_log.py` — decorator `@log_decorator` usando `loguru`, que registra automaticamente chamadas, retornos e exceções de qualquer função decorada
- `exemplo.py` — comparação direta entre log manual e log via decorador na mesma função `soma()`
- Dois arquivos de log gerados: um para INFO e outro só para erros (ERROR+)

## Estrutura

```
aula09/
├── data/               # JSONs de entrada
├── etl.py              # extract, transform, load
├── pipeline.py         # orquestrador
├── utils_log.py        # @log_decorator
├── exemplo.py          # exemplos de uso do decorador
└── meu_arquivo_de_logs.log
```