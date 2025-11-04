import chardet

path = r"C:\Users\PC\Desktop\projetos\Projeto_Nara\NARA_csv\produtos.csv"

# Ler um pedaço do arquivo pra detectar o encoding
with open(path, 'rb') as f:
    result = chardet.detect(f.read(50000))  
print(result)
