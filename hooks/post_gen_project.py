import os


def cleanup():
    import shutil

    for root, subdirs, files in os.walk("."):
        if root[root.rfind("/") + 1 :][0] == "_":
            print(f"Deleting... {root}")
            shutil.rmtree(root)


if __name__ == "__main__":
    cleanup()
