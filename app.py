# app.py
import streamlit as st
from bs4 import BeautifulSoup

st.set_page_config(page_title="Limpador de Tabela HTML", layout="wide")

st.title("🧹 Limpador de Tabela HTML")

# 📝 Campo de entrada com título customizado
html_input = st.text_area("Adicione aqui o seu HTML antigo:", height=300)

# 🔘 Botões lado a lado
col1, col2 = st.columns([1, 1])

# Inicializa a variável do HTML limpo
nova_tabela = ""

with col1:
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

                st.success("HTML limpo gerado com sucesso!")

# Botão de copiar só aparece se houver HTML limpo
with col2:
    if nova_tabela:
        st.button("Copiar novo HTML", on_click=lambda: st.session_state.update({"copiar": True}))

# 📤 Exibe a nova caixa de texto com o resultado
if nova_tabela:
    st.markdown("### Aqui está o seu novo HTML:")
    st.text_area("Resultado", nova_tabela, height=300)

    # Copiar automaticamente para a área de transferência (hack via JS)
    if st.session_state.get("copiar"):
        st.session_state.copiar = False
        st.markdown(f"""
            <script>
            navigator.clipboard.writeText({repr(nova_tabela)});
            </script>
        """, unsafe_allow_html=True)
        