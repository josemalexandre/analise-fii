# Leitura do CSV com Pandas
# Retorno de lista de tickers

import pandas as pd
from utils.paths import DATA_DIR


def load_fii_tickers():
    csv_path = DATA_DIR / 'fii_tickers.csv'
    if not csv_path.exists():
        raise FileNotFoundError('Arquivo de tickers não encontrado.')

    df = pd.read_csv(csv_path, sep=';', decimal=',')

    if 'TICKER' not in df.columns:
        raise ValueError("Coluna 'TICKER' não encontrada no CSV.")

    return df['TICKER'].dropna().unique().tolist()