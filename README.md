# SCNG-Malica
Python skripta, ki omogoča odjavo in prijavo preko spletne aplikacije [Spletna evidenca obrokov](http://malica.scng.si/).

## Inštalacija
Za uporabo skripta je potrebno imeti knjižnico BeautifulSoup. Če uporabljamo *pip*, je inštalacija preprosta. Izvedemo naslednje korake:
```
git clone https://github.com/drobilc/SCNG-Malica.git
cd SCNG-Malica
pip install -r requirements.txt
```

## Uporaba
Po inštalacij potrebnih knjižnic je uporaba skripta preprosta. Najprej ga je potrebno vključiti v programsko kodo.
```python
import malica
```

Na voljo je 5 funkcij.
* `pridobiPodatkeTaTeden()` - izpiše stanje malice ta teden (od ponedeljka do nedelje)
* `pridobiPodatke(datum)` - izšiše podatke o malici za 7 dni od danega datuma
* `odjava(datum)` - odjavi uporabnika od malice na določen dan
* `prijava(datum)` - prijavi uporabnika na topel obrok na določen dan
* `zamenjava(datum, tip)` - na določen dan uporabniku spremeni tip obroka. Ta je lahko le **SUH** - suhi obrok in **OSN** - topli obrok. Tipa ni potrebno napisati, privzet je **SUH**.

Za primer glej spodnji program:
```python
import malica

#Ustvarimo nov objekt uporabnika z uporabniskim imenom "9003477" in geslom "geslogeslo"
uporabnik = malica.Malica("9003477", "geslogeslo")

#Ko je uporabnik prijavljen izpisemo njegovo ime in priimek
print uporabnik.imePriimek

#Izpisemo podatke od ponedeljka do nedelje ta teden
print uporabnik.pridobiPodatkeTaTeden()

#Uporabnika od malice odjavimo za 19. december 2016
uporabnik.odjava("19.12.2016")
print uporabnik.pridobiPodatke("19.12.2016")

#Uporabnika nazaj prijavimo za 19. december 2016
uporabnik.prijava("19.12.2016")
print uporabnik.pridobiPodatke("19.12.2016")

#Uporabniku zamenjamo tip obroka na suho malico
uporabnik.zamenjava("19.12.2016", "SUH")
print uporabnik.pridobiPodatke("19.12.2016")

#Uporabniku zamenjamo tip obroka na topli obrok
uporabnik.zamenjava("19.12.2016", "OSN")
print uporabnik.pridobiPodatke("19.12.2016")
```
