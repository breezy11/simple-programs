# TicTacToe

Python Game projekt Tic Tac Toe (Iks Oks)

Što je Tic Tac Toe (Iks Oks)?
Tic Tac Toe (Iks Oks) jedna je od najčešće igranih igara i najbolja igra  za “ubiti” vrijeme kod dosade koju možete igrati bilo gdje samo sa olovkom i papirom. Ako ne znate kako igrati ovu igru, ne brinite, razumjet ćete lagano. Igraju dvije osobe. Prvo nacrtamo ploču s 3 × 3 kvadratnom rešetkom. Prvi igrač odabire "X" i crta ga na bilo kojoj kvadratnoj rešetki, a onda je mogućnost drugog igrača da na dostupnim mjestima nacrta "O". Ovako igrači crtaju slovima 'X' i 'O' na praznim mjestima sve dok jedan igrač ne uspije iscrtati 3 uzastopne oznake bilo vodoravno, okomito ili dijagonalno. Tada igrač dobiva igru, a inače je neodlučeno kada su popunjena sva mjesta.

Tic Tac Toe (Iks Oks) - O Python projektu
Zanimljiv Python projekt gradit će se pomoću biblioteke pygame. Objasnit ćemo sve metode pygame objekta koje se koriste u ovom projektu. Pygame je sjajna biblioteka koja će nam omogućiti stvaranje prozora i crtanje slika i oblika na prozoru. Na ovaj način ćemo zabilježiti koordinate miša i identificirati blok u kojem trebamo označiti "X" ili "O". Tada ćemo provjeriti je li korisnik pobijedio u igri ili ne. Cijeli izvorni kod projekta možete preuzeti s ove veze: https://github.com/breezy11/TicTacToe

Preduvjeti
Da bismo implementirali ovu igru, upotrijebit ćemo osnovne koncepte Python i Pygame koji je Python biblioteka za izradu igara na više platformi. Sadrži module potrebne za računalnu grafiku i zvučne biblioteke. Za instaliranje biblioteke možete upotrijebiti instalacijski program pip iz naredbenog retka: pip install pygame

Koraci za izgradnju Python projekta - Tic Tac Toe (Iks Oks) igra
Prvo, provjerimo korake za izgradnju Tic Tac Toe (Iks Oks) programa na Pythonu:


Stvoriti zaslon za našu igru.
Na platnu nacrtati kvadratnu rešetku na kojoj ćemo igrati Tic Tac Toe (Iks Oks).
Nakon završetka igre nacrtati statusnu traku da bismo pokazali tko pobjeđuje u igri.
Kad netko pobijedi u igri ili je neodlučeno, onda se resetira igra.
Moramo pokrenuti našu igru unutar beskonačne petlje. Trajno će tražiti događaje i kada korisnik pritisne tipku miša na mreži, prvo ćemo dobiti X i Y koordinate miša. Tada ćemo provjeriti na koji je kvadrat korisnik kliknuo. Tada ćemo na platnu nacrtati odgovarajuću sliku "X" ili "O". To je u osnovi ono što ćemo raditi u ovoj ideji  Python projekta.

1. Inicijalizacija komponenti igre
Započnimo uvozom biblioteke pygame. Tada inicijaliziramo sve globalne varijable koje ćemo koristiti u našoj igri Tic Tac Toe (Iks Oks). Ovdje je board glavna ploča od 3 × 3  i isprva će imati 9 null(0) vrijednosti. Visina i širina platna na kojem ćemo igrati igru je 550 × 550.

2. Inicijalizacija Pygame prozora
Koristimo pygame da stvorimo novi prozor u kojem ćemo igrati našu igru Tic Tac Toe (Iks Oks). Tako inicijaliziramo pygame metodom pg.init () i zaslon prozora je postavljen na širinu od 550 i visinu od 550. Pg.display.set_mode () inicijalizira zaslon i referenciramo ga na varijablu zaslona. Ova će se varijabla zaslona koristiti kad god želimo nešto prikazati na zaslonu. Metoda pg.display.set_caption koristi se za postavljanje imena koje će se pojaviti na vrhu prozora zaslona.

3. Učitavanje i pretvaranje slika
Python  machine learning projekt  koristi mnogo slika poput početne slike koja će se prikazati kada se igra pokrene ili resetira. X i O su slike koje ćemo crtati kad korisnik klikne na mrežu. Učitavamo sve slike i mijenjamo im veličinu kako bi se one lako uklopile u naš prozor. 

4. Definiranje funkcija
Sada stvaramo funkciju koja će pokrenuti igru. Ovu ćemo funkciju koristiti i kada želimo ponovo pokrenuti igru. U pygame se funkcija blit () koristi na površini za crtanje slike na drugoj slici.Stoga crtamo početnu sliku i nakon crtanja uvijek moramo ažurirati zaslon pg.display.update (). Zatim na bijeloj pozadini nacrtamo 2 okomite i vodoravne linije kako bismo napravili mrežu 3 × 3. Funkcija win_check () provjerava  Tic Tac Toe (Iks Oks) ploču da vidi sve oznake od znakova „X” i „O”. Izračunava je li igrač pobijedio u igri ili ne. Može pobijediti ako igrač označi 3 uzastopne oznake u redu, koloni ili dijagonalno. Ova se funkcija poziva svaki put kada na ploči crtamo oznaku "X" ili "O".

5. Pokretanje igre neprekidno
Pokrećemo while petlju i neprekidno provjeravamo da li ima događaja koje napravi korisnik. Ako korisnik pritisne tipku miša, događaj MOUSEBUTTONUP snimit će se i tada ako korisnik pobijedi ili igra bude izjednačena, resetiramo igru. Ažuriramo prikaz u svakoj iteraciji.

Sažetak
Ovim projektom u Pythonu uspješno smo napravili igru Tic Tac Toe (Iks Oks). Popularnu biblioteku pygame koristili smo za prikazivanje grafike na prozoru. Naučili smo kako snimiti događaje s tipkovnice ili miša i aktivirati funkciju kad se pritisne tipka miša. Na ovaj način možemo izračunati položaj miša, nacrtati ‘X’ ili ‘O’ na zaslonu i provjeriti je li igrač pobijedio u igri ili ne.
