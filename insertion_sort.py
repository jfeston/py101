
def insertion_sort(lst):

    # todo: validate lst has at least one element

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = key

# test run
# todo: replace with unit testing
lst = [7, 4, 9, 2, 6, 3]
print('::: original list %s' %lst)
insertion_sort(lst)
print('::: sorted list %s' % lst)

