#!/usr/bin/env python3
""" 0-simple_helper_function.py """

from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
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
