"""
Some convenient tools for dataset parsing and construction.
"""
import csv
import os


class FileListGenerator:
    """Generate a list of specific files in directory."""

    def __init__(self):
        """Initialization"""
        # The list to be populated.
        self.file_list = []

    def generate_list(self, target_dir, format_list=["jpg", "png"]):
        """Generate the file list of format_list in target_dir

        Args:
            target_dir: the directory in which files will be listed.
            format_list: a list of file extention names.

        Returns:
            a list of file urls.

        """
        self.file_list.clear()
        # Walk through directories and list all files.
        for file_path, _, current_files in os.walk(target_dir, followlinks=False):
            for filename in current_files:
                # First make sure the file is exactly of the format we need.
                # Then process the file.
                if filename.split('.')[-1] in format_list:
                    # Get file url.
                    file_url = os.path.join(file_path, filename)
                    self.file_list.append(file_url)

        return self.file_list

    def save_file_path_list(self, list_name='list.csv'):
        """Save the list in csv format.

        Args:
            list_name: the file name to be written.

        """
        with open(list_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['file_url'])

            # Write the header.
            writer.writeheader()

            # Write all the rows.
            for each_record in self.file_list:
                writer.writerow({'file_url': each_record})

    def save_basename_list(self, list_name='basename.csv'):
        basename_list = []
        for each_record in self.file_list:
            basename = os.path.basename(each_record)
            print(basename)
            basename_list.append(basename.split(".")[-2])

        with open(list_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['file_basename'])

            # Write the header.
            writer.writeheader()

            # Write all the rows.
            for each_record in basename_list:
                writer.writerow({'file_basename': each_record})
