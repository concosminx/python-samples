from .common.file_operation import save_to_file


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
        raise NotFoundError(f'{expected} not found')


class NotFoundError(Exception):
    pass


save_to_file("Ana are mere", "new_file.txt")
print(__name__)