from entities.book_tip import BookTip
from entities.blog_tip import BlogTip
from entities.video_tip import VideoTip
from entities.filter_params import book_params, blog_params, video_params


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
            self._bookrepository.remove_row(tip)
        if isinstance(tip, BlogTip):
            self._blogrepository.remove_row(tip)
        if isinstance(tip, VideoTip):
            self._videorepository.remove_row(tip)

# Modify

    def modify(self, modified_tip):
        if isinstance(modified_tip, BookTip):
            self._bookrepository.modify(modified_tip)
        if isinstance(modified_tip, VideoTip):
            self._videorepository.modify(modified_tip)
        if isinstance(modified_tip, BlogTip):
            self._blogrepository.modify(modified_tip)

# Comment

    def comment(self, tip, comment):
        if isinstance(tip, BookTip):
            self._bookrepository.comment(tip, comment)
        if isinstance(tip, VideoTip):
            self._videorepository.comment(tip, comment)
        if isinstance(tip, BlogTip):
            self._blogrepository.comment(tip, comment)

# Tag

    def update_tags(self, tip):
        if isinstance(tip, BlogTip):
            self._blogrepository.update_tags(tip)
        if isinstance(tip, BookTip):
            self._bookrepository.update_tags(tip)
        if isinstance(tip, VideoTip):
            self._videorepository.update_tags(tip)

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
            self._mark_book_tip_as_read(tip)
        if isinstance(tip, VideoTip):
            self._mark_video_tip_as_read(tip)
        if isinstance(tip, BlogTip):
            self._mark_blog_tip_as_read(tip)

    def _mark_book_tip_as_read(self, book_tip):
        self._bookrepository.mark_as_read(book_tip)

    def _mark_blog_tip_as_read(self, blog_tip):
        self._blogrepository.mark_as_read(blog_tip)

    def _mark_video_tip_as_read(self, video_tip):
        self._videorepository.mark_as_read(video_tip)


# Search

    def _search_book_tips(self, my_filter):

        fields, values, comparators, sort_by_values, sort_by_orders = my_filter.book_filters()

        return self._bookrepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

    def _search_blog_tips(self, my_filter):

        fields, values, comparators, sort_by_values, sort_by_orders = my_filter.blog_filters()

        return self._blogrepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

    def _search_video_tips(self, my_filter):

        fields, values, comparators, sort_by_values, sort_by_orders = my_filter.video_filters()

        return self._videorepository.search_tips(fields,
                                            values,
                                            comparators,
                                            sort_by_values,
                                            sort_by_orders)

# Filter

    def filter_tips(self, my_filter):
        filter_params = self._get_filter_params(my_filter)

        if not filter_params:
            return self._search_all_tips(my_filter)

        if not my_filter.types:
            return self._filter_all(my_filter, filter_params)

        tips = []

        if "book" in my_filter.types:
            tips += self._filter_books(my_filter, filter_params)
        if "blog" in my_filter.types:
            tips += self._filter_blogs(my_filter, filter_params)
        if "video" in my_filter.types:
            tips += self._filter_videos(my_filter, filter_params)

        return tips

    def _search_all_tips(self, my_filter):
        tips = self._search_book_tips(my_filter)
        tips += self._search_blog_tips(my_filter)
        tips += self._search_video_tips(my_filter)
        return tips

    def _get_filter_params(self, my_filter):
        filter_params = set()

        for param, value in vars(my_filter).items():
            if value:
                filter_params.add(param)

        return filter_params

    def _filter_all(self, my_filter, filter_params):
        tips = []

        tips += self._filter_books(my_filter, filter_params)
        tips += self._filter_blogs(my_filter, filter_params)
        tips += self._filter_videos(my_filter, filter_params)

        return tips

    def _filter_books(self, my_filter, filter_params):
        if filter_params.issubset(book_params):
            return self._search_book_tips(my_filter)

        return []

    def _filter_blogs(self, my_filter, filter_params):
        if filter_params.issubset(blog_params):
            return self._search_blog_tips(my_filter)

        return []

    def _filter_videos(self, my_filter, filter_params):
        if filter_params.issubset(video_params):
            return self._search_video_tips(my_filter)

        return []
