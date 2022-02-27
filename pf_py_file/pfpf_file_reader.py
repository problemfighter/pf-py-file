from pf_py_common.pf_exception import PFException
from pf_py_file.pfpf_file_util import PFPFFileUtil


class PFPFFileReader:

    def get_file_content(self, file_path):
        if not PFPFFileUtil.is_exist(file_path):
            raise PFException("Invalid File")
        with open(file_path, 'r') as file:
            return file.read()
