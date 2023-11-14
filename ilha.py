# radia.agua.ilha.py
# noinspection GrazieInspection
"""A Ilha é o módulo de estruturação e início do jogo.

Classes neste módulo:
    - :py:class:`IlhaProibida` Ponto central de Construção do jogo.
    - :py:meth:`IlhaProibida.distribuir_cartas_tesouro` Distribuição de cartas tesouro.
    - :py:class:`CartaTesouro` Recursos necessários para resgatar tesouros.
    - :py:class:`CartaAlagamento` Controle ambiental de defesa da Ilha.


LOG - https://bit.ly/Dev_Agile_23

EQUIPE Água 🌊

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
.. codeauthor:: Julia <julia@gmail.com>

Changelog
---------
.. versionadded::    23.11
   |br| Classes IlhaProibida, CartaTesouro, CartaAlagamento (07).
   |br| Melhora a documentação do módulo (08).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
from util import LG


class IlhaProibida:
    """ Ponto central de Construção do jogo.

    """
    def __init__(self):
        from random import shuffle
        # noinspection SpellCheckingInspection
        baralho_tesouro = bt = list("tafv" * 5 + "dd" + "hhh")
        baralho_alaga = ba = list("eee")
        self.cartas_tesouro = [CartaTesouro(face=carta) for carta in bt]
        # recursos do jogador para realizar capturas, drenagem e movimentos
        self.cartas_tesouro += [CartaAlagamento(face=carta) for carta in ba]
        # acrescido de um conjunto de cartas que causam uma enchente
        self.cartas_inunda = list(range(24))
        shuffle(self.cartas_inunda)
        shuffle(self.cartas_tesouro)
        # abaixa um terreno que fica alagado ou afunda no oceano
        LG.log(0, "Bem vindos à Ilha Proibida - montagem do tabuleiro")
        LG.log(0, "cartas tesouro:", self.cartas_tesouro)
        LG.log(0, "cartas de inundação:", self.cartas_inunda)

    def distribuir_cartas_tesouro(self):
        """ Distribuição de cartas Tesouro no início e a cada fim de turno

        :return: None
        """
        ...


class CartaTesouro:
    """Recursos necessários para resgatar tesouros.

    """
    def __init__(self, face):
        self.face = face
        # LG.log(0, "Bem vindos à Ilha Proibida - montagem do tabuleiro")

    def __repr__(self):
        return self.face


class CartaAlagamento(CartaTesouro):
    """ Controle ambiental de defesa da Ilha.

    """
    def __init__(self, face):
        super().__init__(face)
        # LG.log(0, "Bem vindos à Ilha Proibida - montagem do tabuleiro")

    def __repr__(self):
        return "🌊"  # self.face


if __name__ == "__main__":
    IlhaProibida()
