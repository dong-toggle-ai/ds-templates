import os


def cleanup():
    if "{{ cookiecutter.project_type }}" == "library":
        files_excude = [".flake8", ".isort.cfg", ".pre-commit-config.yaml"]
        for file in files_excude:
            os.remove(file)

    import shutil

    for root, subdirs, files in os.walk("."):
        if root[root.rfind("/") + 1 :][0] == "_":
            print(f"Deleting... {root}")
            shutil.rmtree(root)


if __name__ == "__main__":
    cleanup()
