___author__ = "Jeremy Nelson"

import datetime
import random
import rdflib
import click

import pandas as pd

def rdf_series(graph, subject):
    data = [str(subject)]
    index = ['subject']
    for p,o in graph.predicate_objects(subject=subject):
        # Predicate is added to index
        index.append(str(p))
        # Object is store in data
        data.append(str(o))
    return pd.Series(data, index)

def load_graph(graph):
    data_series = []
    # Loads triples into subject data series
    for subject in set(graph.subjects()):
        data_series.append(rdf_series(graph, subject))
    # For now returns a list, should create data frames for each rdf:type
    return data_series

@click.command()
def interactive():
    start = datetime.datetime.utcnow()
    click.echo(f"Starting RDF interactive samplier at {start}")
    raw_rdf = input("Paste in RDF")
    click.echo("You entered:")
    click.echo(raw_rdf)


if __name__ == "__main__":
    interactive()
