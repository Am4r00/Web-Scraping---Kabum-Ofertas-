import pandas as pd

class GerenciadorCSV:
    def salvar_csv(self, lista_produtos, nome_arquivo):
        data = {
            "produto": [p.nome for p in lista_produtos],
            "preço": [p.preco for p in lista_produtos],
            "Parcela": [p.parcela for p in lista_produtos]
        }
        DataFrame = pd.DataFrame(data)
        DataFrame.to_csv(nome_arquivo, index=False, encoding="utf-8")
        
        print(f"Arquivo {nome_arquivo} Criado com sucesso! ")
    
    def limpar_duplicados(self, nome_arquivo):
        DataFrame = pd.read_csv(nome_arquivo)
        DataFrame_limpo = DataFrame.drop_duplicates()
        DataFrame_limpo.to_csv(f"Limpo_{nome_arquivo}", index=False, encoding="utf-8")
        print(f"Arquivo limpo salvo como limpo_{nome_arquivo}")