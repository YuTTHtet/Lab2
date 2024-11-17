import Lab2
import statistics

print("Test_Lab2")

num_list = [10,11,45,67]
sorted_list = Lab2.sort_temperature(num_list)

def test_find_min_max():
    test = [min(num_list),max(num_list)]
    result = Lab2.calc_min_max_temperature(num_list)
    assert(result == test)

def test_calc_average():
    test = sum(num_list) / len(num_list)
    result = Lab2.calc_average_tempertature(num_list)
    assert(result == test)

def test_calc_median_temperature():
    test = statistics.median(num_list)
    result = Lab2.calc_median_temperature(num_list)
    assert(result == test)
