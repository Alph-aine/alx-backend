#!/usr/bin/env python3
'''Calculate the limit of a page'''


def index_range(page: int, page_size: int) -> tuple:
    '''Returns the start and en indexes of a page'''
    offset: int = (page - 1) * page_size
    return (offset, offset + page_size)
