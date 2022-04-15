
## About
This is a bunch of scripts I used to prepare D&D spell reference cards for printing. I started with spell data in csv format and ended up with pdf files suited for my particular print provider.

## Prerequisites
- Scribus (I used version 1.5.8)
- a python installation to run the standalone python scripts

## Overview
There main parts of the project are:
- standalone python scripts used to split/manipulate the csv files
- Scribus templates
- and python scripts to be run from inside Scribus to import/export the data

### Standalone python scripts
Those are intended to be run as shell scripts - they accept standard input and output to standard output.
- csv_remove_html
- csv_replace_feet
- csv_split

An example source csv file is provided in raw_input/. It's the same format used e.g. by http://hardcodex.ru card generator.
You can find an example processed csv file in prepared_input/.

### Scribus templates
.sla files.
*_comp* are for spells that have a material component
*_pl* are for polish language templates
*_verte* are two-sided templates for spells with long descriptions

### Scribus scripts
- spells_from_csv is the main one for importing csv data. Have the template you want to use open in Scribus, run it and choose the csv you want to import
- mass_open opens all files from output directory
- mass_export_to_pdf will export all open files to pdf using current export settings (so make sure bleed, crop marks etc. are set correctly)

## TODO:
- fix polish texts for many spells (spelling mistakes,  english ranges)
- make script fill in all level fields in _verte templates
- remove absolute paths in Scribus scripts
- handle polish/english/material components in a more concise manner (merge some templates?)
- handle class colors better
- warning for duplicate spell names in same file?

