"""
    Utils module
"""
import os
import shutil


def handle_tmp_folder(location):
    """
    TBD
    """
    if os.path.exists(location):
        shutil.rmtree(location)
    os.mkdir(location)
