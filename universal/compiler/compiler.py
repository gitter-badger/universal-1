from ..util import get_file_tuple
from .language.gcc import Gcc
from .language.gpp import Gpp

class Compiler():

    def __init__(self, filename):
        self.filename = filename
        self.compiler = self.get_compiler()

    def compile(self):
        return self.compiler.compile()

    def run(self):
        return self.compiler.run()

    def get_compiler(self):
        (directory, name, extension) = get_file_tuple(self.filename)
        if extension == Gcc.extension():
            compiler = Gcc(self.filename)
        elif extension == Gpp.extension():
            compiler = Gpp(self.filename)
        return compiler

