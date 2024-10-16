import csv

class Prodotto:
    def _init_(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita

class Magazzino:
    def _init_(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.prodotti.append(prodotto)

    def rimuovi_prodotto(self, nome_prodotto):
        for prodotto in self.prodotti:
            if prodotto.nome == nome_prodotto:
                self.prodotti.remove(prodotto)

    def valore_totale(self):
        valore_totale = 0
        for prodotto in self.prodotti:
            valore_totale += prodotto.prezzo * prodotto.quantita
        return valore_totale

    def salva_file(self, nome_file):
        with open(nome_file, 'w', newline='') as csvfile:
            fieldnames = ['Nome', 'Prezzo', 'Quantità']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for prodotto in self.prodotti:
                writer.writerow({'Nome': prodotto.nome, 'Prezzo': prodotto.prezzo, 'Quantità': prodotto.quantita})

    def visualizza_magazzino(self):
        if not self.prodotti:
            print("Il magazzino è vuoto.")
        else:
            print("Inventario del magazzino:")
            for prodotto in self.prodotti:
                print(f"Prodotto: {prodotto.nome}, Prezzo: {prodotto.prezzo}, Quantità: {prodotto.quantita}")

magazzino = Magazzino()
p1 = Prodotto("Maglietta", 15.99, 20)
p2 = Prodotto("Pantaloni", 29.99, 10)
magazzino.aggiungi_prodotto(p1)
magazzino.aggiungi_prodotto(p2)
magazzino.visualizza_magazzino()
magazzino.salva_file('inventario_magazzino.csv')