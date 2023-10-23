#!/usr/bin/env python3
"""
Pagination Task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Parameters:
    - page: Page number (1-indexed).
    - page_size: Number of items per page.

    Returns:
    A tuple containing the start and end index for the specified page.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size should be greater than 0.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
