import os
import django
import json
import random

nr = 50

list_names = ['Ababei',  'Acasandrei',  'Adascalitei',  'Afanasie',  'Agafitei',  'Agape',  'Aioanei',  'Alexandrescu',  'Alexandru',  'Alexe',  'Alexii',  'Amarghioalei',  'Ambroci',  'Andonesei',  'Andrei',  'Andrian',  'Andrici',  'Andronic',  'Andros',  'Anghelina',  'Anita',  'Antochi',  'Antonie',  'Apetrei',  'Apostol',  'Arhip',  'Arhire',  'Arteni',  'Arvinte',  'Asaftei',  'Asofiei',  'Aungurenci',  'Avadanei',  'Avram',  'Babei',  'Baciu',  'Baetu',  'Balan',  'Balica',  'Banu',  'Barbieru',  'Barzu', 'Bazgan', 'Bejan', 'Bejenaru', 'Belcescu', 'Belciuganu', 'Benchea', 'Bilan', 'Birsanu', 'Bivol', 'Bizu', 'Boca', 'Bodnar', 'Boistean', 'Borcan', 'Bordeianu', 'Botezatu', 'Bradea', 'Braescu', 'Budaca', 'Bulai', 'Bulbuc-aioanei', 'Burlacu', 'Burloiu', 'Bursuc', 'Butacu', 'Bute', 'Buza', 'Calancea', 'Calinescu', 'Capusneanu', 'Caraiman', 'Carbune', 'Carp', 'Catana', 'Catiru', 'Catonoiu', 'Cazacu', 'Cazamir', 'Cebere', 'Cehan', 'Cernescu', 'Chelaru', 'Chelmu', 'Chelmus', 'Chibici', 'Chicos', 'Chilaboc', 'Chile', 'Chiriac', 'Chirila', 'Chistol', 'Chitic', 'Chmilevski', 'Cimpoesu', 'Ciobanu', 'Ciobotaru', 'Ciocoiu', 'Ciofu', 'Ciornei', 'Citea', 'Ciucanu', 'Clatinici', 'Clim', 'Cobuz', 'Coca', 'Cojocariu', 'Cojocaru', 'Condurache', 'Corciu', 'Corduneanu', 'Corfu', 'Corneanu', 'Corodescu', 'Coseru', 'Cosnita', 'Costan', 'Covatariu', 'Cozma', 'Cozmiuc', 'Craciunas', 'Crainiceanu', 'Creanga', 'Cretu', 'Cristea', 'Crucerescu', 'Cumpata', 'Curca', 'Cusmuliuc', 'Damian', 'Damoc', 'Daneliuc', 'Daniel', 'Danila', 'Darie', 'Dascalescu', 'Dascalu', 'Diaconu', 'Dima', 'Dimache', 'Dinu', 'Dobos', 'Dochitei', 'Dochitoiu', 'Dodan', 'Dogaru', 'Domnaru', 'Dorneanu', 'Dragan', 'Dragoman', 'Dragomir', 'Dragomirescu', 'Duceac', 'Dudau', 'Durnea', 'Edu', 'Eduard', 'Eusebiu', 'Fedeles', 'Ferestraoaru', 'Filibiu', 'Filimon', 'Filip', 'Florescu', 'Folvaiter', 'Frumosu', 'Frunza', 'Galatanu', 'Gavrilita', 'Gavriliuc', 'Gavrilovici', 'Gherase', 'Gherca', 'Ghergu', 'Gherman', 'Ghibirdic', 'Giosanu', 'Gitlan', 'Giurgila', 'Glodeanu', 'Goldan', 'Gorgan', 'Grama', 'Grigore', 'Grigoriu', 'Grosu', 'Grozavu', 'Gurau', 'Haba', 'Harabula', 'Hardon', 'Harpa', 'Herdes', 'Herscovici', 'Hociung', 'Hodoreanu', 'Hostiuc', 'Huma', 'Hutanu', 'Huzum', 'Iacob', 'Iacobuta', 'Iancu', 'Ichim', 'Iftimesei', 'Ilie', 'Insuratelu', 'Ionesei', 'Ionesi', 'Ionita', 'Iordache', 'Iordache-tiroiu', 'Iordan', 'Iosub', 'Iovu', 'Irimia', 'Ivascu', 'Jecu', 'Jitariuc', 'Jitca', 'Joldescu', 'Juravle', 'Larion', 'Lates', 'Latu', 'Lazar', 'Leleu', 'Leon', 'Leonte', 'Leuciuc', 'Leustean', 'Luca', 'Lucaci', 'Lucasi', 'Luncasu', 'Lungeanu', 'Lungu', 'Lupascu', 'Lupu', 'Macariu', 'Macoveschi', 'Maftei', 'Maganu', 'Mangalagiu', 'Manolache', 'Manole', 'Marcu', 'Marinov', 'Martinas', 'Marton', 'Mataca', 'Matcovici', 'Matei', 'Maties', 'Matrana', 'Maxim', 'Mazareanu', 'Mazilu', 'Mazur', 'Melniciuc-puica', 'Micu', 'Mihaela', 'Mihai', 'Mihaila', 'Mihailescu', 'Mihalachi', 'Mihalcea', 'Mihociu', 'Milut', 'Minea', 'Minghel', 'Minuti', 'Miron', 'Mitan', 'Moisa', 'Moniry-abyaneh', 'Morarescu', 'Morosanu', 'Moscu', 'Motrescu', 'Motroi', 'Munteanu', 'Murarasu', 'Musca', 'Mutescu', 'Nastaca', 'Nechita', 'Neghina', 'Negrus', 'Negruser', 'Negrutu', 'Nemtoc', 'Netedu', 'Nica', 'Nicu', 'Oana', 'Olanuta', 'Olarasu', 'Olariu', 'Olaru', 'Onu', 'Opariuc', 'Oprea', 'Ostafe', 'Otrocol', 'Palihovici', 'Pantiru', 'Pantiruc', 'Paparuz', 'Pascaru', 'Patachi', 'Patras', 'Patriche', 'Perciun', 'Perju', 'Petcu', 'Pila', 'Pintilie', 'Piriu', 'Platon', 'Plugariu', 'Podaru', 'Poenariu', 'Pojar', 'Popa', 'Popescu', 'Popovici', 'Poputoaia', 'Postolache', 'Predoaia', 'Prisecaru', 'Procop', 'Prodan', 'Puiu', 'Purice', 'Rachieru', 'Razvan', 'Reut', 'Riscanu', 'Riza', 'Robu', 'Roman', 'Romanescu', 'Romaniuc', 'Rosca', 'Rusu', 'Samson', 'Sandu', 'Sandulache', 'Sava', 'Savescu', 'Schifirnet', 'Scortanu', 'Scurtu', 'Sfarghiu', 'Silitra', 'Simiganoschi', 'Simion', 'Simionescu', 'Simionesei', 'Simon', 'Sitaru', 'Sleghel', 'Sofian', 'Soficu', 'Sparhat', 'Spiridon', 'Stan', 'Stavarache', 'Stefan', 'Stefanita', 'Stingaciu', 'Stiufliuc', 'Stoian', 'Stoica', 'Stoleru', 'Stolniceanu', 'Stolnicu', 'Strainu', 'Strimtu', 'Suhani', 'Tabusca', 'Talif', 'Tanasa', 'Teclici', 'Teodorescu', 'Tesu', 'Tifrea', 'Timofte', 'Tincu', 'Tirpescu', 'Toader', 'Tofan', 'Toma', 'Toncu', 'Trifan', 'Tudosa', 'Tudose', 'Tuduri', 'Tuiu', 'Turcu', 'Ulinici', 'Unghianu', 'Ungureanu', 'Ursache', 'Ursachi', 'Urse', 'Ursu', 'Varlan', 'Varteniuc', 'Varvaroi', 'Vasilache', 'Vasiliu', 'Ventaniuc', 'Vicol', 'Vidru', 'Vinatoru', 'Vlad', 'Voaides', 'Vrabie', 'Vulpescu', 'Zamosteanu', 'Zazuleac']
list_surnames = ['Adrian', 'Alex', 'Alexandru', 'Alin', 'Andreas', 'Andrei', 'Aurelian', 'Beniamin', 'Bogdan', 'Camil', 'Catalin', 'Cezar', 'Ciprian', 'Claudiu', 'Codrin', 'Constantin', 'Corneliu', 'Cosmin', 'Costel', 'Cristian', 'Damian', 'Dan', 'Daniel', 'Danut', 'Darius', 'Denise', 'Dimitrie', 'Dorian', 'Dorin', 'Dragos', 'Dumitru', 'Eduard', 'Elvis', 'Emil', 'Ervin', 'Eugen', 'Eusebiu', 'Fabian', 'Filip', 'Florian', 'Florin', 'Gabriel', 'George', 'Gheorghe', 'Giani', 'Giulio', 'Iaroslav', 'Ilie', 'Ioan', 'Ion', 'Ionel', 'Ionut', 'Iosif', 'Irinel', 'Iulian', 'Iustin', 'Laurentiu', 'Liviu', 'Lucian', 'Marian', 'Marius', 'Matei', 'Mihai', 'Mihail', 'Nicolae', 'Nicu', 'Nicusor', 'Octavian', 'Ovidiu', 'Paul', 'Petru', 'Petrut', 'Radu', 'Rares', 'Razvan', 'Richard', 'Robert', 'Roland', 'Rolland', 'Romanescu', 'Sabin', 'Samuel', 'Sebastian', 'Sergiu', 'Silviu', 'Stefan', 'Teodor', 'Teofil', 'Theodor', 'Tudor', 'Vadim', 'Valentin', 'Valeriu', 'Vasile', 'Victor', 'Vlad', 'Vladimir', 'Vladut']

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fii_student.settings")
django.setup()
from personalise.models import Board, Personalise

GRUPE = ['-', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
         'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7',
         'X1', 'X2', 'X3', 'alta grupa']


def add_boards_and_get_ids(file_name):
    # load info from json
    b_list = []
    with open(file_name, 'r', encoding='utf8') as ff:
        boards = json.load(ff)
        for board in boards:
            b = Board(
                      year=board['year'],
                      subject=board['subject'],
                      teacher=board['teacher'],
                      description=board['description']
            )
            b.save()
            b_list.append(b)
    return b_list


def insert_values():

    # clear db
    Board.objects.all().delete()

    b_list = add_boards_and_get_ids('boards.json')
    return
    years = [1, 2, 3]
    #  populate db
    for _ in range(nr):
        if _ > len(list_names) - 1 or _ > len(list_surnames) - 1:
            break
        s = Student(name=list_names[_], surname=list_surnames[_], year=random.randrange(1, 4), semian=GRUPE[random.randrange(0, len(GRUPE)-1)])
        s.save()
        p = Personalise(user=s)
        p.save()
        board1 = b_list[random.randrange(0, len(b_list))]
        board2 = b_list[random.randrange(0, len(b_list))]
        p.boards.add(board1)
        # p.remove_board(board1)  # test remove
        p.boards.add(board2)
        p.save()
        p.init_orar()
        p.save()
        pass


def main():
    insert_values()


if __name__ == '__main__':
    main()
