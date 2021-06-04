"""
    DAT Cli implementation using Click package
"""
import os
import click
from dat.errors.dat_exception import DatException
from dat.api.build_api import BuildApi
from dat.api.release_api import ReleaseApi


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
# pylint: disable=W0613
def new(dest, name):
    """
    TBD
    """
    template_elems = ["conf", "doc", "metrics", "src", "tests"]
    if dest:
        if not os.path.exists(dest):
            raise DatException("Destination {} doesn't exist".format(dest))

    for elem in template_elems:
        path = os.path.join(dest, elem)
        os.mkdir(path)
