try:
    # Open the input file for reading
    with open("readme.md", "r", encoding="utf-8") as infile:
        content = infile.read()
    
    # Modify the content (convert to uppercase in this example)
    modified_content = content.upper()

    # Write the modified content into a new file
    with open("readme_modified.md", "w", encoding="utf-8") as outfile:
        outfile.write(modified_content)

    print(f"Modified file has been saved as 'readme_modified.md'.")

except FileNotFoundError:
    print(f"Error: The file 'readme.md' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
