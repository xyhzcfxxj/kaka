from asr import baidu_asr
from tts import baidu_tts
from init import case,record
import pyaudio
import wave
import os
import logging
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 常用变量
CASEPATH = './init/testcase.xlsx'
AUDIOPATH = './audio'


# 唤醒

CHUNK = 1024
FILENAME = AUDIOPATH+'/小荷小荷.mp3'
INPUT = AUDIOPATH+'/现在几点了.mp3'
OUTPUT = './audio/output/小荷1.wav'

def play(filename = FILENAME):
    CHUNK = 1024
    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == '__main__' :
    # 识别excel
    # testCaseList = case.readexcel(CASEPATH)
    # testCaseList = []
    # testCaseList.append("小荷小荷")
    # # testCaseList.append("现在几点了")
    # #
    # # # 生成语音文件
    # result = baidu_tts.text2audio(testCaseList)


    # os.system("ffplay  %s -nodisp -autoexit" % (FILENAME))
    # time.sleep(1)
    # os.system("ffplay  %s -nodisp -autoexit" % (INPUT))
    # # #
    # record.record()

    baidu_asr.audio2text(OUTPUT)
    print(1)

