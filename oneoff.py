import click
import subprocess
import random
import string

@click.group()
def cli(): pass

@cli.command()
@click.argument("runner")
@click.option("--editor", default="nano")
def run(runner, editor):
    file_name = f"/tmp/oneoff-{''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))}"
    f = open(file_name, "w")
    f.close()

    edit = subprocess.run([f"{editor}", f"{file_name}"])
    if (edit.returncode != 0):
        click.echo("Editor returned non-zero error code, quitting")
        return
    
    subprocess.run([f"{runner}", f"{file_name}"])

if __name__ == "__main__":
    run()