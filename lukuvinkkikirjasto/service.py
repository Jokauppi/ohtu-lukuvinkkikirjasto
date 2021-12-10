from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip


class Service:
    def __init__(self, repository, blogrepository, videorepository):
        self._repository = repository
        self._blogrepository = blogrepository
        self._videorepository = videorepository


# Create

    def create_book_tip(self, name, author, isbn, publication_year, comment):
        book_tip = BookTip(name, author, isbn, publication_year, comment)
        return self._repository.add(book_tip)

    def create_blog_tip(self, name, author, url, comment):
        blog_tip = BlogTip(name, author, url, comment)
        return self._blogrepository.add(blog_tip)

    def create_video_tip(self, title, url, comment):
        video_tip = VideoTip(title, url, comment)
        return self._videorepository.add(video_tip)

# Delete

    def remove_book_tip(self, book_tip):
        return self._repository.remove_row(book_tip)

    def remove_blog_tip(self, blog_tip):
        return self._blogrepository.remove_row(blog_tip)

    def remove_video_tip(self, video_tip):
        return self._videorepository.remove_row(video_tip)

# Modify

    def modify(self, tip, modified_tip):
        if isinstance(tip, BookTip):
            return self._repository.modify(tip, modified_tip)
        elif isinstance(tip, VideoTip):
            return self._videorepository.modify(tip, modified_tip)
        elif isinstance(tip, BlogTip):
            return self._blogrepository.modify(tip, modified_tip)

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

    def mark_as_read(self, tip):
        if isinstance(tip, BookTip):
            return self.mark_book_tip_as_read(tip)
        elif isinstance(tip, VideoTip):
            return self.mark_video_tip_as_read(tip)
        elif isinstance(tip, BlogTip):
            return self.mark_blog_tip_as_read(tip)

    def mark_book_tip_as_read(self, book_tip):
        return self._repository.mark_as_read(book_tip)

    def mark_blog_tip_as_read(self, blog_tip):
        return self._blogrepository.mark_as_read(blog_tip)

    def mark_video_tip_as_read(self, video_tip):
        return self._videorepository.mark_as_read(video_tip)


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
