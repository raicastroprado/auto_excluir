#codigo criado com a intenção de organizaçao de documentos dentro de uma pasta, ele exclui automaticamente os arquivos selecinados.

import os

def remover_arquivos(pasta, nomes_arquivos):
    arquivos_removidos = 0
    arquivos_nao_encontrados = []
    
    for nome_arquivo in nomes_arquivos:
        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
            arquivos_removidos += 1
        else:
            arquivos_nao_encontrados.append(nome_arquivo)
    
    print(f"Remoção concluída. Total de arquivos removidos: {arquivos_removidos}")
    
    if arquivos_nao_encontrados:
        print("Os seguintes arquivos não foram encontrados:")
        for arquivo in arquivos_nao_encontrados:
            print(arquivo)

# Exemplo de uso:
pasta = fr"C:\Users\rai.magalhaes\Downloads\OUTNFE_20230522175527"  #caminho da pasta 
nomes_arquivos = [""]  #nome dos arquivos que vao ser deletados

remover_arquivos(pasta, nomes_arquivos)
