import re
import collections
from reportlab.pdfgen           import canvas
from reportlab.lib.pagesizes    import A4
from reportlab.lib              import colors
from reportlab.platypus         import Table, TableStyle

def generate_statistics_pdf(list_result):
    if not list_result:
        print("Analise um texto antes de gerar o PDF.")
        return

    words = [
        element.casefold()
        for element in list_result
        if element and element.isalpha()
    ]

    symbols = [
        element
        for element in list_result
        if element and not element.isalnum()
    ]

    word_counter = collections.Counter(words)
    symbol_counter = collections.Counter(symbols)

    table_data = [
        ["Categoria", "Elemento", "Quantidade"],
        ["Resumo", "Total de elementos", len(list_result)],
        ["Resumo", "Total de palavras", len(words)],
    ]

    for word, quantity in word_counter.most_common():
        table_data.append(["Palavra", word, quantity])

    for symbol, quantity in symbol_counter.most_common():
        table_data.append(["Símbolo", symbol, quantity])

    pdf = canvas.Canvas("estatisticas_texto.pdf", pagesize=A4)
    pdf.setTitle("Estatísticas do texto")

    pdf.setFontSize(18)
    pdf.drawCentredString(300, 800, "ESTATÍSTICAS DO TEXTO")

    statistics_table = Table(
        table_data,
        colWidths=[120, 280, 100]
    )

    statistics_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (2, 1), (2, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    table_width, table_height = statistics_table.wrapOn(pdf, 0, 0)
    statistics_table.drawOn(pdf, 40, 740 - table_height)

    pdf.save()
    print("PDF criado: estatisticas_texto.pdf")

print("ANALISADOR DE TEXTO")

while True:
    options = input(
        "Digite:\n"
        "1 - Adicionar\n"
        "2 - Analisar o texto\n"
        "3 - Estatísticas\n"
        "4 - Gerar PDF\n"
        "5 - Sair\n"
        ": "
    )
    match options:
        case "1":   #adição do texto
            analized_text = input("Digite um texto para analisar\n: ")
            while not analized_text or len(analized_text) <= 2:
                analized_text = input("Local vazio ou menor do que o necessário. Digite um texto válido\n: ")

        case "2":   #analisar o texto
            list_result = re.findall(r"\w+|[^\w\s]|\s+", analized_text)

            list_result = [
                "" if element.isspace() else element
                for element in list_result
            ]

            print(list_result)
        
        case "3": # estatisticas básicas
            if not analized_text:
                print("Adicione um texto para receber as estatísticas")
            else:
                # contagem de palavras
                words = [
                    element.casefold()
                    for element in list_result
                    if element and element.isalpha()
                ]
                word_counter = collections.Counter(words)

                # contagem de simbolos
                symbols = [
                    element
                    for element in list_result
                    if element and not element.isalnum()
                ]
                symbol_counter = collections.Counter(symbols)

                # total de palavras
                total_words = sum(word_counter.values())

                print("ESTATÍSTICAS")

                print("\nPALAVRAS MAIS FREQUENTES")
                print(f"{'PALAVRA':<20} {'QUANTIDADE':>10}")
                print("-" * 32)

                for word, quantity in word_counter.most_common():
                    print(f"{word:<20} {quantity:>10}")

                if symbol_counter:
                    print("\nSÍMBOLOS MAIS FREQUENTES")
                    print(f"{'SÍMBOLO':<20} {'QUANTIDADE':>10}")
                    print("-" * 32)

                    for symbol, quantity in symbol_counter.most_common():
                        print(f"{symbol:<20} {quantity:>10}")
                else:
                    print("\nNenhum símbolo encontrado")

                # quantidade de palavras
                print(f"Quantidade total de elementos: {len(list_result)}")
                print(f"Quantidade total de palavras: {total_words}")
            
            print("\n")
        
        case "4":   #sair do programa
            generate_statistics_pdf(list_result)

        case "5":   #sair do programa
            print("Até logo!")
            break

        case _:
            print("Opção não encontrada")