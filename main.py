class Domanda:
    def __init__(self, testo, opzioni, risposta_corretta):
        self.testo = testo
        self.opzioni = opzioni
        self.risposta_corretta = risposta_corretta

    def mostra_domanda(self):
        print(self.testo)
        for i, opzione in enumerate(self.opzioni):
            print(f"{i+1}. {opzione}")
        print()

    def controlla_risposta(self, risposta_utente):
        return risposta_utente == self.risposta_corretta


def esegui_questionario(domande):
    punteggio = 0
    for domanda in domande:
        domanda.mostra_domanda()
        risposta_utente = input("Inserisci il numero corrispondente alla tua risposta: ")
        if domanda.controlla_risposta(int(risposta_utente)):
            print("Risposta corretta!\n")
            punteggio += 1
        else:
            print("Risposta errata!\n")
    print(f"Il tuo punteggio finale è: {punteggio}/{len(domande)}")


# Definizione delle domande
domanda1 = Domanda("Qual è la capitale dell'Italia?",
                   ["Roma", "Milano", "Napoli", "Firenze"],
                   1)

domanda2 = Domanda("Quale pianeta è più vicino al Sole?",
                   ["Mercurio", "Venere", "Terra", "Marte"],
                   1)

domanda3 = Domanda("Chi ha dipinto la Mona Lisa?",
                   ["Leonardo da Vinci", "Michelangelo", "Raffaello", "Donatello"],
                   1)

# Lista delle domande
domande = [domanda1, domanda2, domanda3]

# Esecuzione del questionario
esegui_questionario(domande)
