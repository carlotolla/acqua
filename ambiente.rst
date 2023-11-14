.. _modulo_ambiente:

Módulo Ambiente
===============

Define objetos sob controle da Ilha

.. mermaid::

    ---
    title: Objetos Representando o Ambiente
    ---
    classDiagram
        note "A ilha representa o jogo"
        CartaTesouro <|-- CartaAlagamento
        note for IlhaProibida "inicia baralho de tesouro\ninicia baralho de alagamento\ninicia grupo de jogadores"
        IlhaProibida <-- CartaTesouro
        IlhaProibida <-- CartaAlagamento

        class IlhaProibida{
            +List cartas_tesouro
            +List cartas_inunda
            +distribui()
        }
        class CartaTesouro{
            +str face
            +ativa()
        }
        class CartaAlagamento{
        }


Objetos do Ambiente
*********************

.. |br| raw:: html

    <br />&emsp;

.. automodule:: ilha
    :members:
    :undoc-members:
    :show-inheritance:
    :platform: Web
    :synopsis: Controle do Tabuleiro.


.. seealso::

   Principal :ref:`modulos_principal`

.. seealso::

   Module :ref:`modulo_jogador`

.. note::
   Objetos que controlam o ambiente.
