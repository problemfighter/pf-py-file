import os
import shutil


class PFPFFileUtil:

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
