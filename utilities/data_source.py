from utilities import read_utils

test_invalid_login_data = read_utils.get_csv_as_list("../test_data/Test_invalid_login_data.csv")

test_employee_data = [
    ("Admin", "admin123", "Peter", "j", "Wick", "Peter Wick", "Peter"),
    ("Admin", "admin123", "John", "J", "Wick", "John Wick", "John")
]


