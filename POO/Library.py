class Livre:
    def __init__(self, ISBN: int, titre: str, auteur: str, annee: int):
        self.ISBN = ISBN
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = bool(True)

    def __str__(self):
        dispo = str()
        if self.disponible:
            dispo = "oui"
        else:
            dispo = "non"
        return f"{self.titre} de {self.auteur} publié en {self.annee} porte \
l'identifiant {self.ISBN} et est bien disponible : {dispo}"


class Membre:
    def __init__(self, ID: int, nom: str):
        self.member_id = ID
        self.nom = nom
        self.emprunts = set()

    def __str__(self):
        return f"Le membre {self.nom} a pour identifiant {self.member_id} \
et a emprunté le.s livre.s suivant.s : {self.emprunts}"


class Bibliotheque(Livre, Membre):
    def __init__(self):
        self._livres = dict()
        self._membres = dict()

    def add_book(self, book: Livre):
        self._livres[book.ISBN] = book
        return

    def remove_book(self, book: Livre):
        del self._livres[book.ISBN]
        return

    def add_member(self, member: Membre):
        self._membres[member.member_id] = member
        return

    def remove_member(self, member: Membre):
        del self._membres[member.member_id]
        return

    def emprunter(self, member: Membre, book: Livre):
        self._membres[member.member_id].emprunts.add(book.ISBN)
        self._livres[book.ISBN].disponible = False
        return

    def retourner(self, member: Membre, book: Livre):
        self._membres[member.member_id].emprunts.discard(book.ISBN)
        self._livres[book.ISBN].disponible = True
        return

    def print_emprunts(self, member: Membre):
        print(f"Les livres empruntés par \
le membre {member.nom} sont les suivants :")
        for emprunt in member.emprunts:
            print(self._livres[emprunt])
        print("")
        return

    def print_members(self):
        print('Les membres de la Bibliothèque sont :')
        for i in self._membres:
            print(self._membres[i])
        print("")
        return

    def print_available(self):
        print("Les livres disponibles sont les suivants :")
        for i in self._livres:
            book = self._livres[i]
            if book.disponible:
                print(book)
        print("")
        return

    def find_by_author(self, author: str):
        print(f"Le.s livre.s écrit.s par {author} sont :")
        for i in self._livres:
            book = self._livres[i]
            if book.auteur is author:
                print(book.titre)
        print("")
        return

    def find_by_title(self, title: str):
        print(f"Le.s livre.s portant le titre {title} sont :")
        for i in self._livres:
            book = self._livres[i]
            if book.titre == title:
                print(book)
        print("")
        return


# Création des membres de la Bibliothèque
feli = Membre(1, "Felicity")
nouchka = Membre(2, "Nouchka")
aka = Membre(3, "O'Aka")
lovely = Membre(4, "Lovely One")

print(lovely)

# Création de livres pour la Bibliothèque
HP1 = Livre(1, "Harry Potter à l'Ecole des Sorciers", "J K Rowling", 1997)
HP2 = Livre(2, "Harry Potter et la Chambre des secrets", "J K Rowling", 1998)
HP3 = Livre(3, "Harry Potter et le Prisonnier d'Azkaban", "J K Rowling", 1999)
LOTR1 = Livre(4, "La Communauté de l'Anneau", "JRR Tolkien", 1954)
LOTR2 = Livre(5, "Les Deux Tours", "JRR Tolkien", 1954)
LOTR3 = Livre(6, "Le Retour du roi", "JRR Tolkien", 1955)
Tao = Livre(7, "The Tao of Equus", "Linda Kohanov", 2001)

print(HP1)

# Création de la Bibliothèque
BNF = Bibliotheque()

# Ajout/Retrait de livres dans la Bibliothèque
BNF.add_book(HP1)
BNF.add_book(HP2)
BNF.add_book(HP3)
BNF.add_book(LOTR1)
BNF.add_book(LOTR2)
BNF.add_book(LOTR3)
BNF.add_book(Tao)

BNF.print_available()

BNF.remove_book(LOTR2)

BNF.print_available()

# Ajout/Retrait de membres dans la Bibliothèque
BNF.add_member(feli)
BNF.add_member(nouchka)
BNF.add_member(aka)
BNF.add_member(lovely)

BNF.print_members()

BNF.remove_member(feli)

BNF.print_members()

# Recherche sur les livres
BNF.find_by_author("JRR Tolkien")

BNF.find_by_title("The Tao of Equus")

BNF.print_available()

# Emprunt/Retour de livres
BNF.emprunter(lovely, Tao)
BNF.emprunter(lovely, LOTR1)

BNF.print_emprunts(lovely)
BNF.print_available()

BNF.retourner(lovely, Tao)

BNF.print_emprunts(lovely)
BNF.print_available()
