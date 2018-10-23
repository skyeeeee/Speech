#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from lib.uuidhelper import get_uuid
from lib.filehelper import cleanfile
from conf.config import GeneralFilePath
from core.speechGenery import SeepchService
from core.recordWave import RocrdService


def servie():
    __uuidname = get_uuid()
    file_path = GeneralFilePath + __uuidname + ".wav"
    print "临时语音文件: %s" % file_path
    print "需要退出时，请讲:'关闭'"
    while True:
        RocrdService().my_record(file_path)

        __service = SeepchService()
        _tmp_res = __service.genery_result(file_path)
        __service.save_result(_tmp_res)
        __service.is_quit(_tmp_res)

        cleanfile(file_path)
