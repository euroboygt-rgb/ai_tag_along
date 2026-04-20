from functions.run_python_file import run_python_file

def run_tests():
    # 1. Standard run
    print("--- Test 1: Usage ---")
    print(run_python_file("calculator", "main.py"))
    
    # 2. Run with arguments
    print("\n--- Test 2: Arguments ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    
    # 3. Run tests
    print("\n--- Test 3: Internal Tests ---")
    print(run_python_file("calculator", "tests.py"))
    
    # 4. Security check
    print("\n--- Test 4: Security ---")
    print(run_python_file("calculator", "../main.py"))
    
    # 5. Non-existent file
    print("\n--- Test 5: Missing File ---")
    print(run_python_file("calculator", "nonexistent.py"))
    
    # 6. Wrong file type
    print("\n--- Test 6: Wrong Extension ---")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    run_tests()
