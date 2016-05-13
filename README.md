This is a command line tool to make deploying [apostello](https://github.com/monty5811/apostello) with docker easier.

## Prerequisites

 * Python 3
 * Docker - follow the [install instruction](https://docs.docker.com/engine/installation/) or use [Digital Ocean](https://m.do.co/c/4afdc8b5be2e)'s one-click Docker droplet to get going quickly.
 * git

This has only been tested on Ubuntu 16.04, but should work with 14.04 and other Linux distributions.


## Installation


```
git clone https://github.com/monty5811/apostello-docker-cli.git
cd apostello-docker-cli
# activate a virtualenv
pip install .
```

## Deploying apostello


```
cd # move to where you want apostello to be installed
apostello init # pull down the apostello repo
cd apostello
apostello config # configure apostello settings
apostello build # build docker images and run collectstatic
apostello start # start the application
apostello migrate # initialise the database
```

apostello should now be running on your server. Open your browser and navigate to the IP address/hostname for your server.

## Backups


Backups are stored in `apostello/docker/backups`:

 * The .caddy folder containing any SSL certificates is kept here
 * You can backup your apostello database any time by running `apostello db_backup`. The backups will be in the `postgres` folder

It is up to you to back up this folder regularly.

## Upgrades


To upgrade, make sure you are in the apostello folder and run

```
apostello upgrade
```

This will result in a short down time while apostello is updated.

## Usage


```
Usage: apostello [OPTIONS] COMMAND [ARGS]...

  Setup, configure, and deploy an instance of apostello.

Options:
  --help  Show this message and exit.

Commands:
  build         (re)Build docker images
  build-assets  Rebuild the frontend assets
  config        Interactive config of env file
  db_backup     Backup current state of database
  db_restore    Rebuild db from a backup
  init          Initialise apostello folder
  logs          Show apostello logs
  migrate       Apply database migrations
  start         Start apostello production environment
  start-dev     Start a development environment
  stop          Stop apostello production environment
  upgrade       Upgrade apostello
````
