#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:01:49 2019

@author: Alessandro Caioli
"""

import time
import numpy as np
import math


# This is a timer decorator I wrote to time the functions. You basically give it the function you want to measure
# and then when you call the function it will also return the time it took to run
def timer(func, name, verbose=False):
    def wrapper(x):
        start = time.time()
        a = func(x)
        end = time.time()
        if verbose:
            print("{} took {} seconds to run".format(name, end-start))
        return a, end-start
    return wrapper

# Bubble Sort
def bubble_sort(l):
    while True:
        changes = 0
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                changes += 1
        if changes == 0:
            break
    return l


# Merge Sort
def merge_sort(arr): 
    """ Divides the arr in smaller subarrays until you only have subarrays with len(a) which are ordered by definition
    (there's nothing to compare them to) with a series of recursive calls. Then calls the merge function which merges
    and orders the subarrays at the same time"""
    if len(arr) == 1:
        return arr
    med = math.floor(len(arr)/2)
    left = merge_sort(arr[:med])
    right = merge_sort(arr[med:])
    return _merge(left, right)
	
def _merge(l, r):   
    i = 0
    j = 0
    sorted_arr = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            sorted_arr.append(l[i])
            i += 1
        else:
            sorted_arr.append(r[j])
            j += 1
    if i < len(l):
        sorted_arr += l[i:]
    elif j < len(r):
        sorted_arr += r[j:]
    return sorted_arr


# Quick Sort
def quick_sort(l):
    """ Calls the partition function which in turn takes a pivot value (in this case it's always the right-most value),
    brings everything smaller on its left side and everything bigger on its right, then calls the partition function again and keep doing the same
    until the whole array is sorted (at some point giving the pivot_index + 1 will make the low higher than the high,
    that's the cue the function needs to stop calling itself) """
    low = 0
    high = len(l)-1
    _partition(l, low, high)
    return l


def _partition(array, low, high): # Recursive, calls itself every iteration.
                                  # Partition always takes as input the whole array, the only thing that changes
                                  # between calls are low and high
    if low < high:
        pivot = array[high]
        i = low

        for j in range(low, high):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[high], array[i] = array[i], array[high]
        _partition(array, low, i - 1)
        _partition(array, i + 1, high)


# Selection Sort
def selection_sort(l):
    
    for i in range(len(l)-1):
        smallest_i = i
        for j in range(i+1, len(l)):
            if l[j] < l[smallest_i]:
                smallest_i = j
        l[i], l[smallest_i] = l[smallest_i], l[i]
    return l


def time_sorting_functions(functions, names, dataset_size=100, iterations=100, verbose=True):
    
    """ Wraps each function in a timing decorator and stores the means from n iterations for each function.
        Then prints out the results.
        About the confusing result with merge_sort, checking on internet it seems than on small datasets it does perform
        similarly if not straight out worst than bubble_sort which has a better best case scenario.
        So if the dataset is either small or better sorted, the difference is not noticeable.
        On the other hand MergeSort should be very robust to changes in both the sortedness of the array and its size,
        making it better for bigger or less ordered datasets.
        Here for reference: 
        https://www.researchgate.net/post/Why_is_the_bubble_sort_algorithm_better_in_term_of_speed_for_the_same_resources_than_merge_sort_for_small_sets_of_data
    """        
    
    results = {}
    best_score = float("inf")
    worst_score = -float("inf")
    best_name = ""
    worst_name = ""
    
    for function, name in zip(functions, names):
        times = []
        func = timer(function, name) # from here on, when we call the function it will also measure its time
        for _ in range(iterations):
            list_to_sort = np.random.randint(0, 2000, dataset_size) # low and high arguments are chosen arbitrarily,
                                                                    # feel free to change them
            sorted_list, t = func(list_to_sort)
            times.append(t)
        m = np.mean(times)
        results[m] = name
        if m < best_score:
            best_score = m
            best_name = name
        if m > worst_score:
            worst_score = m
            worst_name = name
    
    if verbose:
        print("Results (from best to worst):")
        for mean in sorted(results.keys()):
            print("{}: {}".format(results[mean], mean))
        print()
    
    print("The best sorting algorithm was {}, taking on average {} seconds.".format(best_name, best_score))
    print("It was {} faster than the worst one, {}.".format(worst_score/best_score, worst_name))
            
    

if __name__ == "__main__":
    # with a small dataset (merge_sort equal or worst to bubble_sort)
    time_sorting_functions([bubble_sort, selection_sort, quick_sort, merge_sort], 
                           names=["BubbleSort", "SelectionSort", "QuickSort", "MergeSort"],
                           dataset_size=10)
    
    # with a bigger dataset (merge_sort outperforms both bubble_sort and selection_sort, and performs at the same level
    # of quicksort)
    time_sorting_functions([bubble_sort, selection_sort, quick_sort, merge_sort], 
                           names=["BubbleSort", "SelectionSort", "QuickSort", "MergeSort"],
                           dataset_size=1000)

                
            
