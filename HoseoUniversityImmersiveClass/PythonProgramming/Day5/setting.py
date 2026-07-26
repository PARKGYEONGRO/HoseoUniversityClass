import json
settings = {'volume':70, 'theme':'dark', 'language':'ko'}

with open('settings.json', 'w', encoding='utf-8') as f:
    json.dump(settings, f, ensure_ascii = False, indent=4)

with open('settings.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(data)