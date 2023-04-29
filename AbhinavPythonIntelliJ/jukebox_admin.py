from nested_data import albums
SONG_ALBUMS_INDEX=3
SONG_LIST_INDEX=1
while True:
    print("please choose below from album title track (choose valid number)")
    for index,(title,artist,year,songs) in enumerate(albums):
        print(f"{index+1}: {title}")
    
    choice=int(input())
    if 1 <= choice <= len(albums):
        songs_list=albums[choice -1][SONG_ALBUMS_INDEX]
        # print(songs_list)
    else:
        break
    print("Please choose songs from the list:")
    for index,(track_number,song) in enumerate(songs_list):
        print(f"{index+1}: {song}")
    song_choice=int(input())
    if 1 <= song_choice <= len(songs_list):
        song=songs_list[song_choice - 1][SONG_LIST_INDEX]
        # print(song)
    # else:
    #     break
        print(f"Playing {song}")
    print("="*40)

    # for index,value in enumerate(albums):
    #     title,artist,year,songs=value
    #     print(index,title,artist,year,songs)
    # break