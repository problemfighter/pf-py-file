from pf_py_common.pf_exception import PFException
from pf_py_file.pfpf_file_util import PFPFFileUtil


class TextFileMan:

    @staticmethod
    def get_text_from_file(file_path):
        if not PFPFFileUtil.is_exist(file_path):
            raise PFException("Invalid File")
        with open(file_path, 'r', encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_text_to_file(file_path, text_content):
        PFPFFileUtil.delete_file(file_path)
        try:
            stream = open(file_path, 'w', encoding="utf-8")
            stream.write(text_content)
            stream.close()
            return True
        except Exception as e:
            return False

    @staticmethod
    def find_replace_text_content(file_path, find_replace_list_of_dict: list):
        text_content = TextFileMan.get_text_from_file(file_path)
        for find_replace_dict in find_replace_list_of_dict:
            if "find" in find_replace_dict and "replace" in find_replace_dict:
                text_content = text_content.replace(find_replace_dict["find"], find_replace_dict["replace"])

        if text_content:
            TextFileMan.write_text_to_file(file_path, text_content)
