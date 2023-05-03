import random

class Asiakas:
    """
Asiakas-luokka kuvaa palveluun liittyvää asiakasta.
Attributes:
    nimi (str): Asiakkaan nimi.
    ika (int): Asiakkaan ikä.
    asiakasnro (str): Asiakasnumero.

Methods:
    generoi_asiakasnumero(self): Generoi asiakasnumeron satunnaisista numeroista.
    set_nimi(self, nimi): Asettaa asiakkaan nimen.
    get_asiakasnumero(self): Palauttaa asiakasnumeron.
"""
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.asiakasnro = self.generoi_asiakasnumero()

    def generoi_asiakasnumero(self):
        numerot = [str(random.randint(0, 9)) for _ in range(9)]
        return "-".join(["".join(numerot[:2]), "".join(numerot[2:5]), "".join(numerot[5:])])

    def set_nimi(self, nimi):
        if not nimi:
            raise ValueError("Uusi nimi on annettava.")
        if not self.nimi:
             raise ValueError("Asiakas on annettava.")
        self.nimi = nimi

    def get_asiakasnumero(self):
        return self.asiakasnro



class Palvelu:
    """
Palvelu-luokka kuvaa palvelua, jolla voi olla asiakkaita.
Attributes:
    tuotenimi (str): Palvelun tuotenimi.
    asiakkaat (list): Lista palvelun asiakkaista.

Methods:
    luo_asiakasrivi(self, asiakas): Luo asiakkaan tiedot rivimuodossa.
    lisaa_asiakas(self, asiakas): Lisää asiakkaan palveluun.
    poista_asiakas(self, asiakas): Poistaa asiakkaan palvelusta.
    tulosta_asiakkaat(self): Tulostaa palvelun asiakkaat.
"""
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.asiakkaat = []

    def luo_asiakasrivi(self, asiakas):
        return f"{asiakas.nimi} ({asiakas.get_asiakasnumero()}) on {asiakas.ika}-vuotias."

    def lisaa_asiakas(self, asiakas):
        if asiakas in self.asiakkaat:
            return "Asiakas on jo lisätty palveluun."
        else:
            self.asiakkaat.append(asiakas)
            return "Asiakas lisätty palveluun."

    def poista_asiakas(self, asiakas):
        if asiakas in self.asiakkaat:
            self.asiakkaat.remove(asiakas)
            return "Asiakas poistettu palvelusta."
        else:
            return "Asiakasta ei löydy palvelusta."

    def tulosta_asiakkaat(self):
        if self.asiakkaat:
            print(f"Tuotteen {self.tuotenimi} asiakkaat ovat:")
            for asiakas in self.asiakkaat:
                rivi = self.luo_asiakasrivi(asiakas)
                print(rivi)
        else:
            print(f"Tuotteella {self.tuotenimi} ei ole asiakkaita.")


class ParempiPalvelu(Palvelu):
    """
ParempiPalvelu-luokka laajentaa Palvelu-luokkaa tarjoamalla lisäominaisuuksia ja etuja.
Attributes:
    tuotenimi (str): Palvelun tuotenimi.
    asiakkaat (list): Lista palvelun asiakkaista.
    edut (list): Lista palvelun tarjoamista eduista.

Methods:
    lisaa_etu(self, etu): Lisää uuden edun palveluun.
    poista_etu(self, etu): Poistaa edun palvelusta.
    tulosta_edut(self): Tulostaa palvelun edut.
"""
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.edut = []

    def lisaa_etu(self, etu):
        if etu in self.edut:
            return "Etu on jo lisätty palveluun."
        else:
            self.edut.append(etu)
            return "Etu lisätty palveluun."

    def poista_etu(self, etu):
        if etu in self.edut:
            self.edut.remove(etu)
            return "Etu on poistettu palvelusta."
        else:
            return "Etua ei löydy palvelusta."

    def tulosta_edut(self):
        if self.edut:
            print(f"Palvelun {self.tuotenimi} edut ovat:")
            for etu in self.edut:
                print(etu)
        else:
            print(f"Palvelulla {self.tuotenimi} ei ole erityisiä etuja.")
