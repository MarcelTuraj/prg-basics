import csv

# Open the CSV file for reading
with open('it_company.csv', mode='r') as file:
    # Create a CSV reader
    csv_reader = csv.DictReader(file)
    
    # Print the header
    print("GRAPHIC DESIGNERS")
    print("=================")
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Check if the job title is 'Graphic Designer'
        if row['Job Title'] == 'Graphic Designer':
            # Print the first name, last name, and email
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
    
