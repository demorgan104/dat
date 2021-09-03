"""
    DAT Cli implementation using Click package
"""
import os
import click
from dat.api.build_api import BuildApi
from dat.api.release_api import ReleaseApi
from dat.api.new_api import NewApi
from dat.api.test_api import TestApi
from dat.api.document_api import DocumentApi
from dat.api.run_api import RunApi
from dat.utils.dat_logger import app_logger


@click.group()
def cli():
    """
    Your C/C++ technology stack ready in one second
    """
    # create_logger()


@cli.command()
@click.option("--variant")
def build(variant):
    """
    Build your package
    """
    app_logger.info("Building variant %s", variant)
    build_api = BuildApi()
    build_api.build(variant)


@cli.command()
@click.option("--release-type")
def release(release_type):
    """
    Release a package that was already built
    """
    app_logger.info("Releasing %s", release_type)
    release_api = ReleaseApi()
    release_api.release()


@cli.command()
@click.option("-d", "--dest", default=os.getcwd())
@click.option("-n", "--name")
@click.option("--force/--no-force", default=False)
@click.option("-t", "--template", default=None)
# pylint: disable=W0613
def new(dest, name, template, force):
    """
    Generate a DAT package and start developing
    """
    app_logger.info("Generating a new package...")
    new_api = NewApi()
    new_api.new(dest, name, template, force)


@cli.command()
def test():
    """
    Test your package
    """
    test_api = TestApi()
    test_api.test()


@cli.command()
def run():
    """
    Run the executable of your package
    """
    run_api = RunApi()
    run_api.run()


@cli.command()
def document():
    """
    Document your package
    """
    document_api = DocumentApi()
    document_api.document()
