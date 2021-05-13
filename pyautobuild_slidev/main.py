#!/usr/bin/env python3

import requests as curl
import subprocess


def getreleasegh():
    owner = 'slidevjs/'
    repo = 'slidev/'
    search = 'tags'
    url = "https://api.github.com/repos/" + owner + repo + search
    with curl.get(url) as r:
        if r.status_code == 200:
            j = r.json()
    release = str(j[0]['name'])
    release = release.replace("v", "").replace(".", "").lstrip('0')
    return release


def getactualimage():
    owner = 'stig124/'
    repo = 'slidev/'
    search = 'tags'
    url = 'https://registry.hub.docker.com/v2/repositories/' + owner + repo + search
    with curl.get(url) as r:
        if r.status_code == 200:
            j = r.json()
    image = str(j['results'][0]['name'])
    image = image.replace(".", "").lstrip('0')
    return image


def checknpm():
    base = 'https://api.npms.io/v2/search?q='
    package = 'slidev'
    url = base + package
    with curl.get(url) as r:
        if r.status_code == 200:
            j = r.json()
    for i in range(5):
        if package in str(j['results'][i]['package']['scope']):
            npm = str(j['results'][i]['package']['version'])
            npm2 = npm.replace(".", "").lstrip('0')
            return npm2, npm


def process(imv, ghv, npv, rv):
    if imv == ghv:
        print("Nothing to do")
        exit(0)
    elif imv < ghv:
        if ghv == npv:
            print("Build")
            cmd = "build_slidev " + rv
            try:
                subprocess.check_call(cmd, shell=True)
            except subprocess.CalledProcessError:
                print("Script failure")
                exit(4)
        else:
            print("Wating for NPM to catch up")
            exit(6)


if __name__ == "__main__":
    imv = getactualimage()
    ghv = getreleasegh()
    npv, rv = checknpm()
    process(imv, ghv, npv, rv)
