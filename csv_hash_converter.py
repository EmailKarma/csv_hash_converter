import csv
import hashlib

def calculate_sha256(data):
    """
    Calculate the SHA-256 hash value for the given data.
    """
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def process_csv(input_file, output_file):
    """
    Read CSV file, calculate SHA-256 hash for each row, and write to new CSV file.
    """
    with open(input_file, 'r', newline='') as csv_input, \
         open(output_file, 'w', newline='') as csv_output:
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)
        
        for row in reader:
            # Calculate SHA-256 hash for the row
            row_data = ','.join(row)
            hash_value = calculate_sha256(row_data)
            
            # Write original data along with hash value to new CSV file
            writer.writerow([hash_value])

if __name__ == "__main__":
    input_file = input("Enter the path and name of the input CSV file: ")
    output_file = input("Enter the path and name of the output CSV file: ")
    
    try:
        process_csv(input_file, output_file)
        print("Conversion completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
