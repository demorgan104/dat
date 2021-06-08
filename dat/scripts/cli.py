"""
    DAT Cli implementation using Click package
"""
import os
import click
from dat.api.build_api import BuildApi
from dat.api.release_api import ReleaseApi
from dat.api.new_api import NewApi
from dat.utils.dat_logger import app_logger


@click.group()
def cli():
    """
    Your C/C++ technology stack ready in one step
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
# pylint: disable=W0613
def new(dest, name, force):
    """
    Generate a DAT package and start developing
    """
    app_logger.info(
        "Generating a new package... \n Location: %s \n Name: %s", dest, name
    )
    new_api = NewApi()
    new_api.new(dest, name, force)
