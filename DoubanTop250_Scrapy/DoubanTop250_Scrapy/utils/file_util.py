import os
import csv


class FileHandle(object):

    @staticmethod
    def read_csv(file_path, encode="UTF-8"):
        """读取csv文件

        包含字符集的范围是： GB18030 > GBK > GB2312

        先使用UTF-8编码打开文件，如果失败，再使用GB18030编码打开文件
        """

        assert os.path.exists(file_path), '文件不存在'

        file_content = []

        def ergodic_row_data():

            file_content.clear()

            worksheet = csv.reader(workbook)

            for row in worksheet:

                row_content = [v.strip() for v in row]

                blank_line = [value for value in row_content if value]

                if not blank_line:
                    continue

                file_content.append(row_content)

            workbook.close()

            return

        try:
            workbook = open(file=file_path, mode='r', encoding='UTF-8')
            ergodic_row_data()
        except:

            try:
                workbook = open(file=file_path, mode='r', encoding='GB18030')
                ergodic_row_data()

            except UnicodeDecodeError as e:
                assert False, '文件编码有误，无法解析文件'
            except Exception:
                assert False, '文件无法处理'

        return file_content