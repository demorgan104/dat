import os
import shutil


def generate_conanfile(dst):
    shutil.copy(
        os.path.join(os.path.dirname(__file__), 'conanfile.py'),
        os.path.join(
            dst,
            '_dat_build',
            'conanfile.py'
        )
    )
