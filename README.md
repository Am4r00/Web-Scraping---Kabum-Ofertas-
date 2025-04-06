# Web Scraping Kabum - Python 🖥️🔍

## Descrição do Projeto
Este projeto tem como objetivo realizar um Web Scraping no site da Kabum, capturando informações de produtos disponíveis em promoção. O foco principal é coletar dados como:

- Nome do Produto
- Preço
- Condições de Parcelamento  

O projeto foi desenvolvido em Python, utilizando a biblioteca Selenium para automação da navegação e coleta dos dados.

Além disso, o projeto possui um script adicional para realizar a limpeza dos dados coletados, removendo produtos duplicados e gerando um novo arquivo `.csv` final.

---

## Tecnologias Utilizadas
- Python 3.x  
- Selenium  
- Pandas  
- WebDriver (Google Chrome)

---

## Como Executar o Projeto

### 1. Clonar o repositório:
```bash
git clone https://github.com/Am4r00/[https://github.com/Am4r00/Web-Scraping---Kabum-Ofertas-.git]
```
2. Instalar as dependências:
```bash
pip install -r requirements.txt
```
3. Executar o Web Scraping:
```bash
python main.py
```
4. Limpar os dados duplicados:
```bash
python limpeza.py
```
Estrutura do Projeto
```bash
├── main.py           # Script principal que executa o Web Scraping
├── scraper.py        # Classe responsável por realizar o scraping
├── produto.py        # Classe que representa um produto
├── limpeza.py        # Script para limpar dados duplicados
├── produtos_kabum.csv     # Arquivo gerado com os produtos coletados
├── produtosLimpo_kabum.csv # Arquivo final limpo
└── requirements.txt  # Dependências do projeto
```
Resultado Final
Ao final da execução, os dados coletados dos produtos serão armazenados em um arquivo .csv chamado:
produtos_kabum.csv

E após a limpeza de duplicados:
produtosLimpo_kabum.csv

Observações
Este projeto foi desenvolvido com finalidade educacional, A prática de Web Scraping deve respeitar as políticas do site acessado.
Caso o site sofra alterações em seu layout ou estrutura, o código pode necessitar de ajustes.

Autor
Desenvolvido por João Amaro 🚀
