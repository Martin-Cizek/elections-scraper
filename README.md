# elections-scraper

<b>Program na scrapovani volevnich dat z uzemnich celku</b>
<p>Skript prochazi vsechny odkazy na vysledky voleb do Poslanecke snemovny CR v jednotlivych obcich v nadrazenem uzemnim celku (okresu).
Data koncentruje ve formatu CSV do zadaneho textoveho souboru. Jako oddelovac poli je vzhledem k nastaveni Excelu v ceskem prostredi pouzit strednik.
Toto lze zmenit editaci promenne CSV_DELIMITER na zacatku skriptu.</p>
<p><i>Skript se pouziva se 2 vstupnimi parametry:</i>
<b>python elections-scraper.py "URL_s_vyberem_obci" "vystupni_csv_soubor"</b></p>
<p><i>Napriklad:</i><br>
<b>python elections-scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6103" "pelhrimov.csv"</b></p>
<p>Pokud je zadana spatna adresa nebo neni mozno zapisovat do vystupniho souboru, program na to upozorni. Pokud jiz existuje vystupni soubor se zadanym jmenem, je bez dotazu prepsan.</p>

