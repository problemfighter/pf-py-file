import os
import zipfile


class Archive:

    @staticmethod
    def create_zip(source, zip_file_path):
        zip_file = zipfile.ZipFile(zip_file_path, "w")
        source_abspath = os.path.abspath(source)
        for dirname, sub_dirs, files in os.walk(source):
            for filename in files:
                abs_name = os.path.abspath(os.path.join(dirname, filename))
                arcname = abs_name[len(source_abspath) + 1:]
                zip_file.write(abs_name, arcname)
        zip_file.close()
