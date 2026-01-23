"""
Funções para:
- obter valor atual
- calcular preço justo / preço teto
"""

import yfinance as yf
import pandas as pd


# Função para obtenção do preço atual
def get_current_price(ticker):
    ticker = ticker + '.SA'
    current_price = yf.download(ticker, period='1wk', multi_level_index=False)
    current_price = round(current_price.iloc[-1,0], 2)
    return current_price


# Função que exporta (retorna) o somatório dos dividendos dos últimos 12 meses
def get_dividends_ttm_total(ticker):
    ticker += '.SA'
    dividends_fii = yf.Ticker(ticker)
    dividends_ttm = dividends_fii.dividends.iloc[-12:,].sum()
    return dividends_ttm


# Função para cálculo do valor justo de FII
def calculate_fair_value_fii(ticker, premium, rate):
    ticker += '.SA'
    dividends_fii = yf.Ticker(ticker)
    dividends_ltm = dividends_fii.dividends.iloc[-12:,].sum() # Soma dos últimos doze dividendos mensais (Last Twelve Months)
    except_return = (premium + rate) / 100 # prêmio de risco + taxa do tesouro direto IPCA+
    fair_value = dividends_ltm / except_return
    return fair_value







