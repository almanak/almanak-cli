# Standard library
import logging
from os import path
import sys

# Third party
import click

# Application
from almanakcli.convert import convert_grp


# Setup for CLI-logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# info and higher also to sys.stderr (default stream for Streamhandler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter('%(levelname)-8s %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
# all levels to logfile
file_handler = logging.FileHandler(path.expanduser('~/almanak_log.txt'))
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(name)s %(message)s',
                                   datefmt='%y%m%d_%H:%M:%S')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# https://stackoverflow.com/questions/44344940/python-click-subcommand-unified-error-handling
class CatchAllExceptions(click.Group):
    def __call__(self, *args, **kwargs):
        # http://click.pocoo.org/6/exceptions/#where-are-errors-handled
        try:
            # http://click.pocoo.org/6/exceptions/#what-if-i-don-t-want-that
            return self.main(*args, **kwargs, standalone_mode=False)
        except click.ClickException as e:
            # https://github.com/pallets/click/blob/master/click/exceptions.py#L25
            logger.error(e.format_message())
        except click.Abort:
            # click internally reraises EOFError and KeyboardInterrupt as click.Abort
            raise
        except Exception as e:
            # click.echo("caught unspecified exception in CatchAll")
            logger.error(e)
        
        sys.exit(0)


@click.group(
    name='almanak',
    cls=CatchAllExceptions)
@click.option(
    '--verbose',
    is_flag=True,
    help='output all log-levels to console (stderr)')
@click.version_option()
def cli(verbose):
    '''
    Almanak CLI. Tools, services and workflows for almanak.
    '''
    if verbose:
        console_handler.setLevel(logging.INFO)
    pass


# cli.add_command(files_cli)
cli.add_command(convert_grp)
