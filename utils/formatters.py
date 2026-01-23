import streamlit as st
from utils.paths import ASSETS_DIR


def load_css():
    css_file = ASSETS_DIR / 'styles.css'
    if css_file.exists():
        with open(css_file) as css:
            st.html(f'<style>{css.read()}</style>')


def format_currency(value: float) -> str:
    return f'R$ {value:,.2f}'.replace(',', 'x').replace('.', ',').replace('x', '.')


def format_percentage(value: float) -> str:
    return f'{value:.2%}'.replace('.', ',')
