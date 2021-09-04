"""
    Generates a completely functional DAT package
"""
import os
import shutil
import yaml
from dat.errors.dat_exception import DatException
from dat.utils.dat_logger import app_logger


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

    # pylint: disable=R0913, R1732
    def generate_file(
        self, file_name, content_identifier, root_dir, tags, template_name, forced
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
                if os.path.exists(file_path) and forced:
                    os.remove(file_path)
                    with open(file_path, "w") as file:
                        content = self.replace_name_in_content(content, template_name)
                        file.write(content)
                elif not os.path.exists(file_path):
                    with open(file_path, "w") as file:
                        content = self.replace_name_in_content(content, template_name)
                        file.write(content)
            except KeyError:
                app_logger.error(
                    "Could not find %s",
                    content_identifier,
                    exc_info=True,
                )
                open(os.path.join(root_dir, file_name), "w").close()

    def generate_structure(self, config, root_dir, tags, template_name, forced):
        """
        TBD
        """
        for key, value in config.items():
            if self.is_file_entry(value):
                self.generate_file(key, value, root_dir, tags, template_name, forced)
            else:
                new_dir = os.path.join(root_dir, key)
                if forced or not os.path.exists(new_dir):
                    os.mkdir(new_dir)
                if not value is None:
                    self.generate_structure(value, new_dir, tags, template_name, forced)

    def new(self, dest, name, template, forced=False):
        """
        TBD
        """
        app_logger.info(
            "Generating the package: \n Name: %s \n Location: %s", name, dest
        )
        template_file = os.path.join(
            os.path.dirname(__file__), "..", "templates", "bazel_hello.yml"
        )
        if template:
            template_file = os.path.join(template)

        app_logger.info("Using the template file %s", template_file)

        with open(template_file, "r") as input_stream:
            app_logger.info("Loading template descriptor %s", template_file)
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
                app_logger.warning(
                    "Removing directory %s because it already exists !", root_dir
                )
                shutil.rmtree(root_dir)
                os.mkdir(root_dir)
            else:
                app_logger.warning(
                    "Only generating files that don't exist !"
                )

        self.generate_structure(
            descriptor_content["root"],
            root_dir,
            {key: value for key, value in descriptor_content.items() if key != "root"},
            name,
            forced,
        )
        app_logger.info("Package generated at %s", root_dir)
        if "description" in descriptor_content:
            app_logger.info(descriptor_content["description"])
