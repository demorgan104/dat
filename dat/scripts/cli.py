import click
import pathlib
import os
import subprocess
from dat.errors.dat_exception import DatException
from dat.api.build_api import BuildApi
from dat.api.release_api import ReleaseApi


@click.group()
def cli():
    pass


@cli.command()
@click.option('--variant')
def build(variant):
    click.echo('Building variant %s' % variant)
    build_api = BuildApi()
    build_api.build(variant)


@cli.command()
@click.option('--release-type')
def release(release_type):
    click.echo('Releasing %s' % release_type)
    release_api = ReleaseApi()
    release_api.release()
    

@cli.command()
@click.option('-d', '--dest', default=os.getcwd())
@click.option('-n', '--name')
def new(dest, name):
    template_elems = [
        'conf',
        'doc',
        'metrics',
        'src',
        'tests'
    ]
    if dest:
        if not os.path.exists(dest):
            raise DatException(
            'Destination {} doesn\'t exist'.format(
                dest
            )
        )

    for elem in template_elems:
        path = os.path.join(dest, elem)
        os.mkdir(path)
        



    


