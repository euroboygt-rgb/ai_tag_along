from functions.write_file import write_file

def run_tests():
    # Test 1: Simple write
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    
    # Test 2: Nested directory write
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    
    # Test 3: Security check
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    run_tests()
