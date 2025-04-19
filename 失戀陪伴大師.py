import random
import time
import datetime
import webbrowser
from plyer import notification
from playsound import playsound
import threading

# ===============================
# ☁️ 安慰語句與擁抱 ASCII 藝術
# ===============================
comfort_quotes = [
    "你已經很棒了，不是每段感情都會走到最後，但你會走得更遠。",
    "失去愛的人不可怕，失去愛自己的心才值得難過。",
    "你值得更深的愛、更堅定的擁抱。",
    "哭過就好了，明天又是新的自己。",
    "這只是你人生旅程的一站，不是終點。",
]

ascii_hug = r"""
      (づ｡◕‿‿◕｡)づ 給你一個大大的擁抱！
"""

# ===============================
# 📢 語音、影片、鼓勵資源
# ===============================
motiv_audio = "voice.mp3"  # 可自訂為你自己的語音檔
warm_videos = [
    "https://youtu.be/5qap5aO4i9A",  # lofi 音樂
    "https://youtu.be/KxGRhd_iWuE",  # 自然風景
    "https://youtu.be/fbY3i7BrX_s",  # 擁抱動畫
]

# ===============================
# 📆 定時設定（秒）
# ===============================
REMINDER_INTERVAL = 60 * 60      # 每 1 小時提醒喝水/活動
MOTIVATION_INTERVAL = 60 * 60 * 3  # 每 3 小時播放鼓勵語音
FEELING_RECORD_HOUR = 10         # 每天早上 10 點提示紀錄心情

# ===============================
# ❤️ 安慰功能
# ===============================
def comfort_you():
    print("\n❤️ 來，先深呼吸一下...")
    time.sleep(1)
    print(random.choice(comfort_quotes))
    time.sleep(1)
    print(ascii_hug)
    time.sleep(1)
    print("🕯️ 你不是孤單一人，我在這裡陪你。")
    time.sleep(1)

# ===============================
# 🔔 喝水運動提醒
# ===============================
def remind_to_care():
    notification.notify(
        title="🌿 小提醒來囉！",
        message="記得喝水、伸展一下身體，你值得照顧自己 🧡",
        timeout=10
    )

# ===============================
# 📝 寫下今日一句心情
# ===============================
def record_daily_feeling():
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    feeling = input(f"\n📝 [{now}] 今天的心情一句話是？\n➡️ ")
    with open("daily_feelings.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {feeling}\n")
    print("✅ 已記錄，謝謝你願意照顧自己。")

# ===============================
# 🎧 播放語音或影片鼓勵
# ===============================
def play_motivation():
    try:
        print("\n🎧 播放鼓勵語音中...")
        playsound(motiv_audio)
    except:
        print("⚠️ 找不到語音檔，開啟暖心影片代替...")
        webbrowser.open(random.choice(warm_videos))

# ===============================
# 💡 主循環（背景運行）
# ===============================
def background_loop():
    last_motivation_time = time.time()

    while True:
        now = datetime.datetime.now()
        current_time = time.time()

        # 小提醒：喝水、伸展
        remind_to_care()

        # 心情日記：每天 10:00 提示一次
        if now.hour == FEELING_RECORD_HOUR and now.minute < 3:
            record_daily_feeling()

        # 每 3 小時鼓勵語音/影片
        if current_time - last_motivation_time >= MOTIVATION_INTERVAL:
            play_motivation()
            last_motivation_time = current_time

        time.sleep(REMINDER_INTERVAL)

# ===============================
# 🚀 主選單
# ===============================
def main():
    print("💖 歡迎使用《心靈照護 + 失戀急救助手》")
    print("1️⃣ 我現在心情很差，想被安慰")
    print("2️⃣ 啟動每日心靈照護提醒（背景執行）")
    print("0️⃣ 離開")

    choice = input("\n請選擇功能（輸入數字）：")

    if choice == "1":
        comfort_you()
        play_motivation()
    elif choice == "2":
        print("✨ 已啟動心靈照護提醒（可最小化程式）")
        thread = threading.Thread(target=background_loop)
        thread.daemon = True
        thread.start()

        try:
            while True:
                time.sleep(1)  # 保持主程式執行
        except KeyboardInterrupt:
            print("\n🫶 已結束照護提醒，記得好好休息喔！")
    elif choice == "0":
        print("👋 再見，記得你值得被溫柔對待。")
    else:
        print("⚠️ 無效選項，請重新啟動。")

if __name__ == '__main__':
    main()
