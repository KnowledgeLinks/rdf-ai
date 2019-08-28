___author__ = "Jeremy Nelson"

import datetime
import random
import click

@click.command()
def interactive():
    start = datetime.datetime.utcnow()
    click.echo(f"Starting RDF interactive samplier at {start}")
    raw_rdf = input("Paste in RDF")
    click.echo("You entered:")
    click.echo(raw_rdf)


if __name__ == "__main__":
    interactive()
