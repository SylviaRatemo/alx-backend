#!/usr/bin/env python3
"""
Pagination Task 0
"""
import csv
import math
from typing import List, Tuple


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
        assert isinstance(page, int) and page > 0, \
            "Page should be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size should be an integer greater than 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []  # Empty list if start_index is out of range

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        assert isinstance(page, int) and page > 0, \
            "Page should be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size should be an integer greater than 0."

        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(dataset_page),
            'page': page,
            'data': dataset_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size should be greater than 0.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
