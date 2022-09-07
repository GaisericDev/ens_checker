from english_words import english_words_set
from utils.filter_ens_names import filter_ens_names

def get_ens_names(filter_options):
    # boolean whether or not to filter using an existing file
    use_filter = filter_options["use_filter"]
    filter_file_path = filter_options["filter_filepath"]
    test_list = ["elonmusk.eth", "tesla.eth", "spotify.eth", "fdhfdshmfdjusifd.eth"]
    ens_names = filter_ens_names(filter_file_path, test_list) if use_filter else test_list
    return ens_names