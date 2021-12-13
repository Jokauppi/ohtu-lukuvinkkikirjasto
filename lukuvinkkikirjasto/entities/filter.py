class Filter:
    # pylint: disable-duplicate-code

    def __init__(self):
        self.__types = []
        self.__name = ""
        self.__author = ""
        self.__isbn = ""
        self.__publication_year = ""
        self.__url = ""
        self.__read = ""
        self.__comment = ""
        self.__taglist = []

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        accepted = ["book", "blog", "video"]
        for type in value:
            if type not in accepted:
                raise ValueError("Virheellinen tyyppi")
        self.__types = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @property
    def publication_year(self):
        return self.__publication_year

    @publication_year.setter
    def publication_year(self, value):
        self.__publication_year = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def read(self):
        return self.__read

    @read.setter
    def read(self, value):
        if value.strip() not in ['k', 'e']:
            raise ValueError
        self.__read = value.strip()

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value

    @property
    def taglist(self):
        return self.__taglist

    @taglist.setter
    def taglist(self, value):
        self.__taglist.append(value)

    def clear_filters(self):
        self.__types.clear()
        self.__name = ""
        self.__author = ""
        self.__isbn = ""
        self.__publication_year = ""
        self.__url = ""
        self.__read = ""
        self.__comment = ""
        self.__taglist.clear()

    def book_filters(self):

        fields, values, comparators, sort_by_values, sort_by_orders = [], [], [], [], []

        if self.__name:
            self.add_field_and_value(fields, values, comparators, 'name', self.__name, ' LIKE ')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'name', 'ASC')
        if self.__author:
            self.add_field_and_value(fields, values, comparators, 'author', self.__author, ' LIKE ')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'author', 'ASC')
        if self.__publication_year:
            self.add_field_and_value(fields,
                                values,
                                comparators,
                                'publication_year',
                                self.publication_year,
                                '=')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'publication_year', 'DESC')
        if self.__isbn:
            self.add_field_and_value(fields, values, comparators, 'isbn', self.__isbn, '=')
        if self.__comment:
            self.add_field_and_value(
                fields, values, comparators, 'comment', self.__comment, ' LIKE '
            )
        if self.__read.lower() == 'k':
            self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if self.__read.lower() == 'e':
            self.add_field_and_value(fields, values, comparators, 'read', '0', '=')
        if self.__taglist:
            for i, _ in enumerate(self.__taglist):
                self.add_field_and_value(
                    fields, values, comparators, 'tags', self.__taglist[i], ' LIKE '
                )

        return fields, values, comparators, sort_by_values, sort_by_orders

    def blog_filters(self):

        fields, values, comparators, sort_by_values, sort_by_orders = [], [], [], [], []

        if self.__name:
            self.add_field_and_value(fields, values, comparators, 'name', self.__name, ' LIKE ')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'name', 'ASC')
        if self.__author:
            self.add_field_and_value(fields, values, comparators, 'author', self.__author, ' LIKE ')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'author', 'ASC')
        if self.__url:
            self.add_field_and_value(fields, values, comparators, 'url', self.__url, ' LIKE ')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'url', 'ASC')
        if self.__comment:
            self.add_field_and_value(
                fields, values, comparators, 'comment', self.__comment, ' LIKE '
            )
        if self.__read.lower() == 'k':
            self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if self.__read.lower() == 'e':
            self.add_field_and_value(fields, values, comparators, 'read', '0', '=')
        if self.__taglist:
            for i, _ in enumerate(self.__taglist):
                self.add_field_and_value(
                    fields, values, comparators, 'tags', self.__taglist[i], ' LIKE '
                )

        return fields, values, comparators, sort_by_values, sort_by_orders

    def video_filters(self):

        fields, values, comparators, sort_by_values, sort_by_orders = [], [], [], [], []

        if self.__name:
            self.add_field_and_value(fields, values, comparators, 'title', self.__name, ' LIKE ')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'title', 'ASC')
        if self.__url:
            self.add_field_and_value(fields, values, comparators, 'url', self.__url, ' LIKE ')
            self.add_sort_bys(sort_by_values, sort_by_orders, 'url', 'ASC')
        if self.__comment:
            self.add_field_and_value(
                fields, values, comparators, 'comment', self.__comment, ' LIKE '
            )
        if self.__read.lower() == 'k':
            self.add_field_and_value(fields, values, comparators, 'read', '1', '=')
        if self.__read.lower() == 'e':
            self.add_field_and_value(fields, values, comparators, 'read', '0', '=')
        if self.__taglist:
            for i, _ in enumerate(self.__taglist):
                self.add_field_and_value(
                    fields, values, comparators, 'tags', self.__taglist[i], ' LIKE '
                )

        return fields, values, comparators, sort_by_values, sort_by_orders


    def add_field_and_value(self, fields, values, comparators, field, value, comparator='='):
        if value:
            fields.append(field)
            values.append(value)
            comparators.append(comparator)

    def add_sort_bys(self, sort_by_values, sort_by_orders, value, order='ASC'):
        if value:
            sort_by_values.append(value)
            sort_by_orders.append(order)


#    def __str__(self):
#        pad = 7
#        tags = ""
#        if self.__taglist:
#            tags = self.__taglist[0]
#        i = 1
#        while i < len(self.__taglist):
#            tags += ", " + str(self.__taglist[i])
#
#
#        return  "\n---------------------\n" \
#                "Aktiiviset filtterit:" \
#                "\n---------------------\n" \
#                f"{'1. Nimike:':{pad}} {self.__name}\n" \
#                f"{'2. Tekijä:':{pad}} {self.__author}\n" \
#                f"{'3. Vuosi:':{pad}} {self.__publication_year}\n" \
#                f"{'4. ISBN:':{pad}} {self.__isbn}\n" \
#                f"{'5. url:':{pad}} {self.__url}\n" \
#                f"{'6. Luettu (K/E):':{pad}} {self.__read}\n" \
#                f"{'7. Kommentti:':{pad}} {self.__read}\n" \
#                f"{'8. Tagit:':{pad}} {tags}\n"
