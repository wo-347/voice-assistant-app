# android_main.py - Android专用主程序
import os
import sys
import time
from datetime import datetime

try:
    from jnius import autoclass
    from android import api_version
    ANDROID_AVAILABLE = True
except ImportError:
    ANDROID_AVAILABLE = False

# 添加路径
sys.path.append(os.path.dirname(__file__))

from config import Config
from core.command_system import CommandSystem

if ANDROID_AVAILABLE:
    from utils.android_audio import AndroidAudio
else:
    from utils.audio_simulator import AudioSimulator as AndroidAudio

class AndroidVoiceAssistant:
    def __init__(self):
        print("=== Android语音助手启动 ===")
        print(f"📱 运行环境: {'Android' if ANDROID_AVAILABLE else '模拟'}")
        
        self.config = Config()
        self.audio = AndroidAudio()
        self.command_system = CommandSystem()
        
        # Android特定设置
        if ANDROID_AVAILABLE:
            self._setup_android()
    
    def _setup_android(self):
        """Android环境设置"""
        try:
            # 获取Android上下文
            self.python_activity = autoclass('org.kivy.android.PythonActivity')
            self.activity = self.python_activity.mActivity
            
            # 设置常亮（可选）
            self.activity.getWindow().addFlags(0x00000080)  # FLAG_KEEP_SCREEN_ON
            
            print("✅ Android环境设置完成")
            
        except Exception as e:
            print(f"❌ Android设置失败: {e}")
    
    def run(self):
        """运行主循环"""
        print("\n" + "="*50)
        print("🎉 Android语音助手就绪！")
        print("="*50)
        print("模式: 文本输入")
        print("提示: 选择指令编号")
        print("="*50)
        
        try:
            while True:
                user_input = self.audio.simulate_listen()
                
                if user_input and user_input.lower() == 'exit':
                    print("收到退出指令...")
                    break
                
                if user_input and user_input.strip():
                    response = self.command_system.process_command(user_input, self.audio)
                    self.audio.simulate_speak(response)
                    
        except KeyboardInterrupt:
            print("\n🛑 用户中断程序")
        except Exception as e:
            print(f"❌ 程序错误: {e}")
        finally:
            print("\n👋 语音助手已关闭")

if __name__ == "__main__":
    assistant = AndroidVoiceAssistant()
    assistant.run()