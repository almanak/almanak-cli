# Standard library
import logging
# from pathlib import Path
from os import path
import sys

# Third party
import click
# import almanak

# Application
from almanakcli import file_group as file_commands


# Setup for CLI-logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# info and higher to stdout-handler (default stream for Streamhandler)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(levelname)s %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
# all to logfile
file_handler = logging.FileHandler(path.expanduser('~/almanak_log.txt'))
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(funcname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# @click.option('--verbose', is_flag=True, default=False,
#               help='ouput all log-levels to stdout')
@click.group(name='almanak')
def cli():
    '''
    Almanak CLI. Tools, services and workflows for almanak-repos.
    '''
    # logger.info("cli_cmd called")
    # logger.debug("starting cli")
    # logger.error("Is this showing in stderr?")
    click.echo("logger.handlers")
    click.echo("logger.name: " + str(logger.name))


cli.add_command(file_commands.file_cli)
# cli.add_command(file_commands.compress_cmd)
# cli.add_command(file_commands.decompress_cmd)

if __name__ == '__main__':
    cli()
