Web Scraping - Kabum Ofertas 🔎💻
Descrição do Projeto
Este projeto tem como objetivo realizar um Web Scraping no site da Kabum, coletando informações de produtos como nome, preço e informações de parcelamento.

A coleta é feita de forma automatizada utilizando o Selenium, armazenando os dados em um arquivo .csv organizado e pronto para análise.

Além disso, o projeto possui um script extra para realizar a limpeza de dados duplicados no arquivo gerado.

Funcionalidades
Acesso automatizado ao site da Kabum

Coleta de dados dos produtos em promoção (nome, preço e parcelas)

Paginação automática

Armazenamento dos dados em um arquivo .csv

Remoção de registros duplicados

Código organizado em classes e seguindo boas práticas de desenvolvimento

Tecnologias Utilizadas
Python 3

Selenium

Pandas

WebDriver Chrome

Programação Orientada a Objetos (POO)

Estrutura do Projeto
bash
Copiar
Editar
codigo_webscraping/
│
├── main.py               # Arquivo principal que executa o scraping
├── produto.py            # Classe Produto (modelo dos dados)
├── scraper.py            # Classe responsável pelo Web Scraping
└── limpar_dados.py       # Script para limpar dados duplicados do CSV
Como Executar o Projeto
Pré-requisitos:
Python instalado

Instalar as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Requisitos:

nginx
Copiar
Editar
selenium
pandas
Passos para execução:
Execute o scraping:

bash
Copiar
Editar
python main.py
O arquivo produtos_kabum.csv será gerado com os dados coletados.

Execute a limpeza de dados:

bash
Copiar
Editar
python limpar_dados.py
Um novo arquivo produtos_kabum_limpo.csv será gerado com os dados tratados.

Resultado Final
Os dados coletados ficam organizados e prontos para serem utilizados em análises, dashboards ou relatórios.

Exemplo do CSV gerado:

Nome do Produto	Preço	Parcelamento
Placa de Vídeo RTX 3060	R$ 2.499,00	10x de R$ 249,90
SSD Kingston 480GB	R$ 199,00	3x de R$ 66,33
Autor
Desenvolvido por:

João Victor Amaro
Estudante de Análise e Desenvolvimento de Sistemas | Apaixonado por tecnologia e desenvolvimento de software.

LinkedIn
GitHub

