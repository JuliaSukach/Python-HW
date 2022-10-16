# Создать свой класс данных
# Добавить в класс статикметод
# Добавить в класс классметод

class KendrickLamarSong:
    count = 0
    grammy_award_2022 = False

    def __init__(self, song_name: str, album: str, coolness_lvl: int):
        self.song_name = song_name
        self.album = album
        self.coolness_lvl = coolness_lvl

        KendrickLamarSong.count += 1

    @staticmethod
    def rated_songs():
        return KendrickLamarSong.count

    @classmethod
    def change_grammy_status(cls):
        cls.grammy_award_2022 = not cls.grammy_award_2022


first_song = KendrickLamarSong('die hard', 'MMATBS', 5)
assert KendrickLamarSong.rated_songs() == 1

second_song = KendrickLamarSong('love', 'DAMN', 6)
assert KendrickLamarSong.rated_songs() == 2

KendrickLamarSong.change_grammy_status()
assert KendrickLamarSong.grammy_award_2022 == True

