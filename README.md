# 📊 Análise de Preço Justo -- FIIs

Aplicação em Streamlit para calcular o preço justo de Fundos
Imobiliários (FIIs) com base nos dividendos dos últimos 12 meses e na
rentabilidade desejada.

## 🚀 Funcionalidades

-   Seleção de FII a partir de CSV
-   Cálculo de preço justo
-   Interface simples
-   Estrutura organizada por camadas

## 🧱 Estrutura

analise_precos/ - app.py - data/fii_tickers.csv - services/ - charts/ -
utils/ - assets/ - .streamlit/

## ▶️ Como executar

pip install streamlit pandas altair streamlit run app.py

## 📈 Fórmula

Preço Justo = Dividendos / Rentabilidade
