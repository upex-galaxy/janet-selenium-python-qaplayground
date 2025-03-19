import pytest
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.pages.page_dowload import TestDownloadPage


class TestDownload:
    def test_should_dowload_a_file_successfully(self):

        download_directory = os.path.abspath('./tmp')
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': download_directory}
        chrome_options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://qaplayground.dev/apps/download/')

        test_download = TestDownloadPage(driver)
        test_download.download_file()

        file_name = "sample.pdf"

        archivos = os.listdir(download_directory)
        archivos_completos = [os.path.join(download_directory, archivo) for archivo in archivos]
        archivos_ordenados = sorted(archivos_completos, key=os.path.getmtime, reverse=True)
        ultimas_descargas = archivos_ordenados[:1]
        ruta_del_archivo = os.path.join(download_directory, ultimas_descargas)
        nombres_archivos = [os.path.basename(ruta) for ruta in ultimas_descargas]

        assert file_name in nombres_archivos

        os.remove(ruta_del_archivo)


if __name__ == "__main__":
    pytest.main()
