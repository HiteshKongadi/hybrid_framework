from utilities import read_utils

test_invalid_login_data = read_utils.get_csv_as_list("../test_data/Test_invalid_login_data.csv")

# test_employee_data = [
# ("Admin", "admin123", "Peter", "j", "Wick", "Peter Wick", "Peter"),
# ("Admin", "admin123", "John", "J", "Wick", "John Wick", "John")
# ]


test_employee_data = read_utils.get_excel_as_list("../test_data/orange_test_data.xlsx", "test_add_valid_employee")
print(test_employee_data)
