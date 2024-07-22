#!/usr/bin/env python3
'''Pagination module
'''
from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns a range oof indexes of a pagination param
    '''
    first = (page - 1) * page_size
    last = first + page_size
    return (first, last)


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
        '''get data based on ranges of index
        '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        first, last = index_range(page, page_size)
        data = self.dataset()
        if first > len(data):
            return []
        return data[first:last]
