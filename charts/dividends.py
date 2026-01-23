import pandas as pd
import altair as alt
import yfinance as yf


# Função para obtenção de série histórica de dividendos e geração de gráfico a partir da mesma
def plot_monthly_dividends(ticker):
    ticker += '.SA'
    dividends_fii = yf.Ticker(ticker)
    dividend_history = dividends_fii.dividends.iloc[-12:,]
    
    serie = pd.Series(data=dividend_history.values, index=pd.to_datetime(dividend_history.index))
    df = serie.reset_index()
    df.columns = ['data', 'valor']
    df['data'] = df['data'].dt.tz_localize(None)
    df.insert(0,'mes_ano', df['data'].dt.strftime('%m/%Y'))

   
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('mes_ano:N', title='Mês/Ano', sort=None),
        y=alt.Y('valor:Q', title='Dividendos Mensais',  axis=alt.Axis(format='$.2f')),
        tooltip=[
            alt.Tooltip('mes_ano:N', title='Mês/Ano'),
            alt.Tooltip('valor:Q', title='R$', format='.2f')
        ]        
    ).properties(
        title={
            'text': 'Evolução dos Dividendos Mensais',
            'anchor': 'middle',
            'fontSize': 18,
            'fontWeight': 'bold'
        },
        padding={
            'top':30,
            'bottom': 20,
            'left': 20,
            'right': 20
        }
    ).configure_view(strokeWidth=0)
    
    return chart