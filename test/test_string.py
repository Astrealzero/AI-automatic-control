# import os
#
# filenames = []
#
#
# def fileopen(file):
#     for filename in os.listdir(file):
#         if os.path.isfile(os.path.join(file, filename)):
#             filenames.append(filename)
#     return filenames
#
#
# filenames2 = fileopen("../app_folder")
# print(filenames2)
# string_data = "打开百度浏览器"
# if "打开" in string_data and "浏览器" in string_data:
#     os.startfile("..\\app_folder\\"+"浏览器"+".lnk")
# else:
#     print(False)
import io

from pydub import AudioSegment
from pydub.playback import play

# audio = AudioSegment.from_file("./voice/正在打开浏览器.wav", format="wav")
# play(audio)
data = "刘英 同学 打开 了 气"
if "了气" in data:
    print(True)
