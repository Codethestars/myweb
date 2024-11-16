# test_mpage9_verbose.py

from mpage9 import read_data, find_matching_row, DATA_PATH, psychrometric_data

def run_test():
    print(f"1. Checking DATA_PATH value: {DATA_PATH}")
    
    print("\n2. Checking if psychrometric_data was loaded:")
    if psychrometric_data:
        print(f"Data loaded successfully! Number of rows: {len(psychrometric_data)}")
        print("\nFirst 3 rows of loaded data:")
        for i, row in enumerate(psychrometric_data[:3]):
            print(f"Row {i+1}: {row}")
    else:
        print("No data was loaded")
    
    print("\n3. Testing specific lookup:")
    test_temp = 60
    test_humidity = 20
    result = find_matching_row(psychrometric_data, test_temp, test_humidity)
    print(f"Looking for: Temperature = {test_temp}°F, Humidity = {test_humidity}%")
    print(f"Result: {result}")

if __name__ == "__main__":
    print("Starting verbose test of mpage9.py...")
    print("-" * 50)
    try:
        run_test()
    except Exception as e:
        print(f"Error occurred: {type(e).__name__}")
        print(f"Error message: {str(e)}")