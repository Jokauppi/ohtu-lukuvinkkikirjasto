import unittest
from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip
from service import Service
from entities.filter import Filter

class MockBookTipRepository:
    def __init__(self, booktips=None):
        self.booktips = booktips or []
        self.index = 1

    def get_all(self):
        return self.booktips

    def mark_as_read(self, booktip):
        for i, e in enumerate(self.booktips):
            if e.id_number == booktip.id_number:
                self.booktips[i].read = True

    def add(self, booktip):
        new = BookTip(booktip.name, booktip.author,
                        booktip.isbn, booktip.publication_year,
                        booktip.comment,
                        self.index, False)
        self.booktips.append(new)
        self.index += 1

        return booktip

    def remove_row(self, booktip):
        self.booktips.remove(booktip)

    def comment(self, booktip, comment):
        for i, e in enumerate(self.booktips):
            if e.id_number == booktip.id_number:
                self.booktips[i].comment = comment

    def get_read(self, read):
        if read:
            return[book for book in self.booktips if book.read == True]

    def search_tips(self, fields, values, comparators, sort_by_values, sort_by_orders):
        tips = filter(
            lambda tip: tip.name == values[0],
            self.booktips
        )
        return list(tips)

class MockBlogTipRepository:
    def __init__(self, blogtips=None):
        self.blogtips = blogtips or []
        self.index = 1

    def get_all(self):
        return self.blogtips

    def add(self, blogtip):
        new = BlogTip(blogtip.name, blogtip.author,
                        blogtip.url,
                        blogtip.comment,
                        self.index, False)
        self.blogtips.append(new)
        self.index += 1

        return blogtip

    def remove_row(self, blogtip):
        self.blogtips.remove(blogtip)

    def comment(self, blogtip, comment):
        for i, e in enumerate(self.blogtips):
            if e.id_number == blogtip.id_number:
                self.blogtips[i].comment = comment

    def mark_as_read(self, blogtip):
        for i, e in enumerate(self.blogtips):
            print(e.id_number, blogtip.id_number, e.read)
            if e.id_number == blogtip.id_number:
                self.blogtips[i].read = True
            print(e.id_number, blogtip.id_number, e.read)

    def get_read(self, read):
        if read:
            return[blog for blog in self.blogtips if blog.read == True]

    def search_tips(self, fields, values, comparators, sort_by_values, sort_by_orders):
        tips = filter(
            lambda tip: tip.name == values[0],
            self.blogtips
        )
        return list(tips)

class MockVideoTipRepository:
    def __init__(self, videotips=None):
        self.videotips = videotips or []
        self.index = 1

    def get_all(self):
        return self.videotips

    def add(self, videotip):
        new = VideoTip(videotip.title, videotip.url, videotip.comment,
                        self.index, False)
        self.videotips.append(new)
        self.index += 1

        return videotip

    def remove_row(self, videotip):
        self.videotips.remove(videotip)

    def comment(self, videotip, comment):
        for i, e in enumerate(self.videotips):
            if e.id_number == videotip.id_number:
                self.videotips[i].comment = comment

    def mark_as_read(self, videotip):
        for i, e in enumerate(self.videotips):
            if e.id_number == videotip.id_number:
                self.videotips[i].read = True

    def get_read(self, read):
        if read:
            return[video for video in self.videotips if video.read == True]

    def search_tips(self, fields, values, comparators, sort_by_values, sort_by_orders):
        tips = filter(
            lambda tip: tip.title == values[0],
            self.videotips
        )
        return list(tips)

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(MockBookTipRepository(), MockBlogTipRepository(), MockVideoTipRepository())

        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001', '', 1, False)
        self.booktip_a_read = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001', '', 1, True)
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '1234', '2002', '', 2, False)

        self.blogtip_a = BlogTip('Blog1', 'Firstname1, lastname1', 'www.1.com', '', 1, False)
        self.blogtip_a_read = BlogTip('Blog1', 'Firstname1, lastname1', 'www.1.com', '', 1, True)
        self.blogtip_b = BlogTip('Blog2', 'Firstname2, lastname2', 'www.2.com', '', 2, False)
    
        self.videotip_a = VideoTip('Video1', 'www.video.com/1', '', 1, False)
        self.videotip_a_read = VideoTip('Video1', 'www.video.com/1', '', 1, True)
        self.videotip_b = VideoTip('VIdeo2', 'www.video.com/2', '', 2, False)

# Book Tips

    def test_add_book_tip(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year, self.booktip_a.comment)
        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())


    def test_mark_book_tip_as_read(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year, self.booktip_a.comment)
        self.service.create_book_tip(self.booktip_b.name, self.booktip_b.author, self.booktip_b.isbn, self.booktip_b.publication_year, self.booktip_b.comment)

        self.service.mark_as_read(self.booktip_a)
        booktips = self.service.get_read_book_tips(True)

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a_read.__str__())
    
    def test_get_all_book_tips(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year, self.booktip_a.comment)
        self.service.create_book_tip(self.booktip_b.name, self.booktip_b.author, self.booktip_b.isbn, self.booktip_b.publication_year, self.booktip_b.comment)

        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())

    def test_remove_book_tip(self):
        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year, self.booktip_a.comment)
        self.service.remove_tip(self.booktip_a)

        booktips = self.service.get_all_book_tips()
        self.assertEqual(len(booktips), 0)
    
    def test_comment_book_tip(self):
        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year, self.booktip_a.comment)
        self.service.comment(self.booktip_a, "Uusi kommentti")

        booktips = self.service.get_all_book_tips()
        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].comment, "Uusi kommentti")


# Video Tips

    def test_add_video_tip(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url, self.videotip_a.comment)
        videotips = self.service.get_all_video_tips()

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())


    def test_mark_video_tip_as_read(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url, self.videotip_a.comment)
        self.service.create_video_tip(self.videotip_b.title, self.videotip_b.url, self.videotip_b.comment)

        self.service.mark_as_read(self.videotip_a)
        videotips = self.service.get_read_video_tips(True)

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a_read.__str__())
    
    def test_get_all_video_tips(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url, self.videotip_a.comment)
        self.service.create_video_tip(self.videotip_b.title, self.videotip_b.url, self.videotip_b.comment)

        videotips = self.service.get_all_video_tips()

        self.assertEqual(len(videotips), 2)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())
        self.assertEqual(videotips[1].__str__(), self.videotip_b.__str__())

    def test_remove_video_tips(self):
        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url, self.videotip_a.comment)
        self.service.remove_tip(self.videotip_a)

        videotips = self.service.get_all_video_tips()
        self.assertEqual(len(videotips), 0)

    def test_comment_video_tip(self):
        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url, self.videotip_a.comment)
        self.service.comment(self.videotip_a, "Uusi kommentti")

        videotips = self.service.get_all_video_tips()
        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].comment, "Uusi kommentti")

# Blog Tips

    def test_add_blog_tip(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url, self.blogtip_a.comment)
        blogtips = self.service.get_all_blog_tips()

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())
    
    def test_mark_blog_tip_as_read(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url, self.blogtip_a.comment)
        self.service.create_blog_tip(self.blogtip_b.name, self.blogtip_b.author, self.blogtip_b.url, self.blogtip_a.comment)

        self.service.mark_as_read(self.blogtip_a)
        blogtips = self.service.get_read_blog_tips(True)

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a_read.__str__())


    def test_get_all_blog_tips(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url, self.blogtip_a.comment)
        self.service.create_blog_tip(self.blogtip_b.name, self.blogtip_b.author, self.blogtip_b.url, self.blogtip_b.comment)

        blogtips = self.service.get_all_blog_tips()

        self.assertEqual(len(blogtips), 2)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())
        self.assertEqual(blogtips[1].__str__(), self.blogtip_b.__str__())

    def test_remove_blog_tips(self):
        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url, self.blogtip_a.comment)
        self.service.remove_tip(self.blogtip_a)

        blogtips = self.service.get_all_blog_tips()
        self.assertEqual(len(blogtips), 0)

    
    def test_comment_blog_tip(self):
        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url, self.blogtip_a.comment)
        self.service.comment(self.blogtip_a, "Uusi kommentti")

        blogtips = self.service.get_all_blog_tips()
        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].comment, "Uusi kommentti")

#Search
    def test_search_book_tips(self):

        filter = Filter()
        filter.name = 'Book1'
        filter.author = 'Firstname1, lastname1'

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year, self.booktip_a.comment)
        booktips = self.service._search_book_tips(filter)

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())

    def test_search_blog_tips(self):

        filter = Filter()
        filter.name = 'Blog1'
        filter.author = 'Firstname1, lastname1'

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url, self.blogtip_a.comment)
        blogtips = self.service._search_blog_tips(filter)

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())

    def test_search_video_tips(self):

        filter = Filter()
        filter.name = 'Video1'
        filter.url = 'www.video.com/1'

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url, self.videotip_a.comment)
        videotips = self.service._search_video_tips(filter)

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())

    #Filter

    def test_filter_tips(self):
        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year, self.booktip_a.comment)
        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url, self.blogtip_a.comment)
        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url, self.videotip_a.comment)

        filter = Filter()
        filter.name = "Book1"
        tips = self.service.filter_tips(filter)
        self.assertEqual(len(tips), 1)
        filter.types = ["book", "blog", "video"]
        tips = self.service.filter_tips(filter)
        self.assertEqual(len(tips), 1)
        tips = self.service._search_all_tips(filter)
        filter.clear_filters()
        filter.name = self.blogtip_a.name
        self.assertEqual(len(tips), 1)
        
        
