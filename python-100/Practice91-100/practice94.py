import random

lunch = ["김치찌개", "짜장면", "김밥", "햄버거", "순대국밥", "한식뷔페", "샐러드"]

def lunch_reco(lunch):
    menu = random.choice(lunch)
    print(f"추천메뉴는!! {menu}입니다.")

lunch_reco(lunch)
