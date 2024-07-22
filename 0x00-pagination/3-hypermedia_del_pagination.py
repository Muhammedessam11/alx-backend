#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get page info from given index
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        res = dict()
        count = 0
        cvs_data = []
        next_idx = None
        first = index if index else 0
        for i, item in data.items():
            if i >= first and count < page_size:
                cvs_data.append(item)
                count += 1
                continue
            if count == page_size:
                next_idx = i
                break
        res['index'] = index
        res['next_index'] = next_idx
        res['page_size'] = len(cvs_data)
        res['data'] = cvs_data
        return res
