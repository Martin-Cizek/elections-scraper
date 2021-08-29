# elections-scraper

Skript koncentruje vysledky voleb ze vsech obci daneho uzemniho celku do tabulky v CSV souboru.
Uzemni celek se skriptu zadava jako parametr pomoci URL stranky s vyberem obci. Napriklad jako <a href="https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6103">zde</a>.

URL stranky s vyberem obci a jmeno vystupniho souboru se zadavaji jako 2 povinne parametry:

```
python elections-scraper.py "_odkaz na vyber obci_" "_vystupni CSV soubor_"
```
Napriklad:

```
python elections-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6103" "pelhrimov.csv"
```

Jako oddelovac poli je ve vystupnim CSV souboru vzhledem k nastaveni Excelu v ceskem prostredi (carka ma vyznam desetinne tecky) pouzit strednik.
Toto lze zmenit editaci promenne CSV_DELIMITER na zacatku skriptu na libovolny jiny znak.

