"""Prints Hello Coding!"""

def main():
    """The main function that prints Hello Coding!"""
    print("Hello Coding!")

# When we directly execute the file, the __name__ has the value "__main__".
# If the file is inserted as a module, the __name__ will be the name of the module.
# If the file is directly executed, call the main function main()
if __name__ == "__main__":
    main()