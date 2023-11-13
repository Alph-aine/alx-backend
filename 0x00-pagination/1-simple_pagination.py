#!/usr/bin/env python3


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
        '''
        Verifies if arguments are greater than 0, then get the index range
        and returns values in the range
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        if self.dataset() is None:
            return []

        data_range = index_range(page, page_size)
        return self.dataset()[data_range[0]: data_range[1]]
