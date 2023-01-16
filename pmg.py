import sys # Get access to the command line arguments

# returns a string of the merged CSVs
def combine_csv(files):
    merged_header = "" # A string of the merged csv header
    merged_csv = [] # An array of strings for the merged csv

    for file in files:
        with open(file) as f: # Open each file from the command line arguments
            
            lines = f.read().split('\n') # get all lines as an array
            
            # seperate header from content using Python destructuring syntax
            header, *lines = lines
            
            # This only has to be done once, but doing it for each file doesn't hurt
            merged_header = header + ',filename'
            
            merged_csv += [line + ',' + file for line in lines if line != ""]
            
            #                                ^ for each line
            #                                                  ^ that isn't empty
            #              ^ join the filename to it
            # ^ and append it to merged_csv

    # take the csv and stringify it in preparation for printing
    merged_content = '\n'.join(merged_csv)

    return merged_header + '\n' + merged_content

def test():
    test1 = combine_csv(['test1_in1.csv', 'test1_in2.csv'])
    with open('test1_ans.csv') as f:
        assert test1 == f.read(), "Failed test #1!"

    test2 = combine_csv(['test2_in1.csv', 'test2_in2.csv', 'test2_in3.csv'])
    with open('test2_ans.csv') as f:
        assert test2 == f.read(), "Failed test #2!"

    return True # All tests passed


if __name__ == '__main__':
    print(combine_csv(sys.argv[1:]))