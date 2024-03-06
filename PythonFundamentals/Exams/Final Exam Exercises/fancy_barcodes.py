import re


def parse_barcode(bar: str) -> bool:
    """"
    This function check if a barcode
    is valid or not

    if valid returns: True
    else: False
    """
    regex = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
    result = re.fullmatch(regex, bar)
    if result:
        return True
    return False


# Read User input
num = int(input())
# Loop NUM times to save the barcodes into a list
barcodes = [input() for _ in range(num)]
# Looping through the list
for barcode in barcodes:
    # Parse the barcodes to the func above
    match = parse_barcode(barcode)
    # If the return of the func == True
    if match:
        # Get the numbers from the barcode
        numbers = ''.join(re.findall(r'\d', barcode))
        # If there are not any
        if not numbers:
            numbers = '00'
        print(f'Product group: {numbers}')
    else:
        print('Invalid barcode')