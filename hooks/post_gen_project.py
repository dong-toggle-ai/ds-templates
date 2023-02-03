import os


def submodules():
    os.chdir("{{ cookiecutter.project_slug if cookiecutter.project_type == 'library' else '_' }}")

    # Add ds-packages as submodule
    os.system('git submodule add https://github.com/dong-toggle-ai/ds-packages')
    os.chdir("ds-packages")
    os.system('git checkout main && echo main')
    os.chdir("..")

    # The checkout might have left the ds-packages dirty
    os.system("git add ds-packages")
    os.system('git commit -m "Added ds-packages submodule"')


def cleanup():
    if "{{ cookiecutter.project_type }}" == "library":
        files_excude = [".flake8", ".isort.cfg", ".pre-commit-config.yaml"]
        for file in files_excude:
            os.remove(file)

    import shutil
    for root, subdirs, files in os.walk("."):
        if root[root.rfind("/") + 1:][0] == "_":
            print(f"Deleting... {root}")
            shutil.rmtree(root)

def cmd():
    python_version = "{{ cookiecutter.python_version }}"
    if os.system(f"python{python_version} -m venv ./venv") == 0:
        os.system("curl -sSL https://install.python-poetry.org | python3 -")
        os.system("./venv/bin/poetry install")

        os.system("pre-commit install")


if __name__ == "__main__":
    # os.system('git init')
    # os.system('git branch -m main')
    #
    # if "{{ cookiecutter.dependencies_install_type }}" == "git submodule":
    #     submodules()
    #
    # cmd()
    cleanup()
