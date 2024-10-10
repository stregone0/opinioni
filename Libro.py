class Libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
    def get_titolo(self):
        return self.titolo

    def get_autore(self):
        return self.autore

    def get_anno(self):
        return self.anno

    def set_titolo(self, nuovo_titolo):
        self.titolo = nuovo_titolo

    def set_autore(self, nuovo_autore):
        self.autore = nuovo_autore

    def set_anno(self, nuovo_anno):
        self.anno = nuovo_anno

    def __set__(self):
        return f"Libro: {self.titolo}, {self.autore}, ({self.anno})"

        libro1 =Libro("L'infinito", "Giacomo Leopardi", "1867")

        print(libro1)  # output: Linro: L'infinito, Giacomo lropardi, 1867

