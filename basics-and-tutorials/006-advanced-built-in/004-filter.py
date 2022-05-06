friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda x: x.startswith('R'), friends)
print(start_with_r)  # generator

print(list(start_with_r))
print(list(start_with_r))  # already exhausted generator


(friend for friend in friends if friend.startswith('R'))


def my_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i