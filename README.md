# Programmēšana 1, projekts 2025

Projekts tiek īstenots patstāvīgi. Projekta tiek aizstavēts ar prezentāciju un demo.
Kods tiek analizēts pēc aizstavēšanas.

## Analīze, projektēšana, plānošana (0.5pt) (prezentācija)
- Analīze - Problēmas apraksts, kāpēc tā ir aktuāla
- Analīze - Mērķauditorija, kura lietos programmu
- Analīze - eksistējošo risinājumu analīze, ekrānšāviņi, plusi un mīnusi
- Projektēšana - specifikācija, vismaz 5 funkcionālas un 5 nefunkcionālas prasības
- Plānošana - darba uzdevumu saraksts, vismaz 5
- Risinājuma prezentācija - demo vai ekrānšāviņi

## Izstrāde (0.5pt)
- Kods atbilst izvirzītam prasībam
- Ir ievaddatu validācija (pārbaude ka tika ierakstīti korrekti dati)
- Mainīgie rakstīti snake_case, bez saisinājumiem
- Ir komentāri pirms if, for, while kosntrukcijam
- Kods nemet kļūdas darbības laikā
- Izmaiņas saglabātas Github repozitorijā
- Izmaiņas saglabātas vairākas iterācijās (vairāki commit)
- Izmantoti saraksti vai vārdnīcas vai klases
- Izmantota jebkura bibliotēka (modulis uzinstalēts ar PIP un izmantots kodā) 
- Izmantoti JSON faili vai SQLite datubāze datu glabāšanai

## Testēšana (0.5pt)
- Testēšana - 2 veiksmes scenāriji
- 1. Zinot, ka spēlētājs nekustas no sākuma pozīcijas, tad spēlētāja simbols atrodas centrā (6, 6).
- 2. Zinot, ka pēc pietiekama soļu skaita moves_number >= exit_spawn, tad tiek izsaukta funkcija add_exit() un kartes centrā parādās izejas simbols (6, 6).
- Testēšana - 4 lietošanas scenāriji
- 1. Zinot, ka, kad spēlētājs nonāk tajā pašā šūnā, kur atrodas monstrs, tad parādīts zaudējumu ekrāns self.death_screen().
  2. Zinot, ka spēle tiek atsākta pēc sevis uzvaras vai zaudēšanas self.__init__(), tad tiek parādīts self.intro_screen().
  3. Zinot, ka, ievadot taustiņus w; a; s; d, tad spēlētājs pārvietojas noteiktā virzienā, ja nav šķēršļu.
  4. Zinot, ka spēlētājs spēlē, līdz parādās izeja add_exit(), tad tiek parādīts uzvaras ekrāns self.win_screen().
- Testēšana - 2 robež-scenāriji
- 1. Zinot, ka monstors cenšas parādīties tuvāk spēlētājam nekā 8 šūniņas self.add_monster(), tad šī pozīcija tiek ignorēta un tiek izvēlēta pieņemama.
  2. Zinot, ka spēlētājs mēģina iekļūt šūnā ar žoga simbolu FENCE_SYMBOL, tad gājiens netiek veikts un parādās zaudējuma ekrāns self.death_screen().
- Testēšana - 4 automatizēti testi (pytest bilbiotēka)
