import json


def output_to_console(_project, words):
    print('%s: total %s words, %s unique' % (_project, len(words), len(set(words))))
    for word in words.keys():
        print(word)


def save_to_json_file(_project, words):
    json_string = {
        'project':
            {'name': _project,
             'words': {}
             }
    }
    for word, word_count in words.keys():
        json_string['project']['words'][word] = word_count
    with open("data_file.json", "w") as write_file:
        json.dump(json_string, write_file, indent=4)