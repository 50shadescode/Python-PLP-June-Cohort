# -----------------------------------------
# File Read & Write Challenge + Error Handling Lab
# -----------------------------------------

# Ask user for a filename (Error Handling Part)
filename = input("Enter the filename to read: ")

try:
    # Try opening the file for reading
    with open(filename, "r") as infile:
        content = infile.read()
        print("\n--- Original File Content ---")
        print(content)

    # Modify the content (File Read & Write Challenge Part)
    # Example modification: convert text to uppercase
    modified_content = content.upper()

    # Write modified content to a new file
    with open("modified_output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("\nFile has been successfully modified and saved as 'modified_output.txt'")

# Handle case where the file does not exist
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

# Handle any other unexpected errors
except Exception as e:
    print(f"An error occurred: {e}")
