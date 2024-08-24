import csv


def merge_csv(csv_list, output_path):
    # - build list with all fieldnames
    field_names = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            field_names.extend(f for f in field if f not in field_names)
    
    # write data to output file based on field names
    with open(output_path, 'w', encoding='utf-8', new_line='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=field_names)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)