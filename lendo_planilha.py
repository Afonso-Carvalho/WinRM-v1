import pandas as pd

tabela = pd.read_excel('ativos.xlsx') # sheet_name para ler abas da planilha


status = "aaaaa"

tabela.loc[1,'Status'] = status

tabela.to_excel('ativos.xlsx',index=False)

print(tabela)

# host= tabela.iloc[1,2]


# print(host)

# if host =="aaaa":
#     print("oi")
# else:
#     print ("foda")

