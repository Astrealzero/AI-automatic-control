# import sounddevice as sd
#
# x = sd.query_devices()
# print(x)


# --- 调用 GPT-SoVITS 语音合成 ---
import io
import time

import pyttsx3
import requests

# --- GPT-SoVITS API 配置 ---
from pydub import AudioSegment
from pydub.playback import play

# # 设置 FFmpeg 路径（如果未添加到环境变量）
# AudioSegment.converter = r"../ffmpeg/bin/ffmpeg.exe"  # 替换为你的 FFmpeg 路径
# AudioSegment.ffprobe = r"../ffmpeg/bin/ffprobe.exe"  # 替换为你的 FFprobe 路径

# --- 用pyttsx3进行语音合成 ---
# 初始化语音合成引擎
engine = pyttsx3.init()
# 设置语音合成属性（可选）
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 选择语音（0 通常是默认语音）
engine.setProperty('rate', 150)  # 设置语速
engine.setProperty('volume', 1.0)  # 设置音量（0.0 到 1.0）

GPT_SOVITS_API_URL = "https://gsv.ai-lab.top/infer_single"  # 假设的 API 地址
ACCESS_TOKEN = "d28a6b5e192a70a52a0ce8706ed7b352"  # 根据文档生成 Token


def speak(TexT):
    """调用 GPT-SoVITS API 合成语音并播放"""
    if not TexT:
        return

    # # 构造 API 请求头（根据实际文档调整）
    # headers = {
    #     "Authorization": "application/json",
    #     "Content-Type": "application/json"
    # }

    # 构造请求体（根据实际文档调整）
    data = {
        "access_token": f"{ACCESS_TOKEN}",
        "model_name": "星穹铁道",
        "speaker_name": "流萤",
        "prompt_text_lang": "中文",
        "emotion": "中立_neutral",
        "text": TexT,
        "text_lang": "中文",
    }

    try:
        # 发送 API 请求
        # response = requests.post(GPT_SOVITS_API_URL, headers=headers, json=data)
        response = requests.post(GPT_SOVITS_API_URL, json=data)
        if response.status_code == 200:
            audio_url = response.json()["audio_url"]
            # 假设 API 返回的是音频二进制数据（如 WAV 格式）
            # response2 = requests.post(audio_url)
            # if response2.status_code == 200:
            #     print(response2)
            response_audio = requests.get(audio_url, timeout=30)
            audio_data = response_audio.content
            # audio_data = response.content
            with open("voice/" + TexT + ".wav", "wb") as f:
                f.write(audio_data)
            # 使用 pydub 播放音频
            audio = AudioSegment.from_file(io.BytesIO(audio_data), format="wav")
            play(audio)
            print(f"AI助手: {TexT}")
        else:
            print(f"语音合成失败，错误码: {response.status_code}")

    except Exception as e:
        print(f"API 调用异常: {e}")


# 测试语音识别
if __name__ == "__main__":
    speak("今天是星期六")
