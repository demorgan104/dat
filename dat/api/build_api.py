import os
import subprocess
import shutil
from dat.core.conf_reader import get_package_config
from dat.conan.conan_handler import generate_conanfile

class BuildApi(object):

    def __init__(self):
        self.current_dir = os.getcwd()


    def execute_conan_steps(self, dat_tmp, generated_conan_file, config):
        dat_tmp_tmp = os.path.join(dat_tmp, 'tmp')
        source_folder = os.path.join(dat_tmp_tmp, 'source')
        install_folder = os.path.join(dat_tmp_tmp, 'install')
        build_folder = os.path.join(dat_tmp_tmp, 'build')
        package_folder = os.path.join(dat_tmp_tmp, 'package')
        source_folder_flag = "--source-folder={}".format(source_folder)
        install_folder_flag = "--install-folder={}".format(install_folder)
        build_folder_flag = "--build-folder={}".format(build_folder)
        package_folder_flag = "--package-folder={}".format(package_folder)
        source_cmd = "conan source {conan_file} {source_folder_flag}".format(
            conan_file = generated_conan_file,
            source_folder_flag = source_folder_flag
        )
        install_cmd = "conan install {conan_file} {install_folder_flag}".format(
            conan_file = generated_conan_file,
            install_folder_flag = install_folder_flag
        )
        build_cmd = "conan build {conan_file} {source_folder_flag} {install_folder_flag} {build_folder_flag}".format(
            conan_file = generated_conan_file,
            source_folder_flag = source_folder_flag,
            install_folder_flag = install_folder_flag,
            build_folder_flag = build_folder_flag
        )
        package_cmd = "conan package {conan_file} {source_folder_flag} {install_folder_flag} {build_folder_flag} {package_folder_flag}".format(
            conan_file = generated_conan_file,
            source_folder_flag = source_folder_flag,
            install_folder_flag = install_folder_flag,
            build_folder_flag = build_folder_flag,
            package_folder_flag = package_folder_flag
        )

        export_package_cmd = "conan export-pkg {conan_file} {pkg_id} {source_folder_flag} {install_folder_flag} {build_folder_flag} --force".format(
            conan_file = generated_conan_file,
            source_folder_flag = source_folder_flag,
            install_folder_flag = install_folder_flag,
            build_folder_flag = build_folder_flag,
            pkg_id = "stable/release"
        )

        cmd_flow = [
            source_cmd,
            install_cmd,
            build_cmd,
            package_cmd,
            export_package_cmd
        ]

        for cmd in cmd_flow:
            print('Executing cmd "{}"'.format(cmd))
            subprocess.run(
                cmd.split(' ')
            )


    def handle_tmp_folder(self, location):
        if os.path.exists(location):
            shutil.rmtree(location)
        os.mkdir(
            location
        )


    def build(self, variant):
        print('current path: {}'.format(__file__))
        print('current dir: {}'.format(self.current_dir))
        config = get_package_config(os.getcwd())
        dat_tmp_folder = os.path.join(
            self.current_dir,
            '_dat_build'
        )
        self.handle_tmp_folder(
            dat_tmp_folder
        )
        generated_conan_file = generate_conanfile(
            dat_tmp_folder,
            config
        )
        self.execute_conan_steps(
            dat_tmp_folder,
            generated_conan_file,
            config
        )
        
        

    # Support with statement in the future
    def __enter__(self):
        pass 


    def __exit__(self):
        pass
