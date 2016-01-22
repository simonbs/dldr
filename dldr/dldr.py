#!/usr/bin/env python
"""DLDR.
Download videos from dr.dk/tv by supplying the URL.

Usage:
  dldr.py <url> [--slug-name] [--output=DIR]
  dldr.py (-h | --help)
  dldr.py --version

Options:
  -h --help                              Show this screen.
  --version                              Show version.
  --slug-name                            Use slug as file name.  E.g. "huset-pa-christianshavn-1" instead of "Huset På Christianshavn (1)"
  -o DIR, --output=DIR                   Output directory for the downloaded file.
"""
from docopt import docopt
from schema import Schema, Use, And, Or
from urllib.request import urlopen
import os
import subprocess
import re
import json

def start_download(stream_url, file_name, output_dir = None):
  subprocess.call(create_command(stream_url, file_name, output_dir), shell=True)

def create_command(stream_url, file_name, output_dir = None):
  output_dir = "." if output_dir == None else output_dir # Use current directory if none
  output_dir = output_dir[:-1] if output_dir.endswith("/") else output_dir # Remove trailing slash
  file_path = "{0}/{1}.mp4".format(output_dir, file_name)
  return "ffmpeg -i \"{0}\" -c copy -absf aac_adtstoasc \"{1}\"".format(stream_url, file_path)
  
def extract_slug_from_url(url):
  # Handle URLs ending with a slash by removing the slash if it exists
  if url.endswith("/"):
    url = url[:-1]
  comps = url.split("/")
  last = comps[-1]
  return re.sub(r"#.*$", "", last)

def get_program_card(slug):
  return perform_api_request("/programcard/%s" % (slug))

def get_asset_link(card):
  assert card["PrimaryAsset"]["Uri"] != None, "Program has no primary asset, i.e. not video, and cannot be downloaded."
  assert card["PrimaryAsset"]["Kind"] == "VideoResource", "Primary asset is not a video."
  manifest = load_json(card["PrimaryAsset"]["Uri"])
  hls_links = [ l for l in manifest["Links"] if l["Target"] == "HLS" ]
  assert len(hls_links) > 0, "Program has no supported streaming link."
  return hls_links[0]["Uri"]

def perform_api_request(path):
  if path.startswith("/"):
    path = path[1:]
  url = "http://www.dr.dk/mu-online/api/1.3/{0}".format(path)
  return load_json(url)

def load_json(url):
  return json.loads(urlopen(url).read().decode("utf8"))

def run():
  args = docopt(__doc__, version="DLDR 1.0")
  s = Schema({
    '--help': bool,
    '--version': bool,
    '<url>': And(Use(str.lower),
                 lambda s: re.search(r"https?:\/\/(www\.)?dr.dk\/tv\/", s),
                 error="URL does not seem to be from DR TV."),
    '--slug-name': bool,
    '--output': Or(os.path.exists, None, error='Output directory does not exist.'),
  })  
  args = s.validate(args)  
  slug = extract_slug_from_url(args['<url>'])
  card = get_program_card(slug)
  stream_url = get_asset_link(card)
  file_name = card['Slug'] if args['--slug-name'] else card['Title']  
  start_download(stream_url, file_name, args['--output'])

if __name__ == "__main__":
  run()
