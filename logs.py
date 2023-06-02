#!/usr/bin/env python3

import os
import logging

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("diogo", log_level)
ch = logging.StreamHandler() # COnsole/terminal/stderr
ch.setLevel(log_level)
fmt = logging.Formatter(
	'%(asctime)s %(name)s %(levelname)s '
	'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)


"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuario")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execucao")
log.critial("Erro geral ex: banco de dados sumiu")
"""

print("---")

try:
	1 / 0
except ZeroDivisionError as e:
	log.error("Deu erro %s", str(e))
