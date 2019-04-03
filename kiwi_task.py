"""Kiwi.com Python weekend Entry task"""

import argparse
import sys
import requests


def city(content):
    """Return name of city"""
    return content["city"]["name"]


def coord(content):
    """Return Latitude and Longitude"""
    return content["location"]["lat"], content["location"]["lon"]


def iata(content):
    """Return IATA code"""
    return content["id"]


def name(content):
    """Return Airport Name"""
    return content["name"]


def return_args():
    """Return all arguments received in command line"""
    parser = argparse.ArgumentParser(
        description="Kiwi.com Python weekend Entry task"
    )

    parser.add_argument("-c", "--cities", help="output cities", action="store_true")
    parser.add_argument("-l", "--coords", help="output coordinates of each airport", action="store_true")
    parser.add_argument("-i", "--iata", help="output IATA codes", action="store_true")
    parser.add_argument("-n", "--names", help="output airport names", action="store_true")
    parser.add_argument("-f", "--full", help="print all details for each airport", action="store_true")

    args = parser.parse_args()

    return args


def return_outputs():
    """Return all output functions for based on arguments received in command line"""
    args = return_args()

    outputs = []
    if args.full:
        outputs += [city, name, iata, coord]
    else:

        if args.cities:
            outputs += [city]

        if args.coords:
            outputs += [coord]

        if args.iata:
            outputs += [iata]

        if args.names:
            outputs += [name]

    if not outputs:
        outputs += [iata, name]

    return outputs


def main():
    """Output data about airports in the United Kingdom based on arguments
    received in command line"""
    outputs = return_outputs()

    default_url = "https://api.skypicker.com"

    url_ending = "/locations?type=subentity&term=GB&location_types=airport&limit=100&sort=name"

    url = default_url+url_ending

    contents = requests.get(url).json()
    for content in contents["locations"]:

        for output in outputs:
            out = output(content)
            sys.stdout.write(str(out) + ", ")

        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
