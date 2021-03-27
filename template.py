def read_cases():
    """Function reading test cases and passing it to main
    """
    test_cases = int(input())
    all_data = []
    all_cases = []
    for _ in range(test_cases):
        case_data = list(map(int, input().split(" ")))
        case_array = input()
        all_data.append(case_data)
        all_cases.append(case_array)
    return test_cases, all_data, all_cases

def main(case_data, case):
    """Here goes the actual code to solve the question 
    """
    solution = None
    return solution

if __name__ == "__main__":
    test_cases, all_data, all_cases = read_cases()
    for i in range(test_cases):
        solution = main(case_data=all_data[i], case=all_cases[i])
        print("Case #{}: {}".format(i+1, solution))