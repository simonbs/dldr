# dldr

dldr is a tiny command line program for downloading programs from dr.dk/tv. The project is highly inspired by [dldr.brnbw.com](https://github.com/mikker/dldr.brnbw.com) by [@mikker](https://github.com/mikker).

### Installation

You can either download the dldr.py file manually or install it using [Homebrew](http://brew.sh). I recommend the latter.

**Install using Homebrew**

    $ brew tap simonbs/dldr
    $ brew install dldr

**Or install manually**

Copy the dldr.py file to wherever you want it. Install [ffmpeg](http://ffmpeg.org/download.html), [docopt](http://docopt.org) and [schema](https://github.com/keleshev/schema).
 
### Usage

Go to your favorite show on [DR TV](https://www.dr.dk/tv/se/huset-pa-christianshavn/huset-pa-christianshavn-5). Copy the URL. Then run dldr with the URL as an argument.

    $ dldr https://www.dr.dk/tv/se/huset-pa-christianshavn/huset-pa-christianshavn-5

Optionally supply an output directory.

    $ dldr --output ~/Desktop https://www.dr.dk/tv/se/huset-pa-christianshavn/huset-pa-christianshavn-5

By default file name of the programs will be the title of the show, e.g. "Huset på Christianshavn (1)". If you prefer to use the slug as a file name, i.e. "huset-pa-christianshavn-1", supply the `--slug-name` parameter.

For more information, run `$ dldr --help`.