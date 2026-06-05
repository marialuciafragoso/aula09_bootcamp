#! SEM DECORADOR

# from loguru import logger

# logger.add("meu_log.log", level="CRITICAL")

# def soma(x, y):
#     try:
#         soma = x + y 
#         logger.info("Voce digitou os valores corretos!")
#         return soma 
#     except:
#         logger.critical("Voce tem que digitar valores corretos")

# COM DECORADOR 
from utils_log import log_decorator
@log_decorator
def soma(x,y):
    return x + y 

soma(2, 3)
soma(1000, 4)
