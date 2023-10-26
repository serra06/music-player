class MusicPlayer():
    def __init__(self, song_name, singer):
        self.song_name = song_name
        self.singer = singer

    # metot örneği
    def sarki_ismi_degistir(self, value):
        self.song_name = value

song1 = MusicPlayer("c", "singer_abc")
print(song1.song_name, "şarkısının sanatçısı ", song1.singer)

song1.sarki_ismi_degistir("def")
print("değişim sonrası şarkı ismi")

print(song1.song_name, "şarkısının sanatçısı ", song1.singer)

