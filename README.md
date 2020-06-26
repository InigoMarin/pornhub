# PornHub  Video play , The UNIX way

pornhub is a console search and view video program.
It install two programs:

+ pornhub.py
+ pornhub : Bash script to pornhub and pipe programs

## Installation

`sudo make`

## Uninstall

`sudo make clean`

## Program Requeriments

+ **fzf** | **dmenu**
+ **mpv**
+ **xargs**
+ youtube-dl

## Python pip requeriments

+ **pornhub-api**

## Usage

### Dmenu

`pornhub -s <textsearch>`

`pornhub -d -s <textsearch>`

To download video.

### fzf

`pornhub -f -s <textsearch>`

`pornhub -f -d -s <textsearch>`

To download video.


