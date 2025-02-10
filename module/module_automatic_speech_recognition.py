import io
import json
import os

import pyttsx3
import requests
import sounddevice as sd
from pydub import AudioSegment
from pydub.playback import play
from vosk import Model, KaldiRecognizer


class automatic:
    def __init__(self):

        # # 设置 FFmpeg 路径（如果未添加到环境变量）
        # AudioSegment.converter = r"../ffmpeg/bin/ffmpeg.exe"  # 替换为你的 FFmpeg 路径
        # AudioSegment.ffprobe = r"../ffmpeg/bin/ffprobe.exe"  # 替换为你的 FFprobe 路径

        # 下载中文模型（首次使用需要下载）
        # 模型下载地址：https://alphacephei.com/vosk/models
        # 将模型解压到当前目录下的 "model" 文件夹中
        if not os.path.exists("model"):
            print("请下载并解压Vosk中文模型到 'model' 文件夹")
            exit(1)

        # 初始化Vosk模型
        self.model = Model("model")
        self.samplerate = 16000
        self.device = 1  # 麦克风设备ID，可以通过 sd.query_devices() 查看

        # --- 用pyttsx3进行语音合成 ---
        # 初始化语音合成引擎
        self.engine = pyttsx3.init()
        # 设置语音合成属性（可选）
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)  # 选择语音（0 通常是默认语音）
        self.engine.setProperty('rate', 150)  # 设置语速
        self.engine.setProperty('volume', 1.0)  # 设置音量（0.0 到 1.0）

        # --- GPT-SoVITS API 配置 ---
        self.GPT_SOVITS_API_URL = "https://gsv.ai-lab.top/infer_single"  # 假设的 API 地址
        API_KEY = "YOUR_API_KEY"
        API_SECRET = "YOUR_API_SECRET"
        self.ACCESS_TOKEN = "d28a6b5e192a70a52a0ce8706ed7b352"  # 根据文档生成 Token

    def listen(self):
        print("请说话...")
        rec = KaldiRecognizer(self.model, self.samplerate)
        with sd.InputStream(samplerate=self.samplerate, channels=1, dtype='int16', device=self.device) as stream:
            while True:
                data, _ = stream.read(4096)
                if len(data) == 0:
                    break

                # 将 numpy.ndarray 转换为 bytes
                data_bytes = data.tobytes()

                if rec.AcceptWaveform(data_bytes):
                    result = rec.Result()
                    text_text = json.loads(result)["text"]
                    print(f"你说: {text_text}")
                    return text_text
        return None

    # 播放准备好的文件
    def speak3(self, file_path):
        audio = AudioSegment.from_file("..\\voice\\" + file_path, format="wav")
        play(audio)

    # # --- 调用 pyttsx3 语音合成 ---
    def speak2(self, text_text):
        # engine = pyttsx3.init()
        self.engine.say(text_text)
        self.engine.runAndWait()

    # --- 调用 GPT-SoVITS 语音合成 ---
    def speak(self, text_text):
        """调用 GPT-SoVITS API 合成语音并播放"""
        if not text_text:
            return

        # 构造 API 请求头（根据实际文档调整）
        # headers = {
        #     "Authorization": "application/json",
        #     "Content-Type": "application/json"
        # }

        # 构造请求体（根据实际文档调整）
        data = {
            "access_token": f"{self.ACCESS_TOKEN}",
            "model_name": "星穹铁道",
            "speaker_name": "流萤",
            "prompt_text_lang": "中文",
            "emotion": "中立_neutral",
            "text": text_text,
            "text_lang": "中文",
        }

        try:
            # 发送 API 请求
            # response = requests.post(GPT_SOVITS_API_URL, headers=headers, json=data)
            response = requests.post(self.GPT_SOVITS_API_URL, json=data)
            if response.status_code == 200:
                audio_url = response.json()["audio_url"]
                # 假设 API 返回的是音频二进制数据（如 WAV 格式）
                # response2 = requests.post(audio_url)
                # if response2.status_code == 200:
                #     print(response2)
                response_audio = requests.get(audio_url, timeout=30)
                audio_data = response_audio.content
                # 保存语音
                # with open("voice/" + text_text + ".wav", "wb") as f:
                #     f.write(audio_data)
                # 使用 pydub 播放音频
                audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
                play(audio)
                print(f"AI助手: {text_text}")
            else:
                print(f"语音合成失败，错误码: {response.status_code}")

        except Exception as e:
            print(f"API 调用异常: {e}")


# 测试语音识别
if __name__ == "__main__":
    automatic = automatic()
    # text = automatic.listen()
    # if text:
    #     print(f"识别结果: {text}")
    # else:
    #     print("未识别到语音")
    automatic.speak("今天星期六")
