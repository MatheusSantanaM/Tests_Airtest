# -*- encoding=utf8 -*-
__author__ = "mathe"

from airtest.core.api import *

auto_setup(__file__)
assert exists(Template(r"voltar.png", threshold=0.75)), "Erro: O botão voltar não existe na tela"