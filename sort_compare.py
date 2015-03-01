import time
import random

def insertion_sort(a_list):
    t_start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value
    t_end = time.time()
    t_diff = t_end - t_start
    return { "lsit": a_list, "difference": t_diff}

def shell_sort(a_list):
    t_start = time.time()
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    t_end = time.time()
    t_diff = t_end - t_start
    return { "lsit": a_list, "difference": t_diff}

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def python_sort(a_list):
    t_start = time.time()
    a_list = a_list.sort()
    t_end = time.time()
    t_diff = t_end - t_start
    return { "lsit": a_list, "difference": t_diff}

def random_list(limit):  
    temp_list = random.sample(xrange(1, (limit+1)), 100)  
    return temp_list

def main():
    test_list = [500,1000,10000]

    for test in test_list:
        sort_types = {
            'Insertion':0.0, 
            'Shell': 0.0, 
            'Python': 0.0
        }

        i = 0
        while i < 100:
            temp_list = random_list(test)
            sort_types['Insertion'] += insertion_sort(temp_list)["difference"]
            sort_types['Shell'] += shell_sort(temp_list)["difference"]
            sort_types['Python'] += python_sort(temp_list)["difference"]
            i += 1

        for sort_type in sort_types:
            print "%s Sort took %10.7f seconds to run, on average %s" % (sort_type, sort_types[sort_type] / 100, test)


if __name__ == "__main__":
    main()
