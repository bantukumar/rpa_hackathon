import json
from collections.abc import Iterable
from google_images_download import google_images_download  # importing the library


def get_keyword_images(keyword, path_to_store_files):
    response = google_images_download.googleimagesdownload()  # class instantiation
    arguments = {'keywords': keyword, 'limit': 2,
                 'output_directory': path_to_store_files}  # creating list of arguments
    paths = response.download(arguments)  # passing the arguments to the function
    urls = []
    for path in paths[0]:
        if isinstance(paths[0], Iterable):
            for url in paths[0][keyword]:
                urls.append(url)

    return json.dumps({'paths': urls})
