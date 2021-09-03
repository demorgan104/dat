"""
    DAT package test API
"""
import os
import subprocess
import webbrowser
from dat.utils.dat_logger import app_logger
from dat.errors.dat_exception import DatException


class DocumentApi:
    """
    TBD
    """

    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        self.current_dir = os.getcwd()

    def document(self):
        """
        Document api implementation
        """
        app_logger.info("Document api")
        doc_dir = os.path.join(self.current_dir, "doc")
        os.chdir(doc_dir)
        mkdocs_cmd = ["mkdocs", "serve"]
        try:
            webbrowser.open("http://localhost:8000/")
            subprocess.run(mkdocs_cmd, check=True)
        except subprocess.CalledProcessError as error:
            app_logger.error("Error executing %s", mkdocs_cmd, exc_info=True)
            raise DatException(error) from error
