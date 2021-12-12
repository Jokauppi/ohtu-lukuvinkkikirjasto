from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip


class Service:
    def __init__(self, bookrepository, blogrepository, videorepository):
        self._bookrepository = bookrepository
        self._blogrepository = blogrepository
        self._videorepository = videorepository


# Create

    def create_book_tip(self, name, author, isbn, publication_year, comment=''):
        book_tip = BookTip(name, author, isbn, publication_year, comment)
        return self._bookrepository.add(book_tip)

    def create_blog_tip(self, name, author, url, comment=''):
        blog_tip = BlogTip(name, author, url, comment)
        return self._blogrepository.add(blog_tip)

    def create_video_tip(self, title, url, comment=''):
        video_tip = VideoTip(title, url, comment)
        return self._videorepository.add(video_tip)

# Delete

    def remove_tip(self, tip):
        if isinstance(tip, BookTip):
            return self._bookrepository.remove_row(tip)
        elif isinstance(tip, BlogTip):
            return self._blogrepository.remove_row(tip)
        elif isinstance(tip, VideoTip):
            return self._videorepository.remove_row(tip)

# Modify

    def modify(self, modified_tip):
        if isinstance(modified_tip, BookTip):
            return self._bookrepository.modify(modified_tip)
        elif isinstance(modified_tip, VideoTip):
            return self._videorepository.modify(modified_tip)
        elif isinstance(modified_tip, BlogTip):
            return self._blogrepository.modify(modified_tip)

# Comment

    def comment(self, tip, comment):
        if isinstance(tip, BookTip):
            return self._bookrepository.comment(tip, comment)
        elif isinstance(tip, VideoTip):
            return self._videorepository.comment(tip, comment)
        elif isinstance(tip, BlogTip):
            return self._blogrepository.comment(tip, comment)

# Get All

    def get_all_book_tips(self):
        return self._bookrepository.get_all()

    def get_all_blog_tips(self):
        return self._blogrepository.get_all()

    def get_all_video_tips(self):
        return self._videorepository.get_all()

# Get Read/Unread

    def get_read_book_tips(self, read):
        return self._bookrepository.get_read(read)

    def get_read_blog_tips(self, read):
        return self._blogrepository.get_read(read)

    def get_read_video_tips(self, read):
        return self._videorepository.get_read(read)

# Mark as read

    def mark_as_read(self, tip):
        if isinstance(tip, BookTip):
            return self._mark_book_tip_as_read(tip)
        elif isinstance(tip, VideoTip):
            return self._mark_video_tip_as_read(tip)
        elif isinstance(tip, BlogTip):
            return self._mark_blog_tip_as_read(tip)

    def _mark_book_tip_as_read(self, book_tip):
        return self._bookrepository.mark_as_read(book_tip)

    def _mark_blog_tip_as_read(self, blog_tip):
        return self._blogrepository.mark_as_read(blog_tip)

    def _mark_video_tip_as_read(self, video_tip):
        return self._videorepository.mark_as_read(video_tip)


# Search

    def _search_book_tips(self, filter):

        fields, values, comparators, sort_by_values, sort_by_orders = filter.book_filters()

        return self._bookrepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

    def _search_blog_tips(self, filter):

        fields, values, comparators, sort_by_values, sort_by_orders = filter.blog_filters()

        return self._blogrepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

    def _search_video_tips(self, filter):

        fields, values, comparators, sort_by_values, sort_by_orders = filter.video_filters()

        return self._videorepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

# Filter

    def filter_tips(self, filter):
        tips = []

        if not filter.types:
            tips = self._search_all_tips(filter)
        if "book" in filter.types:
            tips += self._search_book_tips(filter)
        if "blog" in filter.types:
            tips += self._search_blog_tips(filter)
        if "video" in filter.types:
            tips += self._search_video_tips(filter)

        return tips

    def _search_all_tips(self, filter):
        tips = self._search_book_tips(filter)
        tips += self._search_blog_tips(filter)
        tips += self._search_video_tips(filter)
        return tips
