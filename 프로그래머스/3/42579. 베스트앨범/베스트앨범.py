def solution(genres, plays):
    genre_play_dict = {}
    song_play_list = []
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_play_dict:
            genre_play_dict[genre] = play
        else:
            genre_play_dict[genre] += play
        song_play_list.append((genre, play, i))
    
    genre_play_sorted = sorted(genre_play_dict.items(), key=lambda x: x[1], reverse=True)
    
    answer = []
    for genre, _ in genre_play_sorted:
        temp_list = [song for song in song_play_list if song[0] == genre]
        temp_list.sort(key=lambda x: (-x[1], x[2]))
        answer.extend([song[2] for song in temp_list[:2]])
    
    return answer