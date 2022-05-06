import os
import shutil


class PFPFFileUtil:

    @staticmethod
    def copy(source, destination):
        if os.path.isdir(source):
            return shutil.copytree(source, destination)
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
        return os.path.exists(path)

    @staticmethod
    def delete(path):
        if PFPFFileUtil.is_exist(path):
            shutil.rmtree(path)

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
