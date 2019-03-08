import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def get_filepath_from_csv(csvfile: Path, filepath_col: str='filepath'):
    if csvfile.exists():
        with open(csvfile, 'r') as ifile:
            reader = csv.DictReader(ifile)
            if filepath_col not in reader.fieldnames:
                raise KeyError("No such column in the csv-file: " + filepath_col)
            for _d in reader:
                path_str = _d.get(filepath_col)
                try:
                    path = Path(path_str)
                    if not path.exists():
                        logger.error("File not found: " + path)
                except Exception as e:
                    logger.error(e.format_message())
                yield _d.get()
    else:
        raise FileNotFoundError


# def csv_input_file(filepath: Path, filepath_col: str='filepath', id_col: str='id'):
