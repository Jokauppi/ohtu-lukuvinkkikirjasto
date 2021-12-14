
class VideoTip:
    # pylint: disable-duplicate-code

    def __init__(self, title: str, url: str,  comment: str = '', \
            id_number: int = None, read: bool = False, tags: str = ""):
        self.title = title
        self.url = url
        self.id_number = id_number
        self.read = read
        self.comment = comment
        # Sisäiset muuttujat joilla ei tarkoituksella ole setteriä.
        # Käytä ohjelmassa add_tag tai remove_tag -metodeja.
        self.__tags = tags # string databaselle
        self.__taglist = []
        if self.__tags != "":
            self.__taglist = tags.split(",") #ohjelmistokäyttöön

    @property
    def title(self):
        return self.__name

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        if not isinstance(value, str):
            raise TypeError("Kommentin pitää olla merkkijono")
        self.__comment = value

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

    @property
    def tags(self):
        return self.__tags

    @property
    def taglist(self):
        return self.__taglist

    def add_tag(self, value):
        if str(value).lower() not in self.taglist:
            self.__taglist.append(str(value).lower())
            if len(self.__taglist) == 1:
                self.__tags = self.__taglist[0]
            else:
                self.__tags = ",".join(self.taglist)

    def remove_tag(self, value):
        if str(value).lower() in self.taglist:
            self.__taglist.remove(str(value).lower())
            if len(self.__taglist) == 1:
                self.__tags = self.__taglist[0]
            else:
                self.__tags = ",".join(self.taglist)
        else:
            raise ValueError("tagia ei ole olemassa")

    def __str__(self):
        pad = 8

        return  f"{'Title:':{pad}} {self.title}\n" \
                f"{'Url:':{pad}} {self.url}\n"\
                f"{'Read:' :{pad}} {self.read}\n"\
                f"{'Comment:' :{pad}} {self.comment}\n"\
                f"{'Tags:' :{pad}} {self.tags}"

    def __eq__(self, other: object) -> bool:

        if isinstance(other, VideoTip):
            return self.title == other.title\
                and self.url == other.url\


        return False
