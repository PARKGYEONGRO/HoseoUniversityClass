import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(URL, headers=headers, timeout=20).text
soup = BeautifulSoup(html, "lxml")

rows = []

# Billboard 현재 페이지 구조 기준
items = soup.select("div.o-chart-results-list-row-container")

for item in items:
    rank = item.select_one("span.c-label")
    title = item.select_one("h3")
    artist = title.find_next("span") if title else None

    labels = [x.get_text(strip=True) for x in item.select("span.c-label")]
    nums = [x for x in labels if x.isdigit() or x == "-"]

    rows.append({
        "rank": rank.get_text(strip=True) if rank else None,
        "title": title.get_text(strip=True) if title else None,
        "artist": artist.get_text(strip=True) if artist else None,
        "last_week": nums[1] if len(nums) > 1 else None,
        "peak": nums[2] if len(nums) > 2 else None,
        "weeks_on_chart": nums[3] if len(nums) > 3 else None,
    })

df = pd.DataFrame(rows)
df.to_csv("billboard_hot100.csv", index=False, encoding="utf-8-sig")

print(df.head())
print(f"Saved {len(df)} rows")