"""
    TBD
"""
import os
import shutil
from dat.utils import replacements

# pylint: disable=R0914
def generate_conanfile(dst, config):
    """
    TBD
    """
    # Create the extensions folder
    package_path = config["package_path"]
    extensions_dir = os.path.join(package_path, "extensions")
    extensions_dst = os.path.join(dst, "extensions")
    # Copy default extensions
    extensions_dir_local = os.path.join(os.path.dirname(__file__), "extensions")
    shutil.copytree(extensions_dir_local, extensions_dst)
    # Replace the default ones with the local ones if they exist
    if os.path.exists(extensions_dir):
        for file in os.listdir(extensions_dir):
            extension_file_src = os.path.join(extensions_dir, file)
            extension_file_dst = os.path.join(extensions_dst, file)
            shutil.copyfile(extension_file_src, extension_file_dst)

    requirements = ""
    if "depends" in config:
        for package_name, version_entry in config["depends"].items():
            package = "{package_name}/{version}@stable/release".format(
                package_name=package_name, version=str(version_entry["version"])
            )
            requirements += '"{package}",'.format(package=package)
        requirements = requirements[:-1]  # remove the last ,
    else:
        requirements = '""'

    new_conan_file = os.path.join(dst, "conanfile.py")
    conan_file_template = os.path.join(os.path.dirname(__file__), "conanfile_template")
    replace_dict = {
        "name": config["name"],
        "description": config["description"],
        "url": config["url"],
        "version": config["version"],
        "requirements": requirements,
    }
    replacements.replace_and_create(replace_dict, conan_file_template, new_conan_file)
    return new_conan_file
