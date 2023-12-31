#!/usr/bin/env python3
'''Simple Pagination'''

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''Returns the start and en indexes of a page'''
    start: int = (page - 1) * page_size
    return start, start + page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Returns a page of data """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        if self.dataset() is None:
            return []

        data_range = index_range(page, page_size)
        return self.dataset()[data_range[0]: data_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        '''Returns concise info about dataset'''

        data = self.get_page(page, page_size)
        data_set = self.__dataset
        len_set = len(data_set) if data_set else 0

        total_pages = math.ceil(len_set / page_size) if data_set else 0
        page_size = len(data) if data else 0

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        hypermedia = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
        return hypermedia
