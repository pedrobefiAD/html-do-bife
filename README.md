# 🧹 Limpador de Tabela HTML com BeautifulSoup

Este script Python lê um arquivo HTML contendo especificações técnicas em uma tabela com classes CSS específicas, extrai os pares nome/valor e gera uma nova tabela HTML limpa com esses dados.

## 📂 Estrutura esperada do HTML de entrada

O script espera encontrar elementos com a estrutura semelhante a:

```html
<div class="specificationTable--fichaTecnica-rowNameValue">
  <div class="specificationTable--fichaTecnica-name">Altura</div>
  <div class="specificationTable--fichaTecnica-value">1,70 m</div>
</div>
```


## 🚀 Como usar

1. Instale os requisitos
Este script usa a biblioteca beautifulsoup4. Instale com:

```
pip install beautifulsoup4
```

2. Coloque seu HTML de entrada
Salve o conteúdo HTML original em um arquivo chamado entrada.html no mesmo diretório do script.

3. Execute o script
No terminal ou prompt de comando:

```
python limpar_html.py
```

4. Resultado
O arquivo saida.html será gerado com a nova tabela limpa.

## 🧾 Saída esperada
A saída será uma tabela HTML simples como esta:

```
<table>
  <tr>
    <td>Altura</td>
    <td>1,70 m</td>
  </tr>
  <tr>
    <td>Largura</td>
    <td>0,80 m</td>
  </tr>
  <!-- e assim por diante -->
</table>
```

## 📌 Requisitos
Python 3.6 ou superior

beautifulsoup4

## ✅ Licença
Este projeto é livre para uso pessoal ou educacional.