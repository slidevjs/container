# Slidev Container

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This is the repository for the source of the Docker image for [slidev](https://github.com/slidevjs/slidev) hosted in the [Docker Hub](https://hub.docker.com/r/stig124/slidev)

##### *This is not meant to be a developing environment, it uses only npm-fetched distributions*


## Getting Started <a name = "getting_started"></a>

### Prerequisites

Just have `docker` (or `podman`) installed

### Running

Pull the image :

```bash
$ docker pull stig124/slidev:latest

or

$ podman pull docker.io/stig124/slidev:latest
```

Go into a directory with a `slides.md` file and run it :

```bash
$ docker run --rm -v "$PWD":/root/slides -p 3030:3030 stig124/slidev:latest
```

**WARNING** : Please note that if you have a `node_modules` folder within the folder with the `slides.md` file, It will be **deleted** (You can add `-e KEEP=1` next to `--rm` in the command to revert this behaviour) as it may blocks the starting of the container


You can :

- Run it in the backgroud by adding `-d`
- Change the default port by replacing the left part of the port declaration

### Build

You can also build the image yourself or tinker with it:

```bash
$ git clone https://github.com/slidevjs/container.git
$ cd container
$ docker build -t <tag> .
```

> The tag syntax is as follows `username`/`image_name`:`version`  
> *`username` is mandatory only if you want to push to remote registry*

### LICENSE

This repository is licensed under the MIT license
