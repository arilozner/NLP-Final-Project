from lyricsgenius import Genius

lyric_dict = {}
genius = Genius('mJE15wCPoy8WL51ozZGFMZgm_HWzcZmV6distweIjCT7ut3UA2kMfey3aTpujMfu')
chrts = genius.charts(chart_genre='rock',per_page=50) 
genre_list = ['rock','pop','rap']

for genre in genre_list:
  lyric_list = []
  for page in range(1,10):
      chrts = genius.charts(chart_genre=genre,page=page,per_page=50)
      for i in range(0, len(chrts['chart_items'])):    
          songid = chrts['chart_items'][i]['item']['id']
          lyrics = genius.lyrics(song_id=songid)
          lyric_list.append(lyrics)
          lyric_dict[genre] = lyric_list
