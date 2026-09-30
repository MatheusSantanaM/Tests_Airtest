# -*- encoding=utf8 -*-
__author__ = "mathe"

from airtest.core.api import *

auto_setup(__file__)
assert exists(Template(r"fase3.png", threshold=0.75)), "Erro: O botão fase3 não existe na tela!"


