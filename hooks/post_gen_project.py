import os

def submodules():

    os.chdir("src")
    # Add hello-world as submodule
    os.system('git submodule add https://github.com/dong-toggle-ai/hello-world')
    os.chdir("hello-world")
    os.system('git checkout main && echo main')
    os.chdir("..")

    # The checkout might have left the hello-world dirty
    os.system("git add hello-world")
    os.system('git commit -m "Added hello-world submodule"')

    # Add ds-abc as submodule
    os.system('git submodule add https://github.com/dong-toggle-ai/ds-abc')
    os.chdir("ds-abc")
    os.system('git checkout main && echo main')
    os.chdir("..")

    # The checkout might have left the ds-abc dirty
    os.system("git add ds-abc")
    os.system('git commit -m "Added ds-abc submodule"')


def cmd():

    python_version = "{{ cookiecutter.python_version }}"
    if os.system(f"python{python_version} -m venv ./venv") != 0:
        os.system("source ./venv/bin/activate")
        os.system("pip install -r requirements.txt")

        os.system("pre-commit install")


if __name__ == "__main__":
    os.system('git init')

    if "{{ cookiecutter.dependencies_install_type }}" == "git submodule":
        submodules()

    cmd()
