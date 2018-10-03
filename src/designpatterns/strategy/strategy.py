#strategy.py

import abc

class FontStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def use_font(self):
        pass

class FontContext:
    def __init__(self, strategy):
        self._strategy = strategy
    def context_interface(self):
        return self._strategy.use_font()

class MonoFontStrategy(FontStrategy):
    def use_font(self):
        return 'using mono font'

class SansFontStrategy(FontStrategy):
    def use_font(self):
        return 'using sans font'
