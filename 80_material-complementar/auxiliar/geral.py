def mostra_linhas(arquivo, linha_ini=None, linha_fim=None, encoding='utf-8'):
    """
    Imprime um grupo de linhas de um arquivo de texto.
    
    Parâmetros
    ----------
    arquivo : str
        Nome do arquivo, por ex.: "obitos_2010-2019.csv".
    linha_ini : int ou None
        Número da primeira linha a ser impressa (começando por 0).
    linha_fim : int ou None
        Número da linha seguinte à última impressa.
    encoding : str
        Encoding do texto do arquivo ('utf-8', 'latin-1' ou outro).
    """
    
    # Abre o arquivo:
    with open(arquivo, 'r', encoding=encoding) as f:
        # Seleciona as linhas:
        lines = f.read().split('\n')[linha_ini:linha_fim]
        # Junta num único texto:
        text  = '\n'.join(lines)
        # Imprime:
        print(text)
        
        
def codifica_string(texto, encoding):
    """
    Transforma uma string `texto` em uma lista de números binários, 
    dado um encoding.
    """
    
    seq = [bin(byte)[2:] for byte in bytes(texto, encoding)]
    
    return seq