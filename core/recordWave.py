# --*-- coding=utf-8 --*--

import wave
from pyaudio import PyAudio, paInt16

class RocrdService(object):
    def __init__(self, framerate=8000, num_samples=2000, channels=1, sampwidth=2, time=30):
        self.framerate = framerate
        self.NUM_SAMPLES = num_samples
        self.channels = channels
        self.sampwidth = sampwidth
        self.TIME = time

    def save_wave_file(self, filename, data):
        '''

        :param filename:
        :param data:
        :return:
        '''

        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes(b"".join(data))
        wf.close()

    def my_record(self, filename):
        '''
        :return:
        '''

        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1,
                         rate=self.framerate, input=True,
                         frames_per_buffer=self.NUM_SAMPLES)
        my_buf = []
        count = 0
        print "录音中，时长为:%s (s), 请开始讲话..." % self.TIME
        while count < self.TIME:
            string_audio_data = stream.read(self.NUM_SAMPLES)
            my_buf.append(string_audio_data)
            count += 1
        print "录音结束..."
        self.save_wave_file(filename, my_buf)
        stream.close()


