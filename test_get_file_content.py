from functions.get_file_content import get_file_content

def test():
    print("--- Testing lorem.txt (Truncation) ---")
    res = get_file_content("calculator", "lorem.txt")
    print(f"Result length: {len(res)}")
    if "truncated" in res:
        print("✅ Truncation message found!")

    print("\n--- Testing main.py ---")
    print(get_file_content("calculator", "main.py"))

    print("\n--- Testing Security (Outside Dir) ---")
    print(get_file_content("calculator", "/bin/cat"))

    print("\n--- Testing calcuator.py---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n--- Testing Missing File ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test()
