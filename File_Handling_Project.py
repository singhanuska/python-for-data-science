from pathlib import Path

def fileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(i, item)

def createfile():
    try:
        name = input("Enter your filename: ")
        p = Path(name)
        if not p.exists():
            with open(name, 'x') as f:
                content = input("Enter any content: ")
                f.write(f"{content}\n")
        else:
            print("File already exists")
    except Exception as e:
        print(f"An error occurred: {e}")

def renamefile():
    try:
        name = input("Enter the file to rename: ")
        p = Path(name)
        if p.exists():
            name2 = input("Enter new name: ")
            p.rename(name2)
            print("File renamed successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def readfile():
    fileandfolder()
    try:
        name = input("Enter the file to read: ")
        p = Path(name)
        if p.exists():
            with open(name, 'r') as f:
                content = f.read()
                print(f"Your file contains: {content}")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def appendfile():
    fileandfolder()
    try:
        name = input("Enter the file to append: ")
        p = Path(name)
        if p.exists():
            with open(name, 'a') as f:
                content = input("Enter your content: ")
                f.write(content)
                print("Content appended successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_content():
    fileandfolder()
    try:
        name = input("Enter the file to remove content from: ")
        p = Path(name)
        if p.exists():
            with open(name, 'w') as f:
                f.truncate(0)
                print("Content removed successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

# MAIN PROGRAM LOOP
while True:
    print("\nChoose an option:")
    print("1: Create a file")
    print("2: Rename a file")
    print("3: Read a file")
    print("4: Append to a file")
    print("5:To remove content from a file")
    print("6: Exit")
    try:
        check = int(input("Enter your response: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Loop continues

    if check == 1:
        createfile()
    elif check == 2:
        renamefile()
    elif check == 3:
        readfile()
    elif check == 4:
        appendfile()
    elif check==5:
        remove_content()
    elif check == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
