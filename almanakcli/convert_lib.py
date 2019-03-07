from pathlib import Path

# Third party
import cv2 as cv
# from cv2 import imread, imwrite, resize, IMWRITE_JPEG_QUALITY, INTER_AREA


ALLOWED_OUTPUT_EXTENSIONS = ['.png', '.gif', '.jpg', '.jpeg', '.jp2', '.tiff', '.tif']
JPEG_QUALITY = 95

def convert_image(input_file: Path, output_file: Path, max_width: int=None, max_height: int=None, quality:int=JPEG_QUALITY):
    # tests
    if not input_file.is_file():
        raise IOError("input_file is not a valid filepath: " + str(input_file))
    if not cv.haveImageReader(str(input_file)):
        raise IOError("Unable to convert files with extension: " + input_file.suffix)
    if not output_file.is_file():
        raise IOError("output_file is not a valid filepath: " + str(output_file))
    if output_file.suffix not in ALLOWED_OUTPUT_EXTENSIONS:
        raise IOError("Unable to save to a fileformat with extension: " + output_file.suffix)

    try:
        cv_img = _read_image(str(input_file))
        if max_height or max_width:
            cv_img = _resize_image(cv_img, max_height=max_height, max_width=max_width)
        final = _save_image(str(output_file), cv_img, quality)
        return output_file
    except Exception as e:
        raise Exception(e)


def _resize_image(cv_image, max_height=None, max_width=None):
    height, width = cv_image.shape[:2]
    scale = 1

    # shrink if img-dimentions are bigger than required
    if max_height and max_height/float(height) < scale:
        scale = max_height / float(height)

    if max_width and max_width/float(width) < scale:
        scale = max_width / float(width)

    # https://docs.opencv.org/3.0-last-rst/modules/imgproc/doc/geometric_transformations.html?highlight=resize#cv2.resize
    return cv.resize(cv_image, fx=scale, fy=scale, interpolation=cv.INTER_AREA)


def _read_image(filepath):
    return cv.imread(filepath)


def _save_image(filename, cv_image, jpg_quality=95):
    return cv.imwrite(filename, cv_image, [cv.IMWRITE_JPEG_QUALITY, jpg_quality])
