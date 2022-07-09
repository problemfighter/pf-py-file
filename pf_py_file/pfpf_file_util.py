import os
import shutil
from pathlib import Path


class FileUtil:

    @staticmethod
    def list_directory(path: str, is_file_only: bool = False, is_dir_only: bool = False, filter_extension: list = None):
        if not FileUtil.is_exist(path):
            return []

        name_list = []
        for name in os.listdir(path):
            name_path = os.path.join(path, name)
            if is_file_only and FileUtil.is_it_file(name_path):
                if filter_extension:
                    if FileUtil.get_file_extension(name) in filter_extension:
                        name_list.append(name)
                else:
                    name_list.append(name)
            elif is_dir_only and FileUtil.is_it_dir(name_path):
                name_list.append(name)
            else:
                name_list.append(name)
        return name_list

    @staticmethod
    def is_exist(path):
        return os.path.exists(path)

    @staticmethod
    def is_it_file(path):
        return os.path.isfile(path)

    @staticmethod
    def is_it_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def get_file_extension(filename):
        if '.' in filename:
            return filename.rsplit('.', 1)[1].lower()

    @staticmethod
    def filename_only(name_with_extension):
        return Path(name_with_extension).stem


class PFPFFileUtil:

    @staticmethod
    def copy(source, destination, ignore=None):
        if os.path.isdir(source):
            return shutil.copytree(source, destination, ignore)
        else:
            return shutil.copy(source, destination)

    @staticmethod
    def create_directories(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def remove_file_if_exist(path):
        if os.path.exists(path):
            os.remove(path)

    @staticmethod
    def join_path(*args):
        return os.path.join(*args)

    @staticmethod
    def is_exist(path):
        return FileUtil.is_exist(path)

    @staticmethod
    def delete(path):
        if PFPFFileUtil.is_exist(path):
            if os.path.isfile(path):
                PFPFFileUtil.delete_file(path)
            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)

    @staticmethod
    def rename(source, destination):
        os.rename(source, destination)

    @staticmethod
    def delete_file(path):
        if PFPFFileUtil.is_exist(path):
            os.remove(path)

    @staticmethod
    def get_file_name(path):
        return os.path.basename(path)

    @staticmethod
    def get_file_extension(file_name):
        split = os.path.splitext(file_name)
        if len(split) < 2:
            return None
        return split[1]

    @staticmethod
    def file_size_into_byte(path):
        if PFPFFileUtil.is_exist(path):
            return os.stat(path).st_size
        return None

    @staticmethod
    def human_readable_file_size(size):
        B = float(size)
        KB = float(1024)
        MB = float(KB ** 2)
        GB = float(KB ** 3)
        TB = float(KB ** 4)

        if B < KB:
            return '{0} {1}'.format(B, 'B' if 0 == B > 1 else 'B')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B / KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B / MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B / GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B / TB)
