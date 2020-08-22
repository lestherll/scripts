# Scripts
Useful scripts for automating small, everyday tasks. This scripts can be utilised in bigger projects.

## Script Table
The table belows lists the scripts, what they do, and their requirements.

| Script Name                     | Description                                  | Requirements             |
| ------------------------------- | -------------------------------------------- |  ----------------------- |
| [synonyms](synonyms.py)         | this script gets the synonyms of a word      | BeautifulSoup4, requests |
| [antonyms](antonyms.py)         | this script gets the antonyms of a word      | BeautifulSoup4, requests |
| [definition](definition.py)     | this displays the meaning/s of a word        | BeautifulSoup4, requests |
| [download_mp3](download_mp3.py) | downloads mp3 version of videos from youtube | youtube-dl, ffmpeg       |
| [price_checker](price_checker.py) | gives the current price of an amazon product | BeautifulSoup4,requests       |

## Usage


## Potential
I made these scripts with a 'potential' in mind, meaning, they can be extended upon or integrated into bigger projects / systems.

- synonyms.py, antonyms.py, and definition.py can be extended into a **dictionary/thesaurus** project.
- download_mp3.py can be integrated into a **GUI project** for downloading videos from the internet in whatever format. Most of the work is already done by youtube-dl library.
- price_checker.py can be integrated into a **bot project** that will notify you whenever the price of a specific product has gone down.