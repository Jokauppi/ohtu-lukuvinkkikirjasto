
class VideoTip:
    def __init__(self, title: str, url: str, id_number: int = None, read: bool = False):
        self.title = title
        self.url = url
        self.id_number = id_number
        self.read = read

    @property
    def title(self):
        return self.__name

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Otsikon pitää olla merkkijono")
        if len(value) <= 0 or len(value) > 100:
            raise ValueError("Otsikon pituus pitää olla 1-100 merkkiä")
        self.__name = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        if not isinstance(value, str):
            raise TypeError("url pitää olla merkkijono")
        if len(value) < 5 or len(value) > 100:
            raise ValueError("url pituus pitää olla 5-100 merkkiä")
        self.__url = value

    def __str__(self):
        pad = 7

        return  f"{'Title:':{pad}} {self.title}\n" \
                f"{'Url:':{pad}} {self.url}\n"

    def __eq__(self, other: object) -> bool:

        if isinstance(other, VideoTip):
            return self.title == other.title\
                and self.url == other.url\


        return False
