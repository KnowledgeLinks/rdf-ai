# sample.py splits an incoming XML file into 80/20 training/testing 
___author__ = "Jeremy Nelson"

import datetime
import random
import xml.etree.ElementTree as etree
import click

@click.command()
@click.argument('marc_filepath')
def eighty_twenty(marc_filepath):
    start = datetime.datetime.utcnow()
    click.echo("Starting {} at {}".format(marc_filepath, start))
    training_xml = open("{0}-training.xml".format(marc_filepath), "w+")
    testing_xml = open("{0}-testing.xml".format(marc_filepath), "w+")
    for row in [training_xml, testing_xml]:
        row.write("""<?xml version="1.0" encoding="UTF-8"?><collection xmlns="http://www.loc.gov/MARC21/slim">""") 
    counter = 0
    for action, elem in etree.iterparse(marc_filepath):
        if "record" in elem.tag:
            test = random.random()
            raw_xml = etree.tostring(elem).decode().replace("ns0:", "")
            # An values <= 80 save to training
            if test <= .80:
                training_xml.write(raw_xml)
            else:
                testing_xml.write(raw_xml)
            #if counter > 0 and not counter%100:
            #    click.echo("{:,}".format(counter), nl=False)
            counter += 1
    for row in [training_xml, testing_xml]:
        row.write("</collection>") 
    training_xml.close()
    testing_xml.close()
    end = datetime.datetime.utcnow()
    click.echo("Finished creating training and testing XML files at {}, total time {:,} minutes for {:,} records".format(end, (end-start).seconds / 60.0, counter))   

if __name__ == "__main__":
   eighty_twenty()
