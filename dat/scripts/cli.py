import click
import pathlib
import os
from dat.errors.dat_exception import DatException


@click.group()
def cli():
    pass


@cli.command()
@click.option('--variant')
def build(variant):
    click.echo('Building variant %s' % variant)


@cli.command()
@click.option('--release-type')
def release(release_type):
    click.echo('Releasing %s' % release_type)

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
        



    


