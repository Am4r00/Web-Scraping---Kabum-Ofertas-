from scraper import ScraperKabum
from gerenciando_csv import GerenciadorCSV

def main():
    scraper = ScraperKabum()
    produtos = scraper.pegar_produtos()

    gerenciador = GerenciadorCSV()
    gerenciador.salvar_csv(produtos, "produtos_kabum.csv")
    gerenciador.limpar_duplicados("produtos_kabum.csv")

if __name__ == "__main__":
    main()
