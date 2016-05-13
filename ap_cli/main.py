import os
import subprocess
from datetime import datetime

import click

from ap_cli import apostello
from ap_cli import build
from ap_cli import config
from ap_cli import db
from ap_cli import dev
from ap_cli import init
from ap_cli import upgrade


@click.group()
def cli():
    """Setup, configure, and deploy an instance of apostello."""
    pass


cli.add_command(apostello.logs)
cli.add_command(apostello.start)
cli.add_command(apostello.stop)

cli.add_command(config.config)

cli.add_command(db.backup)
cli.add_command(db.restore)
cli.add_command(db.migrate)

cli.add_command(init.init)

cli.add_command(upgrade.upgrade)

cli.add_command(build.build)
# dev:
cli.add_command(dev.start_dev)
cli.add_command(dev.build_assets)
