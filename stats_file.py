import numpy as np
def mean(alist):
    """
    This is a mean/average function
    alist -> list type argument
    examples:
    >>> mean([2,3,4])
    """
    alist = np.array(alist)
    tot_items = alist.shape[0]
    print(tot_items)
    print(f"mean: {sum(alist)/tot_items}")
    return sum(alist)/tot_items
