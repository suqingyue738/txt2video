import re
from script.to_video import to_video

with open("./txt/凡人修仙传仙界篇.txt", 'rb') as f:
    txt = f.read().decode()
section_re = "第.*?章"
res = re.findall(section_re, txt)
res = list(res)
new_res = list(set(res))
new_res.sort(key=res.index)
# print(new_res)
start_list = []
for _ in new_res:
    start_ = txt.find(_)
    start_list.append(start_)
start_list = start_list[0::500]
print("len(start_list)", len(start_list))
print(len(txt))
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
# 1362
