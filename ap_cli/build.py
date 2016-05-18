import subprocess

import click


@click.command('build')
def build():
    '''(re)Build docker images'''
    click.echo('Building images')
    # let's build the images, this can take a while the first time
    subprocess.call('docker-compose build'.split())
    # now we need to create the containers so we can collect the static files
    subprocess.call('docker-compose up -d'.split())
    # actually collect the static files
    click.echo('Preparing static files...')
    subprocess.call(
        'docker-compose exec django ./manage.py collectstatic --noinput'.split(
        ))
    # stop the containers again
    subprocess.call('docker-compose stop'.split())
    # rebuild to add the new static files to the images
    subprocess.call('docker-compose build'.split())
    click.echo('You can start apostello by running "apostello start"')
