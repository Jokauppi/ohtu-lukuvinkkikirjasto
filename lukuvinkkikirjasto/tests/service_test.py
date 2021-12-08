import unittest
from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip
from service import Service

class MockBookTipRepository:
    def __init__(self, booktips=None):
        self.booktips = booktips or []

    def get_all(self):
        return self.booktips

    def mark_as_read(self, id):
        self.booktips[id-1].read = True

    def add(self, booktip):
        self.booktips.append(booktip)

        return booktip

    def remove_row(self, booktip):
        self.booktips.remove(booktip)

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

    def get_all(self):
        return self.blogtips

    def add(self, blogtip):
        self.blogtips.append(blogtip)

        return blogtip

    def remove_row(self, blogtip):
        self.blogtips.remove(blogtip)

    def mark_as_read(self, id):
        self.blogtips[id-1].read = True

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

    def get_all(self):
        return self.videotips

    def add(self, videotip):
        self.videotips.append(videotip)

        return videotip

    def remove_row(self, videotip):
        self.videotips.remove(videotip)

    def mark_as_read(self, id):
        self.videotips[id-1].read = True

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

        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001', 1, False)
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '1234', '2002', 2, False)

        self.blogtip_a = BlogTip('Blog1', 'Firstname1, lastname1', 'www.1.com', 1, False)
        self.blogtip_b = BlogTip('Blog2', 'Firstname2, lastname2', 'www.2.com', 2, False)
    
        self.videotip_a = VideoTip('Video1', 'www.video.com/1', 1, False)
        self.videotip_b = VideoTip('VIdeo2', 'www.video.com/2', 2, False)

# Book Tips

    def test_add_book_tip(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())


    def test_mark_book_tip_as_read(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        self.service.create_book_tip(self.booktip_b.name, self.booktip_b.author, self.booktip_b.isbn, self.booktip_b.publication_year)

        self.service.mark_book_tip_as_read(1)
        booktips = self.service.get_read_book_tips(True)

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
    
    def test_get_all_book_tips(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        self.service.create_book_tip(self.booktip_b.name, self.booktip_b.author, self.booktip_b.isbn, self.booktip_b.publication_year)

        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())

    def test_remove_book_tip(self):
        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        self.service.remove_book_tip(self.booktip_a)

        booktips = self.service.get_all_book_tips()
        self.assertEqual(len(booktips), 0)

# Video Tips

    def test_add_video_tip(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url)
        videotips = self.service.get_all_video_tips()

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())


    def test_mark_video_tip_as_read(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url)
        self.service.create_video_tip(self.videotip_b.title, self.videotip_b.url)

        self.service.mark_video_tip_as_read(1)
        videotips = self.service.get_read_video_tips(True)

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())
    
    def test_get_all_video_tips(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url)
        self.service.create_video_tip(self.videotip_b.title, self.videotip_b.url)

        videotips = self.service.get_all_video_tips()

        self.assertEqual(len(videotips), 2)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())
        self.assertEqual(videotips[1].__str__(), self.videotip_b.__str__())

    def test_remove_video_tips(self):
        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url)
        self.service.remove_video_tip(self.videotip_a)

        videotips = self.service.get_all_video_tips()
        self.assertEqual(len(videotips), 0)

# Blog Tips

    def test_add_blog_tip(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url)
        blogtips = self.service.get_all_blog_tips()

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())
    
    def test_mark_blog_tip_as_read(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url)
        self.service.create_blog_tip(self.blogtip_b.name, self.blogtip_b.author, self.blogtip_b.url)

        self.service.mark_blog_tip_as_read(1)
        blogtips = self.service.get_read_blog_tips(True)

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())


    def test_get_all_blog_tips(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url)
        self.service.create_blog_tip(self.blogtip_b.name, self.blogtip_b.author, self.blogtip_b.url)

        blogtips = self.service.get_all_blog_tips()

        self.assertEqual(len(blogtips), 2)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())
        self.assertEqual(blogtips[1].__str__(), self.blogtip_b.__str__())

    def test_remove_blog_tips(self):
        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url)
        self.service.remove_blog_tip(self.blogtip_a)

        blogtips = self.service.get_all_blog_tips()
        self.assertEqual(len(blogtips), 0)

#Search
    def test_search_book_tips(self):
        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        booktips = self.service.search_book_tips(['name', 'author'], ['Book1', 'Firstname1, lastname1'], [], ['name', 'author'], ['ASC','DESC'])

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())

    def test_search_blog_tips(self):
        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url)
        blogtips = self.service.search_blog_tips(['name', 'author'], ['Blog1', 'Firstname1, lastname1'], [], ['name', 'author'], ['ASC','DESC'])

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())

    def test_search_video_tips(self):
        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url)
        videotips = self.service.search_video_tips(['title', 'url'], ['Video1', 'www.video.com/1'], [], ['title', 'url'], ['ASC','DESC'])

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())
