from bs4 import BeautifulSoup

# Lê o HTML de entrada
with open("entrada.html", "r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

# Seleciona todos os pares de nome/valor
linhas = soup.select(".specificationTable--fichaTecnica-rowNameValue")

# Cria uma nova tabela
nova_tabela = "<table>\n"

for linha in linhas:
    nome = linha.select_one(".specificationTable--fichaTecnica-name").get_text(strip=True)
    valor = linha.select_one(".specificationTable--fichaTecnica-value").get_text(strip=True)
    nova_tabela += f"  <tr>\n    <td>{nome}</td>\n    <td>{valor}</td>\n  </tr>\n"

nova_tabela += "</table>"

# Salva o resultado no arquivo de saída
with open("saida.html", "w", encoding="utf-8") as file:
    file.write(nova_tabela)

print("✔ Arquivo 'saida.html' criado com sucesso.")