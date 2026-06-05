import pandas as pd 
#permite interagir com o sistema operacional 
import os    
#buscar arquivos usando padroes 
import glob
#garante que os dados estao no formato esperado antes de processar

from utils_log import log_decorator


# Função de extract que le e consolida os json:

#? Busca todos os .json da pasta "data" com glob
#? Lê cada arquivo como DataFrame e armazena numa lista (df_list)
#? Cada item de df_list é um DataFrame separado, um por arquivo
#? Concatenando os arquivos (juntando) e reinicia do zero para nao repetir:

def extrair_dados(pasta):  

    #!busca todos os arquivos que batem com esse padrão e retorna uma lista de caminhos:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))

    #! Uma list comprehension que percorre cada arquivo da lista e lê como DataFrame. 
    #! O resultado é uma lista de DataFrames:
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]

    #! junta todos os DataFrames da lista em um só, empilhando as linhas 
    #! e reinicia o indice do zero.
    df_total = pd.concat(df_list, ignore_index=True)

    return df_total


# Função que transforma:

def transformar_dados(df: pd.DataFrame):
    df['Receita'] = df['Quantidade'] * df['Venda']
    return df


# Função que da load em csv ou parquet:

def carregar_dados(df, formatos: list):
    for formato in formatos:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        elif formato == 'parquet':
            df.to_parquet( "dados.parquet", index=False)



# Função que junta tudo:
@log_decorator
def pipeline(pasta: str, formato: str):
    dados = extrair_dados(pasta) 
    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados, formato)




#? Local para teste, nao roda essa parte se importar
# if __name__ == "__main__":
#     pasta_argumento = "data"
#     print(extrair_dados(pasta=pasta_argumento))

