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

    

    def add(self, booktip):
        self.booktips.append(booktip)

        return booktip

class MockBlogTipRepository:
    def __init__(self, blogtips=None):
        self.blogtips = blogtips or []

    def get_all(self):
        return self.blogtips

    def add(self, blogtip):
        self.blogtips.append(blogtip)

        return blogtip

class MockVideoTipRepository:
    def __init__(self, videotips=None):
        self.videotips = videotips or []

    def get_all(self):
        return self.videotips

    def add(self, videotip):
        self.videotips.append(videotip)

        return videotip

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(MockBookTipRepository(), MockBlogTipRepository(), MockVideoTipRepository())

        self.booktip_a = BookTip('Book1', 'Firstname1, lastname1', '1234', '2001')
        self.booktip_b = BookTip('Book2', 'Firstname2, lastname2', '1234', '2002')

        self.blogtip_a = BlogTip('Blog1', 'Firstname1, lastname1', 'www.1.com')
        self.blogtip_b = BlogTip('Blog2', 'Firstname2, lastname2', 'www.2.com')
    
        self.videotip_a = VideoTip('Video1', 'www.video.com/1')
        self.videotip_b = VideoTip('VIdeo2', 'www.video.com/2')

# Book Tips

    def test_add_book_tip(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 1)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
    
    
    def test_get_all_book_tips(self):

        self.service.create_book_tip(self.booktip_a.name, self.booktip_a.author, self.booktip_a.isbn, self.booktip_a.publication_year)
        self.service.create_book_tip(self.booktip_b.name, self.booktip_b.author, self.booktip_b.isbn, self.booktip_b.publication_year)

        booktips = self.service.get_all_book_tips()

        self.assertEqual(len(booktips), 2)
        self.assertEqual(booktips[0].__str__(), self.booktip_a.__str__())
        self.assertEqual(booktips[1].__str__(), self.booktip_b.__str__())
        
# Video Tips

    def test_add_video_tip(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url)
        videotips = self.service.get_all_video_tips()

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())
    
    
    def test_get_all_video_tips(self):

        self.service.create_video_tip(self.videotip_a.title, self.videotip_a.url)
        self.service.create_video_tip(self.videotip_b.title, self.videotip_b.url)

        videotips = self.service.get_all_video_tips()

        self.assertEqual(len(videotips), 2)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())
        self.assertEqual(videotips[1].__str__(), self.videotip_b.__str__())

# Blog Tips

    def test_add_blog_tip(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url)
        blogtips = self.service.get_all_blog_tips()

        self.assertEqual(len(blogtips), 1)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())
    
    
    def test_get_all_blog_tips(self):

        self.service.create_blog_tip(self.blogtip_a.name, self.blogtip_a.author, self.blogtip_a.url)
        self.service.create_blog_tip(self.blogtip_b.name, self.blogtip_b.author, self.blogtip_b.url)

        blogtips = self.service.get_all_blog_tips()

        self.assertEqual(len(blogtips), 2)
        self.assertEqual(blogtips[0].__str__(), self.blogtip_a.__str__())
        self.assertEqual(blogtips[1].__str__(), self.blogtip_b.__str__())
