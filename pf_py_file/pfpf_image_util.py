import os.path
from PIL import Image
from pf_py_file.pfpf_file_util import PFPFFileUtil


class ImageUtil:

    @staticmethod
    def make_thumb(image_path, dimension, prefix="thum", name=None, override=True):
        if not PFPFFileUtil.is_exist(image_path):
            return None
        file_original_name = PFPFFileUtil.get_file_name(image_path)
        file_extension = PFPFFileUtil.get_file_name(file_original_name)
        if name:
            name = name + file_extension
        else:
            name = prefix + "-" + file_original_name
        dir_name = os.path.dirname(image_path)
        thumb_path_with_name = os.path.join(dir_name, name)
        if override:
            PFPFFileUtil.delete_file(thumb_path_with_name)

        image = Image.open(image_path)
        image.thumbnail(dimension)
        image.save(thumb_path_with_name)
        return name
