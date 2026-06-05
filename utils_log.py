from loguru import logger 
from sys import stderr
from functools import wraps

logger.remove()

logger.remove()

logger.add(
    "meu_arquivo_de_logs.log",
    format="{time} {level} {message} {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs_critical.log",
    format="{time} {level} {message} {file}",
    level="ERROR",
    delay=True
)

def log_decorator(func):
    #Faz a função decorada manter o nome e documentação originais. 
    #Sem isso, toda função decorada passaria a se chamar wrapper, o que quebraria os logs.
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função
    return wrapper