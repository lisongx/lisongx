# Inspire by Simon Willison's github profile
# https://github.com/simonw
import os
import pathlib
import requests
import datetime
from base64 import b64encode

root = pathlib.Path(__file__).parent.resolve()

GIF = "https://66.media.tumblr.com/9928d0e510741aed0863efeca4fce19b/tumblr_ndsqgsv7331tk1vn4o1_400.gifv"
IMGUR_API = "https://api.imgur.com/3/image"


def upload_image():
    headers = {"Authorization": "Client-ID %s" % os.getenv('IMGUR_CLIENT_ID')}
    print(
        os.system('ls -R /home/runner/work/lisongx/')
    )
    print(
        os.system(['ls -R', os.getenv('GITHUB_WORKSPACE')])
    )

    filepath = os.getenv('GITHUB_WORKSPACE') + 'screenshots/screenshot.png'
    with open(filepath, 'rb') as f:
        img_content = f.read()
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
    content = "# I'm sitting on my Github profile\n![I'm sitting on my Github profile]({image_url})\n![gif]({gif})\n".format(
        gif=GIF, image_url=image_url
    )
    readme.open("w").write(content)
