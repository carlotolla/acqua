# radia.agua.jogador.py
# SPDX-License-Identifier: GPL-3.0-or-later
"""Classes Relacionadas com o Jogador.

LOG - https://bit.ly/Dev_Agile_23

EQUIPE Água

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Julia <julia@gmail.com>

Changelog
---------
.. versionadded::    23.11
    Classe Jogador e MaoJogador (07).

|   **Open Source Notification:** Part of  program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU GPL v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_
|   - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from util import LG


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


class Jogador:
    def __init__(self, nome="Navegador", terreno=None):
        self.terreno = terreno
        self.round = round
        self.nome = nome
        self.mao = MaoJogador(dono=self)
        self.atos = [self._nada, self._move, self._drena]
        LG.log(0, f"{self.nome} se apresentando")

    def rodar(self, rodada):
        self.round = rodada

    def age(self, ato=0, destino=0):
        def agir():
            return self.atos[ato](destino)
        self.round.age(self, agir)

    def __agir(self, ato, destino=0):
        return lambda: ato(destino)

    def _nada(self, destino=0):
        pass

    def _sai(self):
        self.terreno.remove(self)

    def _move(self, destino=0):
        self.terreno.move(self, destino, self._sai)

    def _drena(self, destino=0):
        self.terreno.drena(self, destino)


class Explorador(Jogador):
    def __init__(self, nome="Explorador", terreno=None):
        super().__init__(nome=nome, terreno=terreno)

    def _move(self, destino=0):
        self.terreno.movex(self, destino, self._sai)

    def _drena(self, destino=0):
        self.terreno.drenax(self, destino)


class MaoJogador:
    def __init__(self, dono, cartas=()):
        self.dono = dono
        self.cartas = cartas
        LG.log(0,
               f"A mão do {self.dono.nome} possui {len(self.cartas)} cartas")


# @singleton
class Rodada:
    def ___new__(cls, *args, **kwargs):
        if not hasattr(cls, '_rodada'):
            cls._rodada = super(Rodada, cls).__new__(cls, *args, **kwargs)
        return cls._rodada

    def __init__(self, jogadores=()):
        round = self

        class Turno:
            def __init__(self, jogador):
                self.jogador = jogador
                self.atos = 3
                self.round = iter(round)

            def go(self, act):
                act()

            def gone(self, act):
                pass

            def inicia(self):
                self.atos = 3

            def __iter__(self):
                self.atos = [self.go] * 3 + [self.gone] * 100
                return (jog for jog in self.atos)
        [jog.rodar(self) for jog in jogadores]
        self.rodadas = jogadores * 1000
        self.jogadores = jogadores
        self.__turno = Turno
        self.turnos = {}

    def age(self, jogador, jogada):
        return next(self.turnos[jogador])(jogada)

    def __iter__(self):
        def new_round(jogador):
            self.turnos[jogador] = iter(self.__turno(jogador))
            return jogador
        self.rodadas = self.jogadores * 1000
        return (new_round(jog) for jog in self.rodadas)

    def ___iter__(self):
        for jogador in self.rodadas:
            yield jogador


if __name__ == "__main__":
    Jogador()
