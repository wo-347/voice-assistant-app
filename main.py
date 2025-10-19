# main.py - Kivy应用入口
import os
import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

class VoiceAssistantApp(App):
    def build(self):
        # 显示启动界面
        self.label = Label(
            text='语音助手启动中...\n请稍候',
            font_size='20sp',
            halign='center'
        )
        return self.label

    def on_start(self):
        # 延迟启动语音助手，避免阻塞UI
        Clock.schedule_once(self.start_assistant, 1)

    def start_assistant(self, dt):
        try:
            # 导入并启动语音助手
            from android_main import AndroidVoiceAssistant
            self.assistant = AndroidVoiceAssistant()

            # 更新界面状态
            self.label.text = '语音助手运行中...\n请查看终端输出'

            # 在后台线程中运行
            import threading
            self.thread = threading.Thread(target=self.assistant.run)
            self.thread.daemon = True
            self.thread.start()

        except Exception as e:
            self.label.text = f'启动失败: {str(e)}'

if __name__ == '__main__':
    VoiceAssistantApp().run()