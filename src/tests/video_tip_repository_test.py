import sqlite3
from typing import Any
import unittest
from repositories.video_tip_repository import VideoTipRepository
from entities.video_tip import VideoTip


class TestVideoTipRepository(unittest.TestCase):
    def setUp(self):
        #video_tip_repository.delete_all()
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.video_tip_repository = VideoTipRepository(self.connection)

        self.videotip_a = VideoTip('Video1', 'video.example.com/1', 1, False) 
        self.videotip_b = VideoTip('Video2', 'video.example.com/2', 2, False)

    def test_add(self):
        self.video_tip_repository.add(self.videotip_a)
        videotips = self.video_tip_repository.get_all()

        self.assertEqual(len(videotips), 1)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())

    def test_get_all(self):
        self.video_tip_repository.add(self.videotip_a)
        self.video_tip_repository.add(self.videotip_b)
        videotips = self.video_tip_repository.get_all()

        self.assertEqual(len(videotips), 2)
        self.assertEqual(videotips[0].__str__(), self.videotip_a.__str__())
        self.assertEqual(videotips[1].__str__(), self.videotip_b.__str__())

    def test_cannot_add_same_video_twice(self):
        self.video_tip_repository.add(self.videotip_a)
        self.video_tip_repository.add(self.videotip_a)
        videotips = self.video_tip_repository.get_all()

        self.assertEqual(len(videotips), 1)
    
    def test_delete_all(self):
        self.video_tip_repository.add(self.videotip_a)
        self.video_tip_repository.add(self.videotip_b)
        self.video_tip_repository.delete_all()
        
        videotips = self.video_tip_repository.get_all()
        self.assertEqual(len(videotips), 0)
    
    def test_drop_tables(self):
        self.video_tip_repository.add(self.videotip_a)
        self.video_tip_repository.add(self.videotip_b)
        self.video_tip_repository.drop_tables()
        self.assertRaises(
            Exception,
            lambda: self.video_tip_repository.get_all()
        )