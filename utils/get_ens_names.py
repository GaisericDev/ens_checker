from utils.filter_ens_names import filter_ens_names

def get_ens_names(filter_options):
    use_filter = filter_options["use_filter"]
    filter_file_path = filter_options["filter_filepath"]
    name_list = filter_options["name_list"]
    # filter out non available names from not_available.txt if use_filter = True
    ens_names = filter_ens_names(filter_file_path, name_list) if use_filter else name_list
    return ens_names