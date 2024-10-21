def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input_str = input()
    num_str = input_str.split(",")
    num_list = [float(num.strip()) for num in num_str]
    return num_list

def calc_average_tempertature(num_list):
    avg = sum(num_list) / len(num_list)
    return avg

def calc_min_max_temperature(num_list):
    return [min(num_list), max(num_list)]

def sort_temperature(num_list):
    return sorted(num_list)

def calc_median_temperature(num_list):
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list=get_user_input()
    avg_temp = calc_average_tempertature(num_list)
    print ("Average is",avg_temp)
    min_max = calc_min_max_temperature(num_list)
    print (min_max)
    sorted_temps = sort_temperature(num_list)
    print (sorted_temps)
    median_temp = calc_median_temperature(num_list)
    print (median_temp)

if __name__=="__main__":
    main()
