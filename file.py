# File Read & Write Challenge
def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ File has been modified and saved to {output_file}")

    except FileNotFoundError:
        print(f"❌ The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


# Example usage
modify_file("input.txt", "output.txt")
