# -*- encoding=utf8 -*-
__author__ = "mathe"

from airtest.core.api import *

auto_setup(__file__)
assert exists(Template(r"fase4.png", threshold=0.75)), "Erro: O botão fase4 não existe na tela!"