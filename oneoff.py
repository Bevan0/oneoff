import click
import subprocess
import random
import string
import os

@click.group()
def cli(): pass

@cli.command()
@click.argument("runner")
@click.option("--editor", default="nano")
def run(runner, editor):
    file_name = None
    realrunner = runner
    if runner == "!":
        prevfile = open(f"{os.environ['HOME']}/.config/oneoff-previousfile", "r")
        file_name = prevfile.read().split('\n')[1]
        realrunner = prevfile.read().split('\n')[0]
        prevfile.close()
    elif runner == "EXPORT":
        prevfile = open(f"{os.environ['HOME']}/.config/oneoff-previousfile", "r")
        file_name = prevfile.read().split('\n')[1]
        prevfile.close()

        save_loc = click.prompt("Where do you want to save this? ", type=click.Path())

        if save_loc[0] == "~":
            save_loc = os.environ["HOME"] + save_loc[1:]

        old_file = open(file_name, "r")
        new_file = open(save_loc, "w")
        new_file.write(old_file.read())

        click.echo(f"Saved to {save_loc}")
        return
    else:
        file_name = f"/tmp/oneoff-{''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))}"

    edit = subprocess.run([f"{editor}", f"{file_name}"])
    if (edit.returncode != 0):
        click.echo("Editor returned non-zero error code, quitting")
        return
    
    subprocess.run([f"{realrunner}", f"{file_name}"])

    f = open(f"{os.environ['HOME']}/.config/oneoff-previousfile", "w")
    f.write(f"{runner}\n{file_name}")
