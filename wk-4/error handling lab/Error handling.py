try:
    filename = input("Enter a filename: ")  # step 1
    with open(filename, "r") as f:          # step 2
        content = f.read()
        print("File content:\n", content)

except FileNotFoundError:                   # step 3a
    print("Error: The file does not exist.")

except PermissionError:                     # step 3b
    print("Error: You don’t have permission to read this file.")

except Exception as e:                      # step 3c (catch-all)
    print("Something went wrong:", e)
