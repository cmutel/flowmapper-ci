import shutil
import typer

def main(input, output):
    shutil.copyfile(input, output)
    return True

if __name__ == '__main__':
    typer.run(main)
