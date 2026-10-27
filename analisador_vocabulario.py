import re
import collections
# analized_text = input("Digite um texto para analisar: ")
# # Split by comma, semicolon, or space
# result = re.split(r"[,;\s]+", text)
# print(result)  # ['apple', 'banana', 'orange', 'grape']

print("ANALISADOR DE TEXTO")

while True:
    options = input("Digite:\n1 - Adicionar\n2 - Analisar o texto\n3 - Estatísticas\n4 - Sair\n: ")
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
            print("Até logo!")
            break

        case _:
            print("Opção não encontrada")