import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards
from utils.formatters import load_css, format_currency
from services.data_loader import load_fii_tickers
from services.pricing import calculate_fair_value_fii, get_current_price, get_dividends_ttm_total
from charts.dividends import plot_monthly_dividends


# ---------- CONFIG ----------
st.set_page_config(
    page_title='Análise de Preços',
    page_icon=':material/add_chart:', 
    layout='wide'
)


# ----------- CSS -----------
load_css()



# ---------- DATA ----------
try:
    tickers = load_fii_tickers()
except Exception as e:
    st.error(str(e))
    st.stop()
    

# ------------ UI -----------
st.header('Análise de preços de Fundos Imobiliários (FIIs) segundo o Modelo de Gordon (GGM)')

st.divider()


with st.container(border=True):
    with st.container(border=True):
        colA, colB, colC = st.columns(3)

        with colA:
            selected_ticker = st.selectbox('Selecione o FII', tickers)

        with colB:
            premium = st.number_input(
                'Informe o valor do prêmio', min_value=2.0, max_value=3.0, step=0.5, value=2.5)

        with colC:
            rate = st.number_input(
                'Infome o percentual (%) do título IPCA+', min_value=0.0, max_value=20.0, value=7.73)

    st.markdown(f'<h1>{selected_ticker}</h1>', unsafe_allow_html=True)

    price = get_current_price(selected_ticker)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Total Pago dos 12 Últimos Dividendos',
                  value=format_currency(get_dividends_ttm_total(selected_ticker)))

    with col2:
        st.metric('Preço Atual', format_currency(price))

    with col3:
        fair_value = calculate_fair_value_fii(selected_ticker, premium, rate)
        st.metric('Preço Justo', format_currency(fair_value))


with st.container(border=True):
    st.altair_chart(plot_monthly_dividends(selected_ticker),
                    use_container_width=True, height=500)

style_metric_cards(border_left_color='blue', border_size_px=0)
