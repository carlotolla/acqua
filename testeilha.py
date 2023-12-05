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
import ilha


class TestGeralIlha(unittest.TestCase):
    def setUp(self, objects=None):
        self.ilha = ilha.IlhaProibida()

    def test_cartas_inunda_ilha(self):
        self.assertIn(0, self.ilha.cartas_inunda)
        self.assertEqual(24, len(self.ilha.cartas_inunda))

    def test_cartas_tesouro_ilha(self):
        self.assertIsInstance(self.ilha.cartas_tesouro[0], ilha.CartaTesouro)
        # print([(ct) for ct in self.ilha.cartas_tesouro])
        self.assertIn("a", str(self.ilha.cartas_tesouro))
        self.assertEqual(28, len(self.ilha.cartas_tesouro))
        self.assertEqual(5, len(
            [1 for ct in self.ilha.cartas_tesouro if "a" == str(ct)]))


if __name__ == '__main__':
    unittest.main()

