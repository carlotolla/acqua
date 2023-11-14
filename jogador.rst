.. _modulo_jogador:

Módulo Jogador
===============

A descrição dos objetos controlados pelo Jogador

.. mermaid::

    ---
    title: Objetos Definindo o Jogador
    ---
    classDiagram
        note "Este módulo tem objetos controlado pelo Jogador"
        note for Jogador "recebe cartas de tesouro\n realiza ações:\n- move peão\n- troca cartas\n- recupera tesouro"
        Jogador <--> MaoJogador

        class Jogador{
            +str nome
            +List cartas
            +recebe()
            +age_turno()
        }
        class MaoJogador{
            -Jogador dono
        }


Objetos do Jogador
*********************

.. |br| raw:: html

    <br />&emsp;

.. automodule:: jogador
    :members:
    :undoc-members:
    :show-inheritance:
    :platform: Web
    :synopsis: Controle do Jogador.


.. seealso::

   Principal :ref:`modulos_principal`

.. seealso::

   Ambiente :ref:`modulo_ambiente`

.. note::
   Descreve os objetos que o jogador controla.
