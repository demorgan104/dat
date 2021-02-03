import click

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


    


