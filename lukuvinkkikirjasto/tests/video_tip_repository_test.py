import sqlite3
from typing import Any
import unittest
from repositories.video_tip_repository import VideoTipRepository
from entities.video_tip import VideoTip


class TestVideoTipRepository(unittest.TestCase):
    def setUp(self):
        #repository.delete_all()
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repository = VideoTipRepository(self.connection)

        self.tip_a = VideoTip('Video1', 'video.example.com/1', 'Kommentti', 1, False) 
        self.tip_b = VideoTip('Video2', 'video.example.com/2', 'Kommentti', 2, False)
        self.tip_c = VideoTip('Video3', 'video.example.com/3', 'Kommentti', 3, True)
        self.tip_d = VideoTip('Video4', 'video.example.com/4', 'Kommentti', 4, True)
        
    def test_add(self):
        self.repository.add(self.tip_a)
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())

    def test_delete(self):
        self.repository.add(self.tip_a)
        self.repository.remove_row(self.tip_a)
        tips = self.repository.get_all()
        
        self.assertEqual(len(tips), 0)

    def test_modify(self):
        self.repository.add(self.tip_a)
        tip_a_mod = VideoTip('Video2', 'video.example.com/2', 'Kommentti', 1, False)
        self.repository.modify(tip_a_mod)
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].__str__(), self.tip_b.__str__())

    def test_comment(self):
        self.repository.add(self.tip_a)
        self.repository.comment(self.tip_a, "Uusi kommentti")
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].comment, "Uusi kommentti")


    def test_get_all(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_b.__str__())
    
    def test_get_read(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.add(self.tip_c)
        self.repository.add(self.tip_d)
        tips = self.repository.get_read(True)

        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), self.tip_c.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_d.__str__())
    
    def test_get_unread(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.add(self.tip_c)
        self.repository.add(self.tip_d)
        tips = self.repository.get_read(False)

        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_b.__str__())
    
    def test_marking_as_read_works_correctly(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        tips = self.repository.get_read(True)

        self.assertEqual(len(tips), 0)

        self.repository.mark_as_read(self.tip_a)
        tips = self.repository.get_read(True)

        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].__str__(), "Title:  Video1\nUrl:    video.example.com/1\nRead:   True\nComment: Kommentti")
    
    def test_mark_as_read_returns_error(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.assertFalse(self.repository.mark_as_read(VideoTip("title", "www.google.fi")))

    def test_cannot_add_same_video_twice(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_a)
        tips = self.repository.get_all()

        self.assertEqual(len(tips), 1)
    
    def test_delete_all(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.delete_all()
        
        tips = self.repository.get_all()
        self.assertEqual(len(tips), 0)
    
    def test_drop_tables(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        self.repository.drop_tables()
        self.assertRaises(
            Exception,
            lambda: self.repository.get_all()
        )
    
    def test_search_video_tips(self):
        self.repository.add(self.tip_a)
        self.repository.add(self.tip_b)
        tip_c = VideoTip('Video1', 'video.example.fi/2', '', 1, False)
        self.repository.add(tip_c)
        tips = self.repository.search_tips([], [], [], [], [])
        self.assertEqual(len(tips), 3)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_b.__str__())
        self.assertEqual(tips[2].__str__(), tip_c.__str__())
        tips = self.repository.search_tips(['title'], ['Video1'], [], [], [])
        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        self.assertEqual(tips[1].__str__(), tip_c.__str__())
        tips = self.repository.search_tips(['title'], ['Video1'], [], ['title', 'url'], ['ASC','DESC'])
        self.assertEqual(len(tips), 2)
        self.assertEqual(tips[0].__str__(), tip_c.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_a.__str__())
        tips = self.repository.search_tips(['title', 'url'], ['Video1', 'video.example.com/1'], [], ['title', 'url'], ['ASC','DESC'])
        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        tips = self.repository.search_tips([], [], [], ['title', 'url'], ['ASC','DESC'])
        self.assertEqual(len(tips), 3)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
        self.assertEqual(tips[1].__str__(), self.tip_b.__str__())
        self.assertEqual(tips[2].__str__(), tip_c.__str__())
        self.assertEqual(self.repository.where_string([],[]), "")
        self.assertEqual(self.repository.order_string([],[]), "")
        tips = self.repository.search_tips(['title', 'url'], ['Video1', 'video.example.com/1'], ['LIKE','LIKE'], [], [])
        self.assertEqual(len(tips), 1)
        self.assertEqual(tips[0].__str__(), self.tip_a.__str__())
