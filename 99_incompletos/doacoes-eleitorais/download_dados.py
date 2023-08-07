import requests
from tqdm import tqdm

def get_data_ano(anos):
    for ano in tqdm(anos):
        url=f'https://cdn.tse.jus.br/estatistica/sead/odsele/prestacao_contas/prestacao_de_contas_eleitorais_candidatos_{ano}.zip'

        file_destination = 'dados\\'
        res = requests.get(url)
        if res.status_code == 200:  # http 200 means success
            with open(file_destination, 'wb') as file_handle:  # wb means Write Binary
                file_handle.write(res.content)
        else:
            print(f"Não foi possivel coletar o arquivo erro: {res.status_code}")