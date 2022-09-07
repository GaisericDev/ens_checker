import sys

def filter_ens_names(filter_filepath, list_to_filter):
    # create list from filter_filepath
    not_available = []
    try:
        with open(filter_filepath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                # remove whitespace / newline from each line
                not_available.append(line.strip())
    except Exception as e:
        print(e)
        sys.exit(1)
    # create list that has all items in not_available removed
    filtered_list = [x for x in list_to_filter if x not in not_available]
    return filtered_list