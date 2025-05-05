# app.py
import streamlit as st
from bs4 import BeautifulSoup

st.set_page_config(page_title="Limpador de Tabela HTML", layout="wide")

st.title("🧹 Limpador de Tabela HTML")

html_input = st.text_area("Cole aqui o HTML da tabela com especificações", height=300)

if st.button("Limpar HTML"):
    if html_input.strip() == "":
        st.warning("Por favor, cole algum conteúdo HTML antes de processar.")
    else:
        soup = BeautifulSoup(html_input, "html.parser")
        linhas = soup.select(".specificationTable--fichaTecnica-rowNameValue")

        if not linhas:
            st.error("Nenhuma linha de especificação encontrada com as classes esperadas.")
        else:
            nova_tabela = "<table>\n"
            for linha in linhas:
                nome = linha.select_one(".specificationTable--fichaTecnica-name").get_text(strip=True)
                valor = linha.select_one(".specificationTable--fichaTecnica-value").get_text(strip=True)
                nova_tabela += f"  <tr>\n    <td>{nome}</td>\n    <td>{valor}</td>\n  </tr>\n"
            nova_tabela += "</table>"

            st.success("Tabela limpa gerada com sucesso:")
            st.code(nova_tabela, language="html")
