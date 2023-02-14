#!/usr/bin/env python3

import requests
import requests_cache
import copy

PIXABAY_API_KEY = "11111111-7777777777777777777777777"

# Create a caching session; this will save HTTP responses
# in a local SQLite database, so that requesting the same
# value a second time will retrieve it from the cache,
# saving time and HTTP requests.
session = requests_cache.CachedSession('fruit_cache')

base_url = "https://pixabay.com/api/"
base_params = {
    "key": PIXABAY_API_KEY,
    "q": "fruit",
    "image_type": "photo",
    "category": "food",
    "safesearch": "true"
}

# We'll fetch 100 images, or however many the API can
# provide for our query, whichever is smaller
images = []
page = 1
while len(images) < 100:
    print(f"Fetching page {page} of query results for '{base_params['q']}'")
    # Fetch this specific page by making a copy of the
    # query parameters and then adding the page number
    this_params = copy.copy(base_params)
    this_params["page"] = page
    response = session.get(base_url, params=this_params)
    # If there are no more hits, break out of the loop
    if not response.json()["hits"]: break
    # go through the results and store them in the images list
    for result in response.json()["hits"]:
        images.append({
            "pageURL": result["pageURL"],
            "thumbnail": result["previewURL"],
            "tags": result["tags"],
        })
    page += 1

html_image_list = [
    f"""<li>
            <a href="{image["pageURL"]}">
                <img src="{image['thumbnail']}" alt="{image["tags"]}">
            </a>
        </li>
    """
    for image in images
]
html_image_list = "\n".join(html_image_list)

# Now make a summary HTML page to show us all the results
# Note that in the CSS we double up the { } characters so
# that they're not interpreted by Python's f-string handler
html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<title>Pixabay search for {base_params['q']}</title>
<style>
ul {{
    list-style: none;
    line-height: 0;
    column-count: 5;
    column-gap: 5px;
}}
li {{
    margin-bottom: 5px;
}}
</style>
</head>
<body>
<ul>
{html_image_list}
</ul>
</body></html>
"""
output_file = f"searchresults-{base_params['q']}.html"
with open(output_file, mode="w", encoding="utf-8") as fp:
    fp.write(html)
print(f"Search results summary written as {output_file}")
