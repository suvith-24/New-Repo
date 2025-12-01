"""THis is main module"""
import random


def main() -> list[int]:
    """_summary_

    :Returns: _description_
    :rtype: lsit[int]
    """

    _list = [random.randint(0, 20) for _ in range(50)]

    return _list
