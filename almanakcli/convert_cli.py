# Standard
import logging
from pathlib import Path

# Third pary
import click

convert_log = logging.getLogger(__name__)

@click.group(name='convert')
def convert_cli():
    '''
    Conversion of files
    '''
    convert_log.warning("Warning from click.group(files)")
    pass


@click.command('convert', short_help='convert file(s)')
@click.argument('src', type=click.Path(exists=True, resolve_path=True, allow_dash=True))
@click.argument('dest', type=click.Path(resolve_path=True, allow_dash=True))
@click.option('--batch',
              is_flag=True,
              help='')
@click.option('--overwrite',
              is_flag=True,
              help='overwrite any existing file or directory')
def convert_cmd(src, dest, batch, overwrite):
    '''
    Convert source to destination.
    Returns the full path of the extracted file.
    '''
    if Path(src).is_dir():
        for f in Path(src).iterdir():
            if 
        



@click.command('info', short_help='prints filename')
@click.argument('path', type=click.Path(exists=True, resolve_path=True))
def info_cmd(path):
    '''
    Get information on a file (incl. zip-archives)
    '''
    convert_log.info('Called the info-cmd')
    click.echo(path.name)


@click.command('test', short_help='testcommand')
def test_cmd():
    '''
    Get information on a file (incl. zip-archives)
    '''
    convert_log.info('Called the info-cmd')
    convert_log.warning('convert_log.warning called from inside test_cmd')
    click.echo('click.echo: This is the info I got.')


convert_cli.add_command(convert_cmd)
convert_cli.add_command(info_cmd)
convert_cli.add_command(test_cmd)

# @click.command('extract', short_help='extract file from zip-archive')
# @click.argument('file', type=click.Path())
# @click.argument('archive', type=click.Path(exists=True))
# @click.option('--target-dir',
#               type=click.Path(writable=True, resolve_path=True),
#               help='specify a different directory to extract to')
# @click.option('--overwrite',
#               is_flag=True,
#               help='overwrite any existing file or directory')
# def extract_cmd(file, archive, target_dir, overwrite):
#     '''
#     Extracts a <file> from a <archive> (zip-formatted).
#     Returns the full path of the extracted file.
#     '''

#     # almanak.file.extract returns a path to the extracted file
#     out_path = extract(file_path=file,
#                        zip_path=archive,
#                        out_path=target_dir,
#                        overwrite=overwrite)
#     click.echo(out_path)


# @click.command('zip',
#                short_help='zip-compress file or directory')
# @click.option('--target-dir',
#               type=click.Path(writable=True, resolve_path=True),
#               help='specify a different directory to compress to')
# @click.option('--target-name',
#               type=click.STRING,
#               help='specify a new name for the zip-file.')
# @click.option('--overwrite',  # not sure overwrite works
#               is_flag=True,
#               help='overwrite any existing file')
# @click.argument('path',
#                 type=click.Path(exists=True, resolve_path=True))
# def zip_cmd(path, target_dir, target_name, overwrite):
#     """
#     Saves a zip-compressed copy of <PATH> in the same directory.
#     Returns the full path to the generated zip-archive.
#     """

#     # almanak.file.compress returns a path to the compressed archive
#     zip_path = compress(path,
#                         target=target_dir,
#                         name=target_name,
#                         overwrite=overwrite)
#     click.echo(zip_path)


# @click.command('unzip',
#                short_help='decompress a zip-archive')
# @click.option('--target-dir', 
#               type=click.Path(writable=True, resolve_path=True),
#               help='specify a different path to extract to')
# @click.option('--overwrite',
#               is_flag=True,
#               help='overwrite any existing files or directories')
# @click.argument('path',
#                 type=click.Path(exists=True, resolve_path=True))
# def unzip_cmd(path, target_dir, overwrite):
#     """
#     Decompresses a zipfile PATH into its parent-directory or TARGET.
#     Use OVERWRITE to overwrite any existing file or directory with same name.
#     """
#     # almanak.file.decompress returns a path to the decompressed file or dir
#     zip_path = decompress(path,
#                           target=target_dir,
#                           overwrite=overwrite)
#     click.echo(zip_path)
