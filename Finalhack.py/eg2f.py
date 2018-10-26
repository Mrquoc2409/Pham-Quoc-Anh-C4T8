from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
listEmpty = []
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    search_result = ydl.extract_info('https://www.youtube.com/watch?v=n6BwAWiHcSg&t=182s ',False)
    listEmpty.append(search_result)
print(listEmpty)