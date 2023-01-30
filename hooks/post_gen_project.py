import argparse
import os


def main(args):
    os.system('git init')

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
    os.chdir("src/ds-abc")
    os.system('git checkout main && echo main')
    os.chdir("..")

    # The checkout might have left the ds-abc dirty
    os.system("git add ds-abc")
    os.system('git commit -m "Added ds-abc submodule"')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()

    main(args)
