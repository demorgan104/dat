import os
import subprocess
from dat.core.conf_reader import get_package_config


class ReleaseApi(object):
    def __init__(self) -> None:
        super().__init__()
        self.current_dir = os.getcwd()

    def release(self):
        config = get_package_config(os.getcwd())

        print("releasing package {}".format(config["name"]))
        package_id = "{name}/{version}@stable/release".format(
            name=config["name"], version=config["version"]
        )
        # add the remote (this should be removed later)
        remote_name = "art-local"
        remote_url = "http://localhost:8084/artifactory/api/conan/dat-packages"
        verify_ssl = True
        conan_remote_url_cmd = (
            "conan remote add {remote_name} {remote_url} {verify_ssl}".format(
                remote_name=remote_name, remote_url=remote_url, verify_ssl=verify_ssl
            )
        )
        try:
            subprocess.run(conan_remote_url_cmd.split())
        except:
            print("Conan remote URL already exists !")

        upload_cmd = "conan upload -r {remote_name} {package_id} --all".format(
            remote_name=remote_name, package_id=package_id
        )
        subprocess.run(upload_cmd.split())
