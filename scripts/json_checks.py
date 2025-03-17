path = 'assets\\ssbrc\\lang\\'
ext = '.json'

def read_lang_file(file_path):
    '''Reads a lang file and returns a list of tuples (key, value).'''
    lang_dict = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:  # Ensure it's a valid key-value pair
                key, value = line.split(':', 1)
                key = key.strip().strip('"').lower()  # Clean up the key and normalize case
                line = line.strip()  # Strip extra spaces from the line
                lang_dict.append((key, line))  # Keep both key and line
    return lang_dict

def compare_file_lengths(file1_lines, file2_lines):
    '''Check if both files have the same number of lines and point out any deviations.'''
    len_file1 = len(file1_lines)
    len_file2 = len(file2_lines)

    if len_file1 != len_file2:
        print(f'JSYNC failed; lang files not copied.')
        print(f'  >> Reason: File lengths do not match ({len_file1} vs {len_file2})')

        # Find the first line where one file is missing compared to the other
        min_len = min(len_file1, len_file2)
        for i in range(min_len):
            if file1_lines[i][0] != file2_lines[i][0]:  # Compare keys
                print(f'    >> Deviation starts at line {i + 2}.\n')
                return False

        print(f'    >> File length deviation starts at line {min_len + 1}.')
        return False

    print('JSYNC check 1 success: File lengths match.')
    return True

def compare_keys_in_same_positions(file1_lines, file2_lines):
    '''Check if the keys in both files are in the same positions and show deviations.'''
    for i, ((key1, value1), (key2, value2)) in enumerate(zip(file1_lines, file2_lines)):
        # Strip spaces from the lines and normalize case for comparison
        if key1 != key2 or value1.strip().lower() != value2.strip().lower():
            print(f'JSYNC failed; lang files not copied.')
            print(f'  >> Reason: Difference found at line {i + 2}')
            print(f'    >> File 1: \'{key1}\': \'{value1}\'')
            print(f'    >> File 2: \'{key2}\': \'{value2}\'')

            return False
    print('JSYNC check 2 success: Keys and values are in the same positions.')
    return True

def compare(file1_path, file2_path):
    '''Compares two lang files for line count and key positions.'''
    print()

    file1_lines = read_lang_file(file1_path)
    file2_lines = read_lang_file(file2_path)

    # 1. Compare file lengths
    if not compare_file_lengths(file1_lines, file2_lines):
        return False

    # 2. Compare keys and their positions
    if not compare_keys_in_same_positions(file1_lines, file2_lines):
        return False

    print('JSYNC passed; lang files successfully copied.')
    return True
