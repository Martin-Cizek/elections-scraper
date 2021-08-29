import sys
import csv
import requests
from bs4 import BeautifulSoup

CSV_DELIMITER = ';'
LIST_DELIMITER = ', '


# Vytahne relativni odkazy z uvodni stranky
def extract_urls(main_page_url):
    try:
        page = requests.get(main_page_url)
    except:
        exit("Neplatna adresa serveru, nebo jsou problemy s pripojenim. Ukoncuji elections-scraper.")
    soup = BeautifulSoup(page.content.decode(page.encoding), "html.parser")
    if soup.title.text.lower() == '404 not found':
        exit("Zadana cesta na serveru neexistuje. Ukoncuji elections-scraper.")
    # vsechny hypertextove odkazy na strance
    links_all = soup.find_all('a')
    # vybereme pouze 'ciselne' odkazy smerujici na obce
    links_extracted = [lnk.attrs['href'] for lnk in links_all if lnk.text.isnumeric()]
    return links_extracted


# Vytahne z URL zaklad, ke kteremu budeme pridavat relativni odkazy
def get_base_url(url_string):
    url_fields = url_string.split('/')
    del url_fields[-1]
    base_url = "/".join(url_fields) + "/"
    return base_url


# Vycte zakladni statistiku pro obec z odkazu
def get_stats(sub_page_url):
    stats = dict()
    # vytahnuti kodu obce z URL
    url_params = sub_page_url.split('?')[1].split('&')
    for parm in url_params:
        if 'xobec' in parm:
            stats['Kod obce'] = int(parm.split('=')[1].strip())

    # vycteni souhrnneho infa z uvodni tabulky
    try:
        page = requests.get(sub_page_url)
    except:
        exit("Neplatna adresa serveru, nebo jsou problemy s pripojenim. Ukoncuji elections-scraper.")
    soup = BeautifulSoup(page.content.decode(page.encoding), "html.parser")
    if soup.title.text.lower() == '404 not found':
        exit("Zadana cesta na serveru neexistuje. Ukoncuji elections-scraper.")
    stats['Nazev obce'] = ' '.join(soup.find("h3", string=lambda text: "Obec:" in text).text.strip().split(' ')[1:])
    stats['Volici v seznamu'] = int(soup.find("td", headers="sa2").text.replace(u'\xa0', ''))
    stats['Vydane obalky'] = int(soup.find("td", headers="sa3").text.replace(u'\xa0', ''))
    stats['Platne hlasy'] = int(soup.find("td", headers="sa6").text.replace(u'\xa0', ''))

    # vycteni jmen stran a jejich vysledku z dalsich 2 tabulek
    jmena_stran = [strana_td.text for strana_td in
                   soup.find_all('td', headers='t1sa1 t1sb2', string=lambda text: text != "-")] \
                  + [strana_td.text for strana_td in
                     soup.find_all('td', headers='t2sa1 t2sb2', string=lambda text: text != "-")]

    vysledky_stran = [int(vysledek_td.text.replace(u'\xa0', '')) for vysledek_td in
                      soup.find_all('td', headers='t1sa2 t1sb3', string=lambda text: text != "-")] \
                     + [int(vysledek_td.text.replace(u'\xa0', '')) for vysledek_td in
                        soup.find_all('td', headers='t2sa2 t2sb3', string=lambda text: text != "-")]
    stats.update(dict(zip(jmena_stran, vysledky_stran)))
    return stats


def scrape_elections_data(input_url):
    url_base = get_base_url(input_url)
    print(f"Extrahuji odkazy na vysledky hlasovani v obcich z URL: {input_url}")
    url_list = extract_urls(input_url)
    if len(url_list) < 1:
        exit('Nenalezeny zadne odkazy na obce. Ukoncuji elections-scraper.')
    else:
        print(f"Nalezeno {len(url_list)} odkazu na obce.\n")
    results = list()
    n = len(url_list)
    i = 1
    for url_rel in url_list:
        url = url_base + url_rel
        print(f"\rZpracovavam odkaz {i}/{n}: {url}", end="")
        sts = get_stats(url)
        results.append(sts)
        i += 1
    print('\n')
    return results


def save_csv_file(output_file_name, results_list):
    try:
        with open(output_file_name, mode='w', newline='') as csv_file:
            print(f'Ukladam vysledky do souboru: {output_file_name}')
            field_names = results_list[0].keys()
            writer = csv.DictWriter(csv_file, delimiter=CSV_DELIMITER, fieldnames=field_names)
            writer.writeheader()
            for list_itm in results_list:
                writer.writerow(list_itm)
    except:
        print(f'Vystupni soubor "{output_file_name}" nelze otevrit pro zapis.')
        print('Bud ho vyuziva jina aplikace, nebo je disk chranen proti zapisu.')
        exit('Ukoncuji elections-scraper.')

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 2:
        url_in = args[0]
        file_out = args[1]
        res_list = scrape_elections_data(url_in)
        save_csv_file(file_out, res_list)
    else:
        print('Nedostatecny pocet vstupnich argumentu.')
        print('Pouzivejte volani ve tvaru: python elections-scraper.py "_odkaz_na_vyber_obci_" "_vystupni_soubor_"')
        exit('Ukoncuji elections-scraper.')
    print('Ukoncuji elections-scraper')
    exit(0)
    
