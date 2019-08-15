import os
from  utils import clone_github_repo


def clone_github_request():

    user_answer = input('Хотите скачать public repository с GitHub (y/n): ')

    if user_answer in {'Y', 'y', 'ДА', 'Да', 'да', }:
        while True:
            git_rep = get_github_rep_link()
            dir = get_github_clone_dir()
            break

        return {'rep_link': git_rep, 'dir': dir}
    return None


def get_github_clone_dir():
    while True:
        dir = input('Укажите путь к каталогу: ')
        print(f'Указанный путь: "{dir}"')
        if not dir:
            continue
        if os.path.exists(dir):
            print(f'Каталог "{dir}" уже существует')
            continue
        break
    return dir


def get_github_rep_link():
    while True:
        git_rep = input('Укажите https ссылку на рапозиторий: ').rstrip()
        print(f'Вы указали: "{git_rep}"')
        if not git_rep:
            continue
        break
    return git_rep

#
# git_rep = 'https://github.com/zaboevai/missile_comand.git'
# dir = './django'