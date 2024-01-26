import numpy as np


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


def ptbr_number(number_str):
    """
    Change the format of a string `number_str` representing a number 
    from US style to BR style.
    
    Returns a string.
    """
    
    ptbr_number = number_str.replace(',', '>')
    ptbr_number = ptbr_number.replace('.', ',')
    ptbr_number = ptbr_number.replace('>', '.')
    
    return ptbr_number


def fmt(value, holder):
    """
    Returns a string where `value` (float) follows
    the format `holder` (str, e.g: '{:.2f}'). The
    decimals and separators are Brazilian-style.
    """
    
    # Ignore decimals if they are zero:
    if np.isclose(value % 1, 0):
        n_digits = holder[holder.find('.') + 1]
        h = holder.replace('.{}f'.format(n_digits), '.0f')
    else:
        h = holder
        
    return ptbr_number(h.format(value))


def number_BM_notation(value):
    """
    Returns a shortened string version of number `value` (float)
    using Brasilian decimal separators and 'M' for million and
    'B' for billion.
    
    E.g.: 1200000 -> 1,2M
    """
    
    if np.abs(value) < 100:
        return fmt(value, '{:.2f}')
    if np.abs(value) < 10000:
        return fmt(value, '{:,.0f}')
    if np.abs(value) < 1e5:
        return fmt(value / 1000, '{:.1f} mil')
    if np.abs(value) < 1e6:
        return fmt(value / 1000, '{:.0f} mil')
    if np.abs(value) < 1e7:
        return fmt(value / 1e6, '{:.1f}M')
    if np.abs(value) < 1e9:
        return fmt(value / 1e6, '{:.0f}M')
    if np.abs(value) < 1e10:
        return fmt(value / 1e9, '{:.1f}B')
    if np.abs(value) < 1e12:
        return fmt(value / 1e9, '{:.0f}B')
    
    # Deafult:
    return fmt(value, '{:.0f}')
