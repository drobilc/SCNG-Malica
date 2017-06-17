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

Na voljo je 7 funkcij.
* `pridobiPodatkeTaTeden()` - izpiše stanje malice ta teden (od ponedeljka do nedelje)
* `pridobiPodatke(datum)` - izšiše podatke o malici za 7 dni od danega datuma
* `odjava(datum)` - odjavi uporabnika od malice na določen dan
* `prijava(datum)` - prijavi uporabnika na topel obrok na določen dan
* `zamenjava(datum, tip)` - na določen dan uporabniku spremeni tip obroka. Ta je lahko le **SUH** - suhi obrok in **OSN** - topli obrok. Tipa ni potrebno napisati, privzet je **SUH**
* `pridobiPodatkeDanes()` - pridobi podatke o malici na današnji dan
* `pridobiPodatkeNaDan(datum)` - pridobi podatke o malici za določen dan v letu

Za primer glej spodnji program:
```python
import malica

#Ustvarimo nov objekt uporabnika z uporabniskim imenom "9003477" in geslom "geslogeslo"
uporabnik = malica.Malica("9003477", "geslogeslo")

#Izpisemo podatke od ponedeljka do nedelje ta teden
print uporabnik.pridobiPodatkeTaTeden()

#Uporabnika od malice odjavimo za 19. december 2016
datum = datetime.datetime(2016, 12, 19)
uporabnik.odjava(datum)
print uporabnik.pridobiPodatke(datum)

#Uporabnika nazaj prijavimo za 19. december 2016
uporabnik.prijava(datum)
print uporabnik.pridobiPodatke(datum)

#Uporabniku zamenjamo tip obroka na suho malico
uporabnik.zamenjava(datum, "SUH")
print uporabnik.pridobiPodatke(datum)

#Uporabniku zamenjamo tip obroka na topli obrok
uporabnik.zamenjava(datum, "OSN")
print uporabnik.pridobiPodatke(datum)

#Izpišemo današnji tip obroka
print uporabnik.pridobiPodatkeDanes()

#Izpišemo tip obroka 19. decembra 2016
print uporabnik.pridobiPodatkeNaDan(datum)
```
