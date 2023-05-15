#!/usr/bin/env python3
""" 2-hypermedia_pagination.py """

import csv
import math
from typing import Dict, List, Tuple, Any


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
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Paginates the dataset and returns a list of rows for the given page
        and page size."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        rows = self.dataset()

        if start_index >= len(rows):
            return []

        return rows[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing hypermedia information for the given
        page and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)
        current_page = page
        next_page = current_page + 1 if current_page < total_pages else None
        prev_page = current_page - 1 if current_page > 1 else None

        page_data = self.get_page(page, page_size)

        return {
            'page_size': len(page_data),
            'page': current_page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Given a page number and page size, returns a tuple of start and end
     indexes for pagination.
    Args:
        page (int): the current page number (starting from 1)
        page_size (int): the number of items per page
    Returns:
        tuple[int, int]: a tuple containing the start index (inclusive)
         and end index (exclusive)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
