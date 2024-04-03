import logging
import os
from django.utils.safestring import mark_safe

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TextFilesMerger:
    def merge(self, files, rel_paths=None, no_duplicates=False):
        logger.info("Starting file merge process")
        merged_content = ""
        separator = "\n------------------###------------------\n"
        terminator = "\n###---------#####END######---------###\n\n"

        if not files:
            logger.warning("No files provided for merging")
            return merged_content

        for file, rel_path in zip(files, rel_paths or []):
            file_path = rel_path  # This now includes the directory structure due to the changes on the client side
            bold_filename = f'<b>{file_path}</b>'  # Wrap the file path with <b> tags to make it bold
            logger.info(f"Processing file: {bold_filename}")
            try:
                content = file.read().decode('utf-8')
                file.seek(0)  # Reset file pointer after reading
                merged_content += separator + "### " + mark_safe(bold_filename) + " ###\n\n" + content + terminator  # Include file path in merged content, marking it as safe
            except Exception as e:
                logger.error(f"Error processing file {bold_filename}: {e}")

        logger.info("File merge process completed")
        return merged_content


