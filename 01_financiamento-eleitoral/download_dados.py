import os
import requests
from tqdm import tqdm
import zipfile

class DataDownloader:
    def __init__(self, base_dir='dados/brutos'):
        self.base_dir = base_dir
        self.base_url = 'https://cdn.tse.jus.br/estatistica/sead/odsele/'
        self._create_global_directories()

    def _create_global_directories(self):
        # Cria os diretórios de destino se não existirem
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def download_file(self, url, destination):
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(destination, 'wb') as file_handle:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file_handle.write(chunk)
        except requests.exceptions.RequestException as e:
            print(f"Não foi possível coletar o arquivo. Erro: {e}")

    def unzip_file(self, zip_file_path, destination_dir):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_dir)

class VotacaoSecaoDownloader(DataDownloader):
    def __init__(self, base_dir='dados/brutos'):
        super().__init__(base_dir)
        self.votacao_secao_dir = os.path.join(base_dir, 'votacao_secao')
        self._create_directories()

    def _create_directories(self):
        super()._create_global_directories()
        # Cria o diretório específico para votacao_secao
        if not os.path.exists(self.votacao_secao_dir):
            os.makedirs(self.votacao_secao_dir)

    def download(self, anos, uf):
        for ano in tqdm(anos, desc="Downloading Votacao Secao"):
            url = f'{self.base_url}votacao_secao/votacao_secao_{ano}_{uf}.zip'
            file_destination = os.path.join(self.votacao_secao_dir, f'resultado_{ano}_{uf}.zip')
            self.download_file(url, file_destination)

    def unzip(self, anos, uf):
        for ano in tqdm(anos, desc="Descompactando zipfile"):
            zip_file_path = os.path.join(self.votacao_secao_dir, f'resultado_{ano}_{uf}.zip')
            csv_file_path = os.path.join(self.base_dir, uf, str(ano))
            self.unzip_file(zip_file_path, csv_file_path)

class PrestacaoContasDownloader(DataDownloader):
    def download(self, anos):
        for ano in tqdm(anos, desc="Downloading Prestacao de Contas"):
            url = f'{self.base_url}prestacao_contas/prestacao_de_contas_eleitorais_candidatos_{ano}.zip'
            file_destination = os.path.join(self.base_dir, f'prestacao_de_contas_eleitorais_candidatos_{ano}.zip')
            self.download_file(url, file_destination)

class ColigacaoDownloader(DataDownloader):
    def __init__(self, base_dir='dados/brutos'):
        super().__init__(base_dir)
        self.coligacao_dir = os.path.join(base_dir, 'coligacao')
        self._create_directories()

    def _create_directories(self):
        super()._create_global_directories()
        # Cria o diretório específico para coligacao
        if not os.path.exists(self.coligacao_dir):
            os.makedirs(self.coligacao_dir)

    def download(self, anos):
        for ano in tqdm(anos, desc="Downloading Coligação Secao"):
            url = f'{self.base_url}consulta_coligacao/consulta_coligacao_{ano}.zip'
            file_destination = os.path.join(self.coligacao_dir, f'coligacao_{ano}.zip')
            self.download_file(url, file_destination)

    def unzip(self, anos, uf):
        coligacao_dir = os.path.join(self.base_dir, 'coligacao')
        for ano in tqdm(anos, desc="Descompactando zipfile"):
            zip_file_path = os.path.join(coligacao_dir, f'coligacao_{ano}.zip')
            csv_file_path = os.path.join(self.base_dir, uf, str(ano))
            self.unzip_file(zip_file_path, csv_file_path)

class CandidatoDownloader(DataDownloader):
    def __init__(self, base_dir='dados/brutos'):
        super().__init__(base_dir)
        self.coligacao_dir = os.path.join(base_dir, 'candidato')
        self._create_directories()

    def _create_directories(self):
        super()._create_global_directories()
        # Cria o diretório específico para coligacao
        if not os.path.exists(self.coligacao_dir):
            os.makedirs(self.coligacao_dir)

    def download(self, anos):
        for ano in tqdm(anos, desc="Downloading Coligação Secao"):
            url = f'{self.base_url}consulta_cand/consulta_cand_{ano}.zip'
            file_destination = os.path.join(self.coligacao_dir, f'candidato_{ano}.zip')
            self.download_file(url, file_destination)

    def unzip(self, anos, uf):
        coligacao_dir = os.path.join(self.base_dir, 'candidato')
        for ano in tqdm(anos, desc="Descompactando zipfile"):
            zip_file_path = os.path.join(coligacao_dir, f'consulta_cand_{ano}.zip')
            csv_file_path = os.path.join(self.base_dir, uf, str(ano))
            self.unzip_file(zip_file_path, csv_file_path)

if __name__ == "__main__":
    votacao_secao_downloader = VotacaoSecaoDownloader()
    prestacao_contas_downloader = PrestacaoContasDownloader()
    coligacao_downloader = ColigacaoDownloader()
    candidato_dowloader = CandidatoDownloader()


    anos_votacao_secao = [2021, 2022]
    uf_votacao_secao = 'SP'

    anos_prestacao_contas = [2021, 2022]

    votacao_secao_downloader.download(anos_votacao_secao, uf_votacao_secao)
    prestacao_contas_downloader.download(anos_prestacao_contas)

    coligacao_downloader.download([2022])
    coligacao_downloader.unzip([2022], 'SP')
