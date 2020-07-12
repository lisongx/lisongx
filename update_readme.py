# Inspire by Simon Willison's github profile
# https://github.com/simonw
import os
import pathlib
import requests
import datetime
from base64 import b64encode

root = pathlib.Path(__file__).parent.resolve()

IMGUR_API = "https://api.imgur.com/3/image"


def upload_image():
    headers = {"Authorization": "Client-ID %s" % os.getenv('IMGUR_CLIENT_ID')}
    with open('screenshot.png', 'rb') as f:
        img_content = f.read()
        print('image content', len(img_content))
        response = requests.post(
            IMGUR_API,
            headers = headers,
            data = {
                'image': b64encode(img_content),
                'type': 'base64',
                'name': 'screenshot-%s.png' % datetime.datetime.now(),
                'title': 'Picture'
            }
        )
        data = response.json()
        print('response data', data)
        return data['data']['link']


if __name__ == "__main__":
    readme = root / "README.md"
    image_url = upload_image()
    content = "# I'm sitting on my Github profile\n![I'm sitting on my Github profile](%s)" % image_url
    readme.open("w").write(content)
