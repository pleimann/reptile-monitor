from os import PathLike
from jinja2 import Environment, FileSystemLoader, select_autoescape

import random
import time

from paho.mqtt import publish as mqtt_publish
from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'


def render_template(filename: PathLike):
  env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
  )

  template = env.get_template(filename)

  rendered = template.render(
    animals=["winnie", "wesley", "waffle", "wilson"]
  )
 
  return rendered


if __name__ == "__main__":
  rendered = render_template("reptile_plate.jsonl.j2")
  with open("h:/openhasp/reptile_plate.jsonl", "w") as file:
    file.write(rendered)

  rendered = render_template("reptile_plate.yaml.j2")
  with open("h:/openhasp/reptile_plate.yaml", "w") as file:
    file.write(rendered)

  mqtt_publish.single("hasp/reptile_plate/command", payload="restart", 
    auth={'username':"controller", 'password':"!QAZ@WSX3edc4rfv"},
    hostname="homeassistant.local", port=1883, client_id=f'python-mqtt-{random.randint(0, 1000)}'
  )
