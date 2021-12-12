
class BlogTip:
    # pylint: disable-duplicate-code

    def __init__(self, name: str, author: str, url: str, comment: str = '', id_number: int = None, read: bool = False):
        self.name = name
        self.author = author
        self.url = url
        self.id_number = id_number
        self.read = read
        self.comment = comment

    @property
    def name(self):
        return self.__name

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        if not isinstance(value, str):
            raise TypeError("Kommentin pitää olla merkkijono")
        self.__comment = value



    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nimen pitää olla merkkijono")
        if len(value) <= 0 or len(value) > 100:
            raise ValueError("Nimen pituus pitää olla 1-100 merkkiä")
        self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Nimen pitää olla merkkijono")
        if len(value) <= 0 or len(value) > 100:
            raise ValueError("Nimen pituus pitää olla 1-100 merkkiä")
        self.__author = value

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

        return f"{'Title:':{pad}} {self.name}\n" \
                f"{'Author:':{pad}} {self.author}\n" \
                f"{'url:':{pad}} {self.url}\n"\
                f"{'Read:' :{pad}} {self.read}\n"\
                f"{'Comment:' :{pad}} {self.comment}"

    def __eq__(self, other: object) -> bool:

        if isinstance(other, BlogTip):
            return self.name == other.name\
                and self.author == other.author\
                and self.url == other.url\


        return False
