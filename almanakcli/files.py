# Standard
import logging

# Third pary
import click
from almanak.file import compress, decompress, extract, fileinfo

files_log = logging.getLogger(__name__)

@click.group(name='files')
def files_cli():
    '''
    Operations on file(s)
    '''
    files_log.warning("warning from click.group(files)")
    pass


@click.command('info', short_help='info on a file, incl. zip-archive')
@click.argument('path', type=click.Path(exists=True, resolve_path=True))
def info_cmd(path):
    '''
    Get information on a file (incl. zip-archives)
    '''
    files_log.info('Called the info-cmd')
    click.echo('This is the info I got.')


@click.command('extract', short_help='extract file from zip-archive')
@click.argument('file', type=click.Path())
@click.argument('archive', type=click.Path(exists=True))
@click.option('--target-dir',
              type=click.Path(writable=True, resolve_path=True),
              help='specify a different directory to extract to')
@click.option('--overwrite',
              is_flag=True,
              help='overwrite any existing file or directory')
def extract_cmd(file, archive, target_dir, overwrite):
    '''
    Extracts a <file> from a <archive> (zip-formatted).
    Returns the full path of the extracted file.
    '''

    # almanak.file.extract returns a path to the extracted file
    out_path = extract(file_path=file,
                       zip_path=archive,
                       out_path=target_dir,
                       overwrite=overwrite)
    click.echo(out_path)


@click.command('zip',
               short_help='zip-compress file or directory')
@click.option('--target-dir',
              type=click.Path(writable=True, resolve_path=True),
              help='specify a different directory to compress to')
@click.option('--target-name',
              type=click.STRING,
              help='specify a new name for the zip-file.')
@click.option('--overwrite',  # not sure overwrite works
              is_flag=True,
              help='overwrite any existing file')
@click.argument('path',
                type=click.Path(exists=True, resolve_path=True))
def zip_cmd(path, target_dir, target_name, overwrite):
    """
    Saves a zip-compressed copy of <PATH> in the same directory.
    Returns the full path to the generated zip-archive.
    """

    # almanak.file.compress returns a path to the compressed archive
    zip_path = compress(path,
                        target=target_dir,
                        name=target_name,
                        overwrite=overwrite)
    click.echo(zip_path)


@click.command('unzip',
               short_help='decompress a zip-archive')
@click.option('--target-dir', 
              type=click.Path(writable=True, resolve_path=True),
              help='specify a different path to extract to')
@click.option('--overwrite',
              is_flag=True,
              help='overwrite any existing files or directories')
@click.argument('path',
                type=click.Path(exists=True, resolve_path=True))
def unzip_cmd(path, target_dir, overwrite):
    """
    Decompresses a zipfile PATH into its parent-directory or TARGET.
    Use OVERWRITE to overwrite any existing file or directory with same name.
    """
    # almanak.file.decompress returns a path to the decompressed file or dir
    zip_path = decompress(path,
                          target=target_dir,
                          overwrite=overwrite)
    click.echo(zip_path)


@click.command('test', short_help='test-cmd')
def test_cmd():
    '''
    Get information on a file (incl. zip-archives)
    '''
    files_log.info('Logger.info: Called the info-cmd')
    files_log.warning('files_log.warning called from inside test_cmd')
    click.echo('click.echo: This is the info I got.')

files_cli.add_command(extract_cmd)
files_cli.add_command(zip_cmd)
files_cli.add_command(unzip_cmd)
files_cli.add_command(test_cmd)
# file_cli.add_command(identify_mcd)
# file_cli.add_command(hash_cmd)
files_cli.add_command(info_cmd)
