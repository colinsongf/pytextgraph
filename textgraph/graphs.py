# coding: utf-8
"""
Graphs
"""

import math


def spark(nums):
    """
    Returns a vertical spark graph from a list of integers.

    nums -- list of integers to graph

    """
    parts = u' ▁▂▃▄▅▆▇█'
    fraction = max(nums) / float(len(parts) - 1)
    # Replace each number with its appropriate part then join
    return ''.join(parts[int(math.ceil(x / fraction))] for x in nums)


def horizontal_graph(data, width=79):
    """
    Returns a horizontal graph from a list of integers or
    list of tuples (label, integer).

    data -- list of integers or list of tuples (label, integer)
    width -- width of output (int)

    """
    parts = ['█' * i for i in range(0, width)]

    if isinstance(data[0], tuple):

        fraction = max([v[1] for v in data]) / float(len(parts) - 1)

        # Pad labels
        max_label_length = len(max([v[0] for v in data], key=len))
        data = [(v[0] + " " * (max_label_length - len(v[0])), v[1])
                for v in data]

        # Create Lines and output
        out = ""
        out_line = "{label} {parts}\n"
        for i in range(len(data)):
            line_parts = parts[int(math.ceil(data[i][1] / fraction))]
            out = out + out_line.format(label=data[i][0],
                                        parts=line_parts)
        return out

    elif isinstance(data[0], int):
        fraction = max(data) / float(len(parts) - 1)
        return ''.join(parts[int(math.ceil(x / fraction))] + "\n" for x in data)
    else:
        raise TypeError


def vertical_graph(nums, height=10):
    """
    Returns a vertical graph from a list of integers.
    Height of the graph can be specified.

    nums -- list of integers to graph
    height -- height of largest bar (int)

    """
    character = '▉'
    fraction = max(nums) / float(height)
    nums = [int(math.ceil(n / fraction)) for n in nums]

    out = ""
    row_numbers = list(range(1, height + 1))
    row_numbers.reverse()
    for i in row_numbers:
        for n in nums:
            if n >= i:
                out = out + character
            else:
                out = out + ' '
        out = out + "\n"
    return out
