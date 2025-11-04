# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   *I have not given or received any unauthorized aid on this assignment."
#
# Name:       Ethan Mikolaycik
# Section:    563
# Assignment: Print Math 
# Date:       8/27/2025

# split barcodes
def split_barcode(barcode: str):
    group1 = []
    group2 = []
    last_digit = int(barcode[-1])
    for idx, val in enumerate(barcode[:-1]):
        if idx % 2 == 0:
            group1.append(val)
        else:
            group2.append(val)
            
    group1 = [int(v) for v in group1]
    group2 = [int(v) for v in group2]

    last = str(sum(group2) * 3 + sum(group1))[-1]
    return (10 - int(last)) == last_digit

def read_write_valid_barcodes(barcodes_path: str, valid_barcodes_path: str):
    valid_barcodes = ""
    count = 0
    with open(barcodes_path, "r") as f:
        for line in f:
            barcode = line.strip()
            if split_barcode(barcode): 
                count += 1
                valid_barcodes += line

    with open(valid_barcodes_path, "w") as f:
        f.write(valid_barcodes)

    return count

barcodes_path = input("Enter the name of the file: ")
valid_barcodes_path = "valid_barcodes.txt"

c = read_write_valid_barcodes(barcodes_path, valid_barcodes_path)
print(f"There are {c} valid barcodes")