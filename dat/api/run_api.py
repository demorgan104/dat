"""
    DAT package test API
"""
import os
import subprocess
import webbrowser
from dat.utils.dat_logger import app_logger
from dat.errors.dat_exception import DatException


class RunApi:
    """
    TBD
    """

    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        self.current_dir = os.getcwd()

    def run(self):
        """
        Document api implementation
        """
        extensions_dir = os.path.join(self.current_dir, 'extensions')
        run_extensions = os.path.join(extensions_dir, "run.py")
        if not os.path.exists(run_extensions):
            raise DatException("You should place a run.py script inside extensions folder !")
        exec(open(run_extensions).read())
        #run_app()
