# radia.agua.util.py
"""Utilitário da Ilha proibida para mensagens no console.

LOG - https://bit.ly/Dev_Agile_23

EQUIPE Água 🌊

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Julia <julia@gmail.com>

Changelog
---------
.. versionadded::    23.11
    📰 🌊 Log multi plataforma (08).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""


class Log:
    """Console inteligente que usa self.do_print no desktop ou adiciona texto no html.

    """
    def __init__(self, level=0):
        self._level = level
        self.level = level
        self.doc = self.span = self.br = None
        try:
            from browser import document, html
            # noinspection PyUnresolvedReferences
            import javascript
            # importa um módulo que dá erro de importação quando não está no Brython

            _ = javascript.NULL
            self.doc, self.span, self.br = document["pydiv"], html.SPAN, html.BR
        except ImportError:
            self.log = self.do_print
            # instala "self.do_print" como o console de mensagens se não está no brython

    def log(self, level=None, *args):
        level = self._level if level is None else level
        _ = [self.doc <= self.span(str(tx)+self.br()) for tx in args if level >= self.level]

    def do_print(self, level=None, *args):
        level = self._level if level is None else level
        _ = [print(str(tx)) for tx in args if level >= self.level]


LG = Log()
