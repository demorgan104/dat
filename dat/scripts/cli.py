"""
    DAT Cli implementation using Click package
"""
import os
import click
from dat.api.build_api import BuildApi
from dat.api.release_api import ReleaseApi
from dat.api.new_api import NewApi


@click.group()
def cli():
    """
    TBD
    """


@cli.command()
@click.option("--variant")
def build(variant):
    """
    TBD
    """
    click.echo("Building variant %s" % variant)
    build_api = BuildApi()
    build_api.build(variant)


@cli.command()
@click.option("--release-type")
def release(release_type):
    """
    TBD
    """
    click.echo("Releasing %s" % release_type)
    release_api = ReleaseApi()
    release_api.release()


@cli.command()
@click.option("-d", "--dest", default=os.getcwd())
@click.option("-n", "--name")
@click.option("--force/--no-force", default=False)
# pylint: disable=W0613
def new(dest, name, force):
    """
    TBD
    """
    click.echo("Generating a new package... \n Location: {} \n Name: {}".format(
        dest,
        name
    ))
    new_api = NewApi()
    new_api.new(dest, name, force)
    
