# Analisador de Texto e Vocabulário (CLI)

Um programa de terminal desenvolvido em Python para analisar textos, extrair estatísticas de frequência de palavras, identificar símbolos/pontuações e contar a densidade de elementos. 

Este projeto foi construído para praticar o processamento básico de texto, utilizando **Expressões Regulares (`re`)**, **List Comprehensions**, métodos de sanitização de strings e o módulo nativo **`collections`**.

## Funcionalidades

- **Entrada e validação de texto:** recebe textos do usuário com validação para impedir entradas vazias ou com menos de 3 caracteres.
- **Tokenização com RegEx:** utiliza expressões regulares como `re.findall` para separar palavras, pontuações e símbolos de forma precisa.
- **Contagem de frequência de palavras:** transforma os termos para minúsculas (`.casefold()`), ignora espaços/pontuações e contabiliza as ocorrências de cada palavra usando `collections.Counter`.
- **Análise de símbolos:** identifica e ranqueia pontuações e caracteres especiais separadamente.
- **Relatório tabular:** exibe os resultados no terminal organizados em tabelas com alinhamento de colunas, mostrando os termos mais frequentes (`.most_common()`) e as contagens totais.

## 🔮 *Feats* Futuras

- [x] **Exportação em PDF:** exportar o relatório estatístico gerado para um arquivo PDF.
- [ ] **Detector de similaridade:** *input* de dois textos e o programa calcula quantas palavras eles têm em comum.

## ⚙️ Pré-requisitos

Para rodar este projeto, você precisa ter o **Python 3.10 ou superior** instalado no seu computador, pois o código utiliza a estrutura moderna de controle de fluxo `match/case`.

## 💻 Como clonar e executar para uso próprio

Se você quiser testar este projeto na sua máquina, siga os passos abaixo:

1. Abra o seu terminal (ou Git Bash).
2. Clone este repositório executando o comando:
   ```bash
   git clone https://github.com/nathanmontt/analisador_vocabulario.git
3. Execute o arquivo Python:
   ```bash
   python analisador_vocabulario.py