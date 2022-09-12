# EDA Automation

This project aims to automate the creation of generic figures for simple EDA.

## Table of Contents

<!-- vim-markdown-toc GFM -->

- [Prerequisite](#prerequisite)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [External Data](#external-data)

<!-- vim-markdown-toc -->

## Prerequisite

1. Python 3.10

## Dependencies

Install python libraries,

```sh
pip install -r requirements.txt
```

Installing `Fiona` and `GDAL` might vary across OS and python versions.

## Usage

To generate simple figures,

```sh
python main.py
```

## External Data

The following files are required in `data/` to run scripts in notebooks.

1. [USA region](https://education.nationalgeographic.org/resource/united-states-regions)
2. [USA shapefile](https://www.census.gov/cgi-bin/geo/shapefiles/index.php)

For datasets, extract the zip file to `datasets/`
