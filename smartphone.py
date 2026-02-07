class Smartphone:
    def __init__(self, brand):
        self.brand = brand

    def make_call(self):
        print("Calling...")

class Camera(Smartphone):
    def take_photo(self):
        print(self.brand, "camera is taking a photo")

class MusicPlayer(Smartphone):
    def play_music(self):
        print(self.brand, "is playing music")


# Object Creation
phone1 = Camera("Samsung")
phone1.make_call()
phone1.take_photo()

phone2 = MusicPlayer("Apple")
phone2.make_call()
phone2.play_music()