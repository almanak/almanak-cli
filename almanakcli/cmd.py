# Standard library
import logging
# from pathlib import Path
from os import path
# import sys

# Third party
import click
# import almanak

# Application
from almanakcli import files


# Setup for CLI-logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# info and higher also to stderr (default stream for Streamhandler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(levelname)s %(name)s %(message)s")
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
# all levels to logfile
file_handler = logging.FileHandler(path.expanduser('~/almanak_log.txt'))
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# https://stackoverflow.com/questions/44344940/python-click-subcommand-unified-error-handling
class CatchAllExceptions(click.Group):
    def __call__(self, *args, **kwargs):
        try:
            return self.main(*args, **kwargs)
        except Exception as exc:
            click.echo('We found %s' % exc)


# https://stackoverflow.com/questions/45875930/is-there-a-way-to-handle-exceptions-automatically-with-python-click
def safe_cli():
    try:
        click.echo("channeling through safe_cli...")
        cli()
    except Exception as e:
        logger.exception()
        click.echo(e)
        

# @click.option('--verbose', is_flag=True, default=False,
#               help='ouput all log-levels to stdout')
# This is not tested yet
# @click.group(name='almanak', cls=CatchAllExceptions)
@click.group(name='almanak')
def cli():
    '''
    Almanak CLI. Tools, services and workflows for almanak-repos.
    '''
    click.echo('entering cli-commandgroup...')
    pass
    # logger.info("cli_cmd called")
    # logger.error("Is this showing in stderr?")
    # click.echo("logger.name: " + str(logger.name))


cli.add_command(files.files_group)
# cli.add_command(file_commands.compress_cmd)
# cli.add_command(file_commands.decompress_cmd)

# if __name__ == '__main__':
#     cli()
