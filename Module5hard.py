import time
import sys
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


class  Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if len([u for u in self.users if u.nickname == nickname]) != 1:
            return
        else:
            tmp_user = [u for u in self.users if u.nickname == nickname][0]
            if tmp_user.password == hash(password):
                self.current_user=tmp_user


    def register(self, nickname, password, age):
        if nickname not in [user_arr.nickname for user_arr in self.users]:
            self.users.append(User(nickname, hash(password), age))
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} ужо существует")
        pass

    def log_out(self):
        self.current_user = None

    def add(self, *kwargs):
        for v in kwargs:
            if v.title not in [video_arr.title for video_arr in self.videos]:
                self.videos.append(v)

    def get_videos(self, find_word):
        return list(filter(lambda x: find_word.upper() in x, [video_arr.title.upper() for video_arr in self.videos]))

    def watch_video(self, name):
        if self.current_user == None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        video_name = self.get_videos(name)
        if len(video_name) == 1:
            tmp_video = [v for v in self.videos if v.title == name][0]
            if tmp_video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, давай до свидания")
            else:
                for i in range(1, tmp_video.duration+1):
                    print(i, end=' ')
                    sys.stdout.flush()
                    time.sleep(1)
                print("Конец видео")

# тестируем
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 201)
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



