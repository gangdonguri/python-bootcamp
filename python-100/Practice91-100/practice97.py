last_names = {
    "김": "金",
    "이": "李",
    "박": "朴",
    "정": "政",
    "조": "調",
    "강": "姜",
    "최": "崔",
    "윤": "尹",
    "장": "長",
    "임": "任"
}

def Search(last_name):
    if last_name in last_names:
        print(last_names[last_name])
    else:
        print("찾을 수 없는 성씨 입니다.")

Search("김")
Search("마이클")