import os
import collections
import argparse

from utils.word_analyser import get_top_words
from utils.github import clone_github_repo
from utils.console_user_requests import clone_github_request


def print_calc_result(_project, verb_size, words):
    print('%s: total %s words, %s unique' % (_project, len(words), len(set(words))))
    for word, occurence in collections.Counter(words).most_common(verb_size):
        print(word, occurence)


def calc_verbs(_project: str, word_size: int, only_func_names=False, only_verbs=False):
    project_path = os.path.join('.', _project)
    if not os.path.exists(project_path):
        return

    words = get_top_words(project_path, only_func_names=only_func_names, only_verbs=only_verbs)
    if words:
        print_calc_result(project_path, word_size, words)


def console_parser():
    parser = argparse.ArgumentParser(description='Analyze project code by words and verbs.', add_help=True)
    parser.add_argument('path', type=str, default='', help='Path to project')
    parser.add_argument('-fn', action='store_true', help='Calculate words in function names')
    parser.add_argument('-v', action='store_true', help='Calculate verbs')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # TODO Need add some logging

    clone_github_answer = clone_github_request()

    if clone_github_answer:
        print(f'Репозиторий клонируется...')
        clone_github_repo(clone_github_answer['rep_link'], clone_github_answer['dir'])
        print(f'Клонирование успешно завершено!')

    TOP_SIZE = 200

    projects = [
        'django',
        'flask',
        'pyramid',
        'reddit',
        'requests',
        'sqlalchemy',
    ]
    user_answer = input('Провести анализ кода проекта ? (y/n)')
    if user_answer.lower() not in {'y','да'}:
        exit()

    console_args = console_parser()

    print(f'Analyze path={console_args.path}, -fn={console_args.fn}, -v={console_args.v}.')

    if console_args.path:
        projects.clear()
        projects.append(os.path.basename(console_args.path))

    for project in projects:
        calc_verbs(_project=project,
                   word_size=TOP_SIZE,
                   only_func_names=console_args.fn,
                   only_verbs=console_args.v)