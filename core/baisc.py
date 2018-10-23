# --*-- coding=utf-8 --*--

import io

from conf.config import SAVEFILE


def savefile(res):
    with io.open(SAVEFILE, mode='a+', encoding='utf-8') as savefile:
        if isinstance(res, basestring):
            savefile.write(res.encode('utf-8') + u"\n")
            savefile.flush()
        elif isinstance(res, list):
            savefile.writelines(res)
            savefile.write(u"\n")
            savefile.flush()
        else:
            savefile.write(bytes(res.encode('utf-8')))
            savefile.flush()


if __name__ == '__main__':
    savefile(['1', '2', '3'])
    savefile(["seiee"])
