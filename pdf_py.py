import pdfplumber
import pandas as pd

# Function to extract lines containing a specific string
def extract_lines_from_pdf(pdf_path, search_string):
    extracted_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Extract lines containing the search string
                for line in text.splitlines():
                    if search_string.lower() in line.lower():
                        extracted_lines.append(line.strip())
    return extracted_lines

# Main function
if __name__ == "__main__":
    # Ask the user for the PDF file path and string to search
    input_pdf = input("Enter the path to the PDF file: ").strip()
    search_string = input("Enter the string to search for: ").strip()

    # Extract lines from the PDF
    try:
        lines = extract_lines_from_pdf(input_pdf, search_string)
        if lines:
            # Prompt user for the output preference
            print("\nHow would you like to handle the extracted lines?")
            print("1. Save to a CSV file")
            print("2. Print on the screen")
            print("3. Both")
            choice = input("Enter your choice (1/2/3): ").strip()

            # Handle choice
            if choice == "1" or choice == "3":
                output_csv = input("Enter the name for the output CSV file (e.g., output.csv): ").strip()
                df = pd.DataFrame(lines, columns=["Extracted Lines"])
                df.to_csv(output_csv, index=False)
                print(f"Extracted {len(lines)} lines containing '{search_string}' and saved to '{output_csv}'.")

            if choice == "2" or choice == "3":
                print("\nExtracted Lines:")
                for line in lines:
                    print(line)

            if choice not in ["1", "2", "3"]:
                print("Invalid choice. No action taken.")
        else:
            print(f"No lines containing '{search_string}' were found in the PDF.")
    except FileNotFoundError:
        print(f"The file '{input_pdf}' was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")