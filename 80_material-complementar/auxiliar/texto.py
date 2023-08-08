import numpy as np

def remove_acentos(string, i=0):
    """
    Remove os acentos da `string` (str).

    Retorna uma string.
    """
    
    # Missing values case:
    if type(string) == type(np.NaN):
        return string
    
    accent_list = [('Ç','C'),('Ã','A'),('Á','A'),('À','A'),('Â','A'),('É','E'),('Ê','E'),('Í','I'),('Õ','O'),('Ó','O'),
                   ('Ô','O'),('Ú','U'),('Ü','U'),('ç','c'),('ã','a'),('á','a'),('à','a'),('â','a'),('é','e'),('ê','e'),
                   ('í','i'),('õ','o'),('ó','o'),('ô','o'),('ú','u'),('ü','u'),('È','E'),('Ö','O'),('Ñ','N'),('è','e'),
                   ('ö','o'),('ñ','n'),('Ë','E'),('ë','e'),('Ä','A'),('ä','a')]
    if i >= len(accent_list):
        return string
    else:
        string = string.replace(*accent_list[i])
        return remove_acentos(string, i + 1)
