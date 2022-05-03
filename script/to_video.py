import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")


def to_video(text: str = "video txt", path: str = "./test.mp3"):
    engine = pyttsx3.init()
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")
    # engine.say(text)
    engine.save_to_file(text, path)
    engine.runAndWait()


if __name__ == '__main__':
    to_video()
"""
普通话: 
com.apple.speech.synthesis.voice.ting-ting.premium
粤语 ：
com.apple.speech.synthesis.voice.ting-ting.premium
台湾女生普通话: 
com.apple.speech.synthesis.voice.mei-jia
"""
"""
for len_start in range(len(start_list)):
    if len_start == 0:
        txt_start = 0
    else:
        txt_start = start_list[len_start]
    if len_start == len(start_list) - 1:
        txt_end = -1
    else:
        txt_end = start_list[len_start + 1] + 1
    # print("txt_start", len_start)
    # print("txt_start", txt_start, txt_end)
    new_txt = txt[txt_start:txt_end]
    if len_start == 0:
        title = "前言"
    else:
        title = new_txt.split("\r")[0].replace(" ", "_")
    print(title)
    to_video(text=new_txt, path=f"./mp3/{title}.mp3")
    # break

"""
