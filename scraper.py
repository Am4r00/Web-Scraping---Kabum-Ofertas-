from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from produto import Produto

class ScraperKabum:
    def __init__(self):
         # Aqui criamos o navegador que o Selenium vai controlar
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)

    def pegar_produtos(self):
        # Ele busca os produtos da página e salva na lista
        url = "https://www.kabum.com.br/promocao/HARDWAREKABUM?page_number=1&page_size=100&facet_filters=&sort=&variant=null"
        self.driver.get(url)
        time.sleep(3)

        lista_produtos = []

        while len(lista_produtos) < 50:
            produtos = self.driver.find_elements(By.CLASS_NAME, "productCard")

            for produto in produtos:
                if len(lista_produtos) >= 50:
                    break

                nome = self._extrair(produto, By.CLASS_NAME, "nameCard")
                preco = self._extrair(produto, By.CLASS_NAME, "priceCard")
                parcela = self._extrair(produto, By.CSS_SELECTOR, ".desktop\\:leading-4")

                lista_produtos.append(Produto(nome, preco, parcela))

            if not self._proxima_pagina():
                break

        self.driver.quit()
        return lista_produtos

    def _extrair(self, elemento, by, valor):
        try:
            return elemento.find_element(by, valor).text
        except:
            return "Sem dado"

    def _proxima_pagina(self):
        # Tentando ir pra próxima página
        try:
            botao = self.driver.find_element(By.CSS_SELECTOR, 'button[title="Próxima página"]')
            if "disabled" in botao.get_attribute("class"):
                return False
            botao.click()
            time.sleep(3)
            return True
        except:
            return False
