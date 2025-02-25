import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.pages.page_dowload import TestDownloadPage


class TestDownload:
    def test_should_dowload_a_file_successfully(self):
        driver = webdriver.Chrome()
        driver.get('https://qaplayground.dev/apps/download/')
        test_download = TestDownloadPage(driver)
        test_download.download_file()
        download_dir = "C:\\Users\\jjack\\Downloads"
        nombre_archivo = "sample.pdf"
        archivos = os.listdir(download_dir)
        archivos_completos = [os.path.join(download_dir, archivo) for archivo in archivos]
        archivos_ordenados = sorted(archivos_completos, key=os.path.getmtime, reverse=True)
        ultimas_descargas = archivos_ordenados[:10]
        nombres_archivos = [os.path.basename(ruta) for ruta in ultimas_descargas]
        assert nombre_archivo in nombres_archivos


if __name__ == "__main__":
    pytest.main()
