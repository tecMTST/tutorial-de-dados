#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Functions for downloading data (and unzipping it).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import requests
import zipfile
import io
import os
import numpy as np


def retrieve_zipped_files(url, save_dir, verbose=True, timeout=10800):
    """
    Downloads a ZIP file and unzip it.
    
    Parameters
    ----------
    url : str
        The URL address of the file to download.        
    save_dir : str
        The path to the folder where to save the unzipped files. New 
        folders are created as needed.      
    verbose : bool (default True)
        Whether or not to print status messages along the process.    
    timeout : int (detault 10800)
        Number of seconds to wait for download before giving up. Default 
        is 3 hours.    
        
    Returns
    -------
    Nothing
    """
    
    assert type(timeout) == int and timeout > 0, '`timeout` should be a int > 0.'
    assert type(url) == str, '`url` should be a str.'
    assert type(save_dir) == str, '`save_dir` should be a str.'
    assert url[-4:].lower() == '.zip', 'Expecting ZIP file.'

    if verbose:
        print('Downloading file...')
    session = requests.session()
    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
    headers  = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330'}
    response = session.get(url, timeout=timeout, headers=headers)

    if response.status_code != 200:
        raise Exception('HTTP request failed with code ' + str(response.status_code))
    
    if verbose:
        print('Unzipping file...')
    z = zipfile.ZipFile(io.BytesIO(response.content))

    z.extractall(save_dir)
    if verbose:
        print('Files unzipped to ' + save_dir)


def Q_arq_dir(caminho, recurso):
    """
    Informa se encontra o `recurso` (str, pode ser nome de arquivo 
    ou de diretório) no `caminho` (str, representando uma pasta).
    
    Returna True ou False.
    """
    # Junta o recurso ao caminho:
    completo = os.path.join(caminho, recurso)
    # Verifica se encontra o recurso:
    encontrou = os.path.isfile(completo) or os.path.isdir(completo)

    return encontrou
        

def sincronizar_arquivos(url, salvar_em, arquivos, verbose=True, timeout=10800, forcar=False):
    """
    Baixa arquivos ZIP caso eles não existam. É possível mandar reescrever também.

    Parâmetros
    ----------
    url : str
        Endereço web do arquivo ZIP.
    salvar_em : str ou path
        Caminho para a pasta onde salvar o conteúdo do arquivo ZIP.
    arquivos : list de str
        Lista de nomes de arquivos que estão dentro do ZIP e que devem aparecem 
        quando ele for descomprimido.
    verbose : bool
        Se é para imprimir mensagens sobre o que está acontecendo ou não.
    timeout : int
        Quanto tempo esperar antes de desistir de pegar a resposta do request 
        (acho que em segundos).
    forcar : bool
        Se é para forçar o download do arquivo e sobrescrever os arquivos ou não.
    """

    # Padroniza input para lista:
    if type(arquivos) == 'str':
        arquivos = [arquivos]

    # Verifica se arquivos existem:
    todos_existem = np.array([Q_arq_dir(salvar_em, a) for a in arquivos]).all()
    
    if (todos_existem == False) or (forcar == True):
        # Se não existir ou se quiser baixar de qualquer jeito, baixa arquivos:
        retrieve_zipped_files(url, salvar_em, verbose=verbose, timeout=timeout)
    else:
        # Se já existir:
        if verbose:
            print('Arquivos já foram baixados')
