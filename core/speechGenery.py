# --*-- coding=utf-8 --*--

import sys
from lib.sdkClient import client
from lib.fileRead import get_file_content
from baisc import savefile


class SeepchBase(object):
    def _format_result(self, result):
        words_list = []
        res = result.get("result")
        for wordsline in res:
            words_list.append(wordsline + "\n")
        return words_list

    def _show(self, result):
        if isinstance(result, basestring):
            print result
        else:
            for words in result:
                print words

    def _quit(self, result):
        '''
        when 用户关闭时， 退出程序
        :param result:
        :return:
        '''
        res = result.get("result")
        for wordsline in res:
            if wordsline.startswith("关闭") or wordsline.endswith("关闭"):
                print "系统关闭..."
                sys.exit(0)

class SeepchService(SeepchBase):
    def genery_result(self, file_path, rate=8000, dev_pid=1536):
        '''
        genery voice file path
        :param file_path:
        :param rate:
        :param dev_pid:
        :return:
        '''

        print "正在分析语音..."
        _formate = file_path.split(".")[-1]
        _file_content = get_file_content(file_path)
        return client.asr(_file_content, _formate, rate, {'dev_pid': dev_pid, })

    def save_result(self, result, ishow=False):
        '''
        save the word to the file
        :param result:
        :return:
        '''

        _re_content = self._format_result(result)
        savefile(_re_content)

        if ishow:
            self._show(result)

        print "结果已保存至文件..."

    def is_quit(self, result):
        '''
        when need quit, sys will exit 0
        :param result:
        :return:
        '''

        self._quit(result)
