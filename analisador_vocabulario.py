import re

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
            # list_result = re.split(r"([^\w\s]+|\s+)", analized_text)
            # print(list_result)  # ['apple', 'banana', 'orange', 'grape']
            # continue

            # list_result = re.split(r"([^\w\s]+|\s+)", analized_text)

            # list_result = [
            #     "" if element.isspace() else element
            #     for element in list_result
            # ]

            # print(list_result)

            list_result = re.findall(r"\w+|[^\w\s]+|\s", analized_text)

            list_result = [
                "" if element.isspace() else element
                for element in list_result
            ]

            print(list_result)
        
        case "3": # estatisticas básicas
            # if not original_sorteador_nome_set:
            #     print("Adicione um texto para receber as estatísticas")
            # else:
                # print("ESTATÍSTICAS DO SORTEIO")
                # print(f"Quantidade total de participantes: {len(set_copy)}")

                # result = len(set_copy) - len(original_sorteador_nome_set)
                # print(f"Quantidade de participantes restantes (total - já sorteados) = {result}")
                # for each_participant in original_sorteador_nome_set:
                #     print(each_participant)

                # print(f"Quantidade de sorteios já feitos: {draw_cont}")
                # print()
            continue
        
        case "4":   #sair do programa
            print("Até logo!")
            break

        case _:
            print("Opção não encontrada")