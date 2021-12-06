from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip


class Service:
    def __init__(self, repository, blogrepository, videorepository):
        self._repository = repository
        self._blogrepository = blogrepository
        self._videorepository = videorepository


# Create

    def create_book_tip(self, name, author, isbn, publication_year):
        book_tip = BookTip(name, author, isbn, publication_year)
        return self._repository.add(book_tip)

    def create_blog_tip(self, name, author, url):
        blog_tip = BlogTip(name, author, url)
        return self._blogrepository.add(blog_tip)

    def create_video_tip(self, title, url):
        video_tip = VideoTip(title, url)
        return self._videorepository.add(video_tip)

# Get All

    def get_all_book_tips(self):
        return self._repository.get_all()

    def get_all_blog_tips(self):
        return self._blogrepository.get_all()

    def get_all_video_tips(self):
        return self._videorepository.get_all()

# Get Read/Unread

    def get_read_book_tips(self, read):
        return self._repository.get_read(read)

    def get_read_blog_tips(self, read):
        return self._blogrepository.get_read(read)

    def get_read_video_tips(self, read):
        return self._videorepository.get_read(read)

# Mark as read

    def mark_book_tip_as_read(self, id_number):
        return self._repository.mark_as_read(id_number)

    def mark_blog_tip_as_read(self, id_number):
        return self._blogrepository.mark_as_read(id_number)

    def mark_video_tip_as_read(self, id_number):
        return self._videorepository.mark_as_read(id_number)


# Search

    def search_book_tips(self, fields, values, comparators, sort_by_values, sort_by_orders):
        return self._repository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

    def search_blog_tips(self, fields, values, comparators, sort_by_values, sort_by_orders):
        return self._blogrepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

    def search_video_tips(self, fields, values, comparators, sort_by_values, sort_by_orders):
        return self._videorepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)
