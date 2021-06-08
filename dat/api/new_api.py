"""
    Generates a completely functional DAT package
"""
import os
import shutil
import yaml
from dat.errors.dat_exception import DatException


class NewApi:
    """
        TBD
    """
    def __init__(self) -> None:
        pass

    @staticmethod
    def replace_name_in_content(content, name):
        """
            TBD
        """
        return content.replace("<${TEMPLATE_NAME}>", name)

    @staticmethod
    def is_file_entry(value):
        """Checks that an entry in the root is a file or not
        Args:
            value: Possible File content. This is always a list in case the file has a content.
                   In case the file should be empty, the value will be None.
        Returns:
            If the key represents a file
        """
        if value is None:
            return False
        return "None" in value or isinstance(value, list)

    #pylint: disable=R0913
    def generate_file(
        self, file_name, content_identifier, root_dir, tags, template_name
    ):
        """
            TBD
        """
        if content_identifier == "None":
            open(os.path.join(root_dir, file_name), "w").close()
        else:
            # Use the content_identifier to get the content from top config
            try:
                tag = next(iter(content_identifier))
                content = tags[tag]
                file_path = os.path.join(root_dir, file_name)
                if os.path.exists(file_path):
                    os.remove(file_path)
                with open(file_path, "w") as file:
                    content = self.replace_name_in_content(content, template_name)
                    file.write(content)
            except KeyError:
                print(
                    "Could not find {content_id}".format(content_id=content_identifier)
                )
                open(os.path.join(root_dir, file_name), "w").close()

    def generate_structure(self, config, root_dir, tags, template_name):
        """
            TBD
        """
        for key, value in config.items():
            if self.is_file_entry(value):
                self.generate_file(key, value, root_dir, tags, template_name)
            else:
                new_dir = os.path.join(root_dir, key)
                os.mkdir(new_dir)
                if not value is None:
                    self.generate_structure(value, new_dir, tags, template_name)

    def new(self, dest, name, forced=False):
        """
        TBD
        """
        print("Generating a DAT package")

        template_file = os.path.join(
            os.path.dirname(__file__), "..", "templates", "basic.yml"
        )
        with open(template_file, "r") as input_stream:
            print(
                "Loading template descriptor {descriptor_location}".format(
                    descriptor_location=template_file
                )
            )
            descriptor_content = yaml.safe_load(input_stream)

        if not name:
            raise DatException("Please provide a name for your package !")
        # Create root dir
        package_name = self.replace_name_in_content(descriptor_content["name"], name)
        root_dir = os.path.join(dest, package_name)
        if not os.path.exists(root_dir):
            os.mkdir(root_dir)
        else:
            if forced:
                print(
                    "Removing directory {dir} because it already exists !".format(
                        dir=root_dir
                    )
                )
                shutil.rmtree(root_dir)
                os.mkdir(root_dir)
            else:
                raise DatException(
                    "The package you are trying to generate already exists !"
                )

        self.generate_structure(
            descriptor_content["root"],
            root_dir,
            {key: value for key, value in descriptor_content.items() if key != "root"},
            name,
        )
        print("Package generated at {destination}".format(destination=root_dir))
        if "description" in descriptor_content:
            print(descriptor_content["description"])
