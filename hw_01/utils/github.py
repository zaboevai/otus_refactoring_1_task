from git import Repo


def clone_github_repo(repo_path, dir_path):
    """
    Clone GITHUB repositories to dir
    :param repo_path:
    :param dir_path:
    :return:
    """
    Repo.clone_from(url=repo_path, to_path=dir_path)