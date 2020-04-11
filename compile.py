#!/usr/bin/python3
import glob, hashlib, json, yaml

bishop_working_dict = {"all": []}
wordlist_working_dict = {"all": []}

files = glob.glob("./sources/**/*.yml", recursive=True)


def bishop_append(path, entry, source_class):
    global bishop_working_dict

    # allow for unvalidate-able patsh to be added to wordlists, but not bishop
    if "validation" not in entry.keys():
        return

    bishop_working_entry = {
        "description": entry["description"],
        "enabled": True,
        "name": entry["title"],
        "risk": "low",
        "searchString": entry["validation"],
        "url": path,
    }

    m = hashlib.md5()
    m.update(json.dumps(bishop_working_entry).encode('utf-8'))
    bishop_working_entry["uid"] = m.hexdigest()

    if source_class not in bishop_working_dict.keys():
        bishop_class_tmp = []
    else:
        bishop_class_tmp = bishop_working_dict[source_class]

    bishop_class_tmp.append(bishop_working_entry)
    bishop_working_dict[source_class] = bishop_class_tmp

def wordlist_append(path, source_class):
    global wordlist_working_dict

    if source_class not in wordlist_working_dict.keys():
        wordlist_class_tmp = []
    else:
        wordlist_class_tmp = wordlist_working_dict[source_class]
    wordlist_class_tmp.append(path)
    wordlist_working_dict[source_class] = wordlist_class_tmp

def add_to_multi_dict(path, entry, source_class):
    bishop_append(path, entry, "all")
    bishop_append(path, entry, source_class)

    wordlist_append(path, "all")
    wordlist_append(path, source_class)


for file_path in files:
    file_components = file_path.split("/")
    source_class = file_components[-2]

    with open(file_path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)

        for recon_path, recon_dict in data_loaded.items():
            add_to_multi_dict(recon_path, recon_dict, source_class)

for bishop_class, bishop_data in bishop_working_dict.items():
    out_file = "./bishop/" + bishop_class + ".json"
    with open(out_file, 'w') as json_target:
        json.dump(bishop_data, json_target, indent=4)

for wordlist_class, wordlist_data in wordlist_working_dict.items():
    out_file = "./wordlists/" + wordlist_class + ".txt"
    wordlist = ""
    for word in wordlist_data:
        wordlist = wordlist + word + "\n"
    wordlist.strip("\n")
    with open(out_file, 'w') as wordlist_target:
        wordlist_target.write(wordlist)