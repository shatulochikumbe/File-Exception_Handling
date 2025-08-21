def read_and_write_file():
    # Step 1: Ask the user for the filename
    input_filename = input("Assignment.pdf")

    try:
        # Step 2: Open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Step 3: Modify the content (example: convert text to uppercase)
        modified_content = content.upper()

        # Step 4: Define the new output file name
        output_filename = f"modified_{input_filename}"

        # Step 5: Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Success: Modified content has been written to '{output_filename}'.")

    # Handle if file doesn't exist
    except FileNotFoundError:
        print(f"\n❌ Error: The file '{input_filename}' was not found.")

    # Handle permission error
    except PermissionError:
        print(f"\n❌ Error: Permission denied to read the file '{input_filename}'.")

    # Handle any other unexpected error
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_write_file()
