import re
import urllib.request
import os.path as path
from typing import List
import dataclasses
import json

from bs4 import BeautifulSoup

base_url = "https://apod.nasa.gov/apod/"
LINK_FILE_PATH = "APODImages/image_links.txt"


@dataclasses.dataclass(frozen=True)
class Author:
    name: str
    email: str


@dataclasses.dataclass(frozen=True)
class APODImage:
    title: str
    url: str
    author: Author
    description: str = ""


def get_list_of_apod_urls() -> List[APODImage]:
    response = urllib.request.urlopen("https://apod.nasa.gov/apod/archivepixFull.html")
    soup = BeautifulSoup(response, features="html.parser")
    links = soup.findAll("a", attrs={"href": re.compile("^ap.*\.html$")})
    new_links = []
    for link in links:
        try:
            href = base_url + link.get("href")
            new_page = urllib.request.urlopen(href)
            s2 = BeautifulSoup(new_page, features="html.parser")
            author = get_attribution(s2)
            images = s2.findAll("a", attrs={"href": re.compile(".*jpg$")})
            des = get_description(s2)
            title = link.contents[0]
            for image in images:
                image_href = image.get("href")
                if image_href.startswith("image"):
                    new_url = base_url + image_href
                    new_links.append(
                        APODImage(
                            title=title, url=new_url, description=des, author=author
                        )
                    )
        except Exception as e:
            print(e)
            pass
    return new_links


def get_attribution(s2):
    attrib = s2.find("center").find_next("center").findChild("a").find_next("a")
    attrib_email = attrib.get("href")
    attrib_name = attrib.text
    author = Author(name=attrib_name, email=attrib_email)
    return author


def get_description(s2) -> str:
    paragraphs = s2.findAll("p")
    des = ""
    for p in paragraphs:
        if "Explanation" in p.text:
            des = p.text
            des = des[: des.find("Tomorrow's picture")]
            des = " ".join(des.split()).lstrip("Explanation:").strip()
    return des


def get_apod_links(force=False):
    file_path = path.join(path.dirname(__file__), LINK_FILE_PATH)
    if path.exists(file_path) and (not force):
        with open(file_path, "r") as f:
            as_string = f.read()
        links = json.loads(as_string)
        links = [
            APODImage(
                title=l.get("title"),
                url=l.get("url"),
                description=l.get("description"),
                author=Author(name=l.get("author_name"), email=l.get("author_email")),
            )
            for l in links
        ]
    else:
        links = get_list_of_apod_urls()
        if links:
            with open(file_path, "w") as f:
                f.write(
                    json.dumps(
                        [
                            {
                                "author_name": l.author.name,
                                "author_email": l.author.email,
                                "title": l.title,
                                "url": l.url,
                                "description": l.description,
                            }
                            for l in links
                        ]
                    )
                )
    return links


if __name__ == "__main__":
    get_apod_links(force=True)
