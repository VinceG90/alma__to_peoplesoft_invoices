import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml_to_dataframe(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Create a list to hold the parsed data
    data = []

    # Define the namespace
    namespace = {'ns': 'http://com/exlibris/repository/acq/invoice/xmlbeans'}

    # Loop through each 'invoice' element in the XML
    for invoice in root.findall('ns:invoice_list/ns:invoice', namespace):
        # Create a dictionary to hold the data for this invoice
        invoice_data = {}
        for child in invoice:
            if child.tag == '{http://com/exlibris/repository/acq/invoice/xmlbeans}invoice_amount':
                invoice_data['currency'] = child.find('ns:currency', namespace).text
                invoice_data['sum'] = child.find('ns:sum', namespace).text
            else:
                invoice_data[child.tag.split('}')[1]] = child.text

        data.append(invoice_data)

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    return df

# Example usage
xml_file = 'C:\\Users\\vincent.garin\\PycharmProjects\\alma__to_peoplesoft_invoices\\input\\xxx input.xml'  # Replace with your XML file path
df = parse_xml_to_dataframe(xml_file)

# Check if DataFrame is empty
if df.empty:
    print("No data found.")
else:
    print(df)

# Save the DataFrame to a CSV file
    csv_file = 'C:\\Users\\vincent.garin\\PycharmProjects\\alma__to_peoplesoft_invoices\\output\\output.csv'  # Specify your desired output CSV file name
    df.to_csv(csv_file, index=False)  # Save without the index
    print(f"DataFrame saved to {csv_file}")