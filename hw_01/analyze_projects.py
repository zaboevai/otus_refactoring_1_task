import os
import collections

from utils.output import output_to_console, save_to_json_file
from utils.word_analyser import get_top_words
from utils.github import clone_github_repo
from utils.console import clone_github_request, console_parser


def calc_words_in_project(_project: str, word_size: int, only_func_names=False, only_verbs=False, to_json=False):
    project_path = os.path.join('.', _project)
    if not os.path.exists(project_path):
        return

    top_words = get_top_words(project_path, only_func_names=only_func_names, only_verbs=only_verbs)
    if top_words:
        words = {}
        for word, occurence in collections.Counter(top_words).most_common(word_size):
            words[word] = occurence

        if to_json:
            save_to_json_file(_project, words)
        else:
            output_to_console(_project, words)


if __name__ == '__main__':
    # TODO Need add some logging

    TOP_SIZE = 200

    projects = [
        'django',
        'flask',
        'pyramid',
        'reddit',
        'requests',
        'sqlalchemy',
    ]

    console_args = console_parser()

    if console_args.path:
        projects.clear()
        projects.append(os.path.basename(console_args.path))

    user_answer = input('Провести анализ кода проекта ? (y/n)')

    if user_answer.lower() not in {'y', 'да'}:
        exit()

    clone_github_answer = clone_github_request()

    if clone_github_answer:
        print(f'Репозиторий клонируется...')
        clone_github_repo(clone_github_answer['rep_link'], clone_github_answer['dir'])
        print(f'Клонирование успешно завершено!')

    for project in projects:
        calc_words_in_project(_project=project,
                              word_size=TOP_SIZE,
                              only_func_names=console_args.fn,
                              only_verbs=console_args.v,
                              to_json=console_args.j,)
