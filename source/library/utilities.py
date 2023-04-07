def split_list(items: list, n_groups: int) -> list[list]:
    """Split a list into n sublists of equal size."""
    k, m = divmod(len(items), n_groups)
    return list(items[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n_groups))
