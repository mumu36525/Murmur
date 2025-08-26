import random
import re

class SimpleChatBot:
    def __init__(self):
        self.responses = {
            r".*(你好|嗨|hello|hi).*": [
                "你好！我是你的AI助手。",
                "嗨！很高兴与你交流。",
                "你好啊！今天有什么可以帮你的吗？"
            ],
            r".*(叫什么名字|你是谁|你叫啥).*": [
                "我是星期二，很高兴认识您！",
            ],
            r".*(天气|气温|下雨|晴天).*": [
                "抱歉，我目前无法获取实时天气信息。",
                "要查询天气，你可以使用专业的天气应用或网站。"
            ],
            r".*(谢谢|感谢|thank you).*": [
                "不客气！很高兴能帮到你。",
                "随时为你效劳！",
                "这是我应该做的。"
            ],
            r".*(再见|拜拜|end|stop|exit).*": [
                "再见！期待下次与你交流。",
                "好的，有需要随时找我哦！",
                "再见，祝你今天愉快！"
            ]
        }
        
        self.default_responses = [
            "很有趣的观点，能告诉我更多吗？",
            "我不太明白，你能换种方式说吗？",
            "这个话题很有意思，但我还需要学习更多。",
            "我正在学习如何更好地与人交流，你能多告诉我一些吗？"
        ]
    
    def respond(self, user_input):
        user_input = user_input.lower().strip()
        
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        return random.choice(self.default_responses)
    
    def chat(self):
        print("聊天机器人已启动! 输入'退出'或'再见'来结束对话。")
        print("=" * 50)
        
        while True:
            user_input = input("你: ")
            if user_input.lower() in ['退出', '再见', 'end', 'exit', 'stop']:
                print("机器人: " + random.choice(self.responses[r".*(再见|拜拜|end|stop|exit).*"]))
                break
            
            response = self.respond(user_input)
            print("机器人: " + response)

# 运行聊天机器人
if __name__ == "__main__":
    bot = SimpleChatBot()
    bot.chat()