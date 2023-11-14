
{'date': 'Tue Nov 07 2023 11:40:17.645 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 40
    Jogador()
  module <module> line 26
    self.mao = MaoJogador(dono=self)
  module <module> line 35
    print(f"A mão do {self.dono.nome} possui {len(self.cartas)} cartas")
  module <module> line 1
    (self.dono.nome)
AttributeError: 'Jogador' object has no attribute 'nome'
'''},
{'date': 'Tue Nov 07 2023 12:22:28.194 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 42
  print("cartas tesouro:" self.cartas_tesouro)
                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 07 2023 12:22:52.295 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 45
  def distribuir_cartas_tesouro(self)
                                      ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 07 2023 12:23:14.884 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 63
    IlhaProibida()
  module <module> line 37
    self.cartas_tesouro += [CartaAlagamento(face=carta) for carta in ba]
  module <module> line 57
    super().__init__(self, face)
TypeError: __init__() takes 2 positional arguments but more were given
'''},
{'date': 'Tue Nov 07 2023 19:12:33.931 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 36
    main()
  module <module> line 31
    Ilha()
  module agua.ilha line 39
    LG.log(0, "Bem vindos à Ilha Proibida - montagem do tabuleiro")
AttributeError: 'module' object has no attribute 'log'
'''},
{'date': 'Tue Nov 07 2023 19:13:58.159 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 22
    from agua.__init__ import LG
ImportError: cannot import name 'LG'

ImportError
Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 268
    action()
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 22
    from agua.__init__ import LG
'''},