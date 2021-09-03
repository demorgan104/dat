"""
    DAT package test API
"""
import os

# pylint: disable=W0611
import subprocess
from dat.errors.dat_exception import DatException


class RunApi:
    """
    TBD
    """

    # pylint: disable=too-few-public-methods
    def __init__(self) -> None:
        self.current_dir = os.getcwd()

    # pylint: disable=R1732,W0122
    def run(self):
        """
        Document api implementation
        """
        extensions_dir = os.path.join(self.current_dir, "extensions")
        run_extensions = os.path.join(extensions_dir, "run.py")
        if not os.path.exists(run_extensions):
            raise DatException(
                "You should place a run.py script inside extensions folder !"
            )
        exec(open(run_extensions).read())
        # run_app()
