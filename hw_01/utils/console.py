import argparse
import os


def clone_github_request():
    user_answer = input('Хотите скачать public repository с GitHub (y/n): ')

    if user_answer.lower() not in {'y', 'да', }:
        return None

    while True:
        git_rep = get_github_rep_link()
        if git_rep:
            dir = get_github_clone_dir()
            if dir:
                return {'rep_link': git_rep, 'dir': dir}
        break
    return None


def get_github_clone_dir():
    while True:
        dir = input('Укажите путь к каталогу: ')
        print(f'Указанный путь: "{dir}"')

        if dir:
            if os.path.exists(dir):
                print(f'Каталог "{dir}" уже существует')
                continue
            break

        if is_continue_question():
            continue
        return None

    return dir


def get_github_rep_link():
    while True:
        git_rep = input('Укажите https ссылку на рапозиторий: ')
        print(f'Вы указали: "{git_rep.rstrip()}"')

        if git_rep:
            break

        if is_continue_question():
            continue

        return None

    return git_rep.rstrip()


def is_continue_question():
    answer = input('Ошибка! Продолжить (y/n): ')
    return answer.lower() in {'y', 'да'}


if __name__ == '__main__':
    # git_rep = 'https://github.com/zaboevai/missile_comand.git'
    # dir = 'django'
    user_answer = clone_github_request()
    print(user_answer)


def console_parser():
    parser = argparse.ArgumentParser(description='Analyze project code by words and verbs.', add_help=True)
    parser.add_argument('path', type=str, default='', help='Path to project')
    parser.add_argument('-fn', action='store_true', help='Calculate words in function names')
    parser.add_argument('-v', action='store_true', help='Calculate verbs')
    args = parser.parse_args()
    print(f'Analyze path={args.path}, -fn={args.fn}, -v={args.v}.')
    return args