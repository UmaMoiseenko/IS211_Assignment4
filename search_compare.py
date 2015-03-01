import time
import random

def sequential_search(a_list, item):
    a_list.sort() 
    t_start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    t_end = time.time()
    t_diff = t_end - t_start
    return { "found": found, "difference": t_diff}

def ordered_sequential_search(a_list, item):
    t_start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    t_end = time.time()
    t_diff = t_end - t_start
    return { "found": found, "difference": t_diff}

def binary_search_iterative(a_list, item):
    a_list.sort()
    t_start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    t_end = time.time()
    t_diff = t_end - t_start
    return { "found": found, "difference": t_diff}

def binary_search_recursive(a_list, item):
    a_list.sort()
    t_start = time.time()
    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)
            
    t_end = time.time()
    t_diff = t_end - t_start
    return { "found": found, "difference": t_diff}

def random_list(limit):  
    temp_list = random.sample(xrange(1, (limit+1)), 100)  
    return temp_list

def main():
    test_list = [500,1000,10000]

    for test in test_list:
        search_types = {
            'Sequential': 0.0, 
            'Ordered Sequential':0.0, 
            'Iterative Binary': 0.0, 
            'Recursive Binary': 0.0
        }
        i = 0

        while i < 100:
            temp_list = random_list(test)

            search_types['Sequential'] += sequential_search(temp_list, -1)["difference"]
            search_types['Ordered Sequential'] += ordered_sequential_search(temp_list, -1)["difference"]
            search_types['Iterative Binary'] += binary_search_iterative(temp_list, -1)["difference"]
            search_types['Recursive Binary'] += binary_search_recursive(temp_list, -1)["difference"]
            i += 1

        for search_type in search_types:
            print "%s Search took %10.7f seconds to run, on average %s" % (search_type, search_types[search_type] / 100, test)


if __name__ == "__main__":
    main()
