# Задание "Свой YouTube"

import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, str):
            return self.nickname == other
        return NotImplemented

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, str):
            return item.lower() in self.title.lower()
        return NotImplemented

    def show(self):
        for self.time_now in range(self.time_now + 1, self.duration + 1):
            print(self.time_now, end=" ")
            time.sleep(1)
        self.time_now = 0
        print("Конец видео")


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            hashed = hash(password)
            if user.nickname == nickname and user.password == hashed:
                self.current_user = user
                break

    def register(self, nickname, password, age):
        if not nickname in self.users:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if not video in self.videos:
                self.videos.append(video)

    def get_videos(self, find_str):
        result = []
        for video in self.videos:
            if find_str in video:
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if video.title == title:
                    if video.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
                    video.show()
                    break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
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
