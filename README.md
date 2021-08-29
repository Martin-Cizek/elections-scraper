# elections-scraper

Skript koncentruje vysledky voleb do Poslanecke snemovny ze vsech obci daneho uzemniho celku do tabulky v CSV souboru.
Uzemni celek se skriptu zadava jako parametr pomoci URL stranky s vyberem obci. <a href="https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6103">Ukazka vyberu obci zde</a>.

URL stranky s vyberem obci a jmeno vystupniho souboru se zadavaji jako 2 povinne parametry:

```
python elections-scraper.py "_odkaz na vyber obci_" "_vystupni CSV soubor_"
```
Napriklad:

```
python elections-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6103" "pelhrimov.csv"
```

<i>Pokud vystupni soubor existuje, je bez dotazu prepsan. Pokud vystupni soubor nelze otevrit pro zapis, skript na to upozorni a ukonci se.
V pripade spatne zadane URL nebo problemu s pripojenim na to skript upozorni a predcasne se ukonci bez zapisu do vystupniho souboru.</i>

Knihovny potrebne pro spusteni lze nainstalovat jednoduse pomoci manazeru pip a prilozeneho souboru requirements.txt:

```
pip install -r requirements.txt
```

Ukazka volani skriptu a vystupu do terminalu:

```
(venv) C:\...\scraping>python elections-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6103" "pelhrimov.csv"
Extrahuji odkazy na vysledky hlasovani v obcich z URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6103
Nalezeno 120 odkazu na obce.

Zpracovavam odkaz 120/120: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=10&xobec=549231&xvyber=6103

Ukladam vysledky do souboru: pelhrimov.csv
Ukoncuji elections-scraper
```

Ukazka vystupniho souboru:

```
Kod obce;Nazev obce;Volici v seznamu;Vydane obalky;Platne hlasy;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;Radostné Česko;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;Referendum o Evropské unii;TOP 09;ANO 2011;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů
509388;Arneštovice;68;54;54;3;0;0;14;0;6;2;0;0;0;0;0;3;0;3;14;0;0;0;0;0;0;9;0
561118;Bácovice;63;37;37;0;0;0;5;0;3;2;0;0;1;0;0;1;0;1;18;0;4;0;0;0;0;2;0
561126;Bělá;45;29;27;2;0;0;5;0;1;0;0;0;0;0;0;4;0;0;2;0;6;0;0;0;1;6;0
```

Jako oddelovac poli je ve vystupnim CSV souboru vzhledem k nastaveni Excelu v ceskem prostredi (carka ma vyznam desetinne tecky) pouzit strednik.
Toto lze zmenit editaci promenne CSV_DELIMITER na zacatku skriptu na libovolny jiny znak. 
