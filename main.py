import os
import pandas as pd

def tratar_valor(df: pd.DataFrame, coluna: str = "valor") -> pd.DataFrame:
    """
    Normaliza a coluna 'valor':
    - Remove pontos e vírgulas de milhar
    - Converte vírgula decimal em ponto
    - Converte para float
    """
    df[coluna] = (
        df[coluna]
        .astype(str)                      # garante string
        .str.replace(r"\.", "", regex=True)  # remove separador de milhar
        .str.replace(",", ".", regex=True)   # troca vírgula decimal por ponto
        .astype(float)                    # converte para número
    )
    return df

def processar_csvs():
    diretorio = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

    arquivos = ["fluxo_caixa.csv", "consulta_titulos.csv"]  # ajuste os nomes dos dois arquivos

    for nome in arquivos:
        caminho = os.path.join(diretorio, nome)

        # lê CSV
        df = pd.read_csv(caminho)

        # trata coluna 'valor'
        df_tratado = tratar_valor(df, coluna="valor")

        # salva novo CSV tratado
        novo_nome = nome.replace(".csv", "_tratado.csv")
        novo_caminho = os.path.join(diretorio, novo_nome)
        df_tratado.to_csv(novo_caminho, index=False)

        print(f"Arquivo tratado salvo em: {novo_caminho}")

if __name__ == "__main__":
    processar_csvs()
