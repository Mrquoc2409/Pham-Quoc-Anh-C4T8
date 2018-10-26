from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch5'
}

ydl = YoutubeDL(options)
search_result = ydl.extract_info('Crush', False)
# print(search_result)
import json
with open('search_file.json', 'w') as outfile:
    json.dump(search_result, outfile)
listMusic = search_result['entries' ]

print(listMusic[0])