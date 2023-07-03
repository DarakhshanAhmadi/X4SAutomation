import logging
import os
import shutil
import time

logger = logging.getLogger(__name__)


def delete_files_older_than(directory, days=1):
    logger.info(f'Deleting files in [{directory}] older than [{days}] days')
    for filename in os.listdir(directory):
        if os.path.getmtime(os.path.join(directory, filename)) < time.time() - days * 86400:
            if os.path.isfile(os.path.join(directory, filename)):
                os.remove(os.path.join(directory, filename))
                logger.info(f"Successfully deleted [{filename}] in directory [{directory}]")


def delete_directory_older_than(directory, days=1):
    logger.info(f'Deleting sub folders in directory [{directory}] older than [{days}] days')
    sub_folders = [f.path for f in os.scandir(directory) if f.is_dir()]
    for folder in sub_folders:
        if os.path.getmtime(folder) < time.time() - days * 86400:
            shutil.rmtree(folder)
            logger.info(f"Successfully deleted directory [{folder}]")
