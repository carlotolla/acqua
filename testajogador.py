"""Teste da Ilha.


LOG - https://bit.ly/Dev_Agile_23

EQUIPE Água 🌊

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Julia <julia@gmail.com>

Changelog
---------
.. versionadded::    23.11
   |br| Classes IlhaProibida, CartaTesouro, CartaAlagamento (07).
   |br| Melhora a documentação do módulo (08).

|   **Open Source Notification:** This file is part of  **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU GPL v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>_`
_    `UFRJ <https://ufrj.br/>`_.
"""
import unittest
import jogador
from util import LG
LG.level = 2


class TestRodada(unittest.TestCase):
    def setUp(self, objects=None):
        self.jogadores = [
            jogador.Jogador("Nav0", self), jogador.Explorador("Ex1", self),
            jogador.Explorador("Ex2", self),
        ]
        self.rodada = jogador.Rodada(self.jogadores)
        self.removed = []

    def remove(self, peao):
        self.removed.append(peao)

    def move(self, peao, destino, vai):
        if destino in [2, 4, 6, 8]:
            vai()

    def test_rodada(self):
        self.assertIn(self.jogadores[0], self.rodada.jogadores)
        self.assertEqual(3, len(self.rodada.jogadores))

    def test_3_rodadas(self):
        jog = iter(self.rodada)
        self.assertIn("0", next(jog).nome)
        self.assertIn("1", next(jog).nome)
        self.assertIn("2", next(jog).nome)
        self.assertIn("0", next(jog).nome)
        self.assertIn("1", next(jog).nome)
        self.assertIn("2", next(jog).nome)
        self.assertEqual(3, len(self.rodada.jogadores))

    def test_3_turnos(self):
        jog = iter(self.rodada)
        jogador = next(jog)
        self.assertIn("0", jogador.nome)
        jogador.age(0, 0)
        jogador.age(1, 0)
        jogador.age(1, 2)
        self.assertIn(jogador, self.removed)
        jogador.age(2, 4)


if __name__ == '__main__':
    unittest.main()

