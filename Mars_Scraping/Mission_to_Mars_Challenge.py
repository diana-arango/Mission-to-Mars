{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c59f427d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "92a257d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 93.0.4577\n",
      "Get LATEST driver version for 93.0.4577\n",
      "Driver [/Users/dianaarango/.wdm/drivers/chromedriver/mac64/93.0.4577.63/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "# Set your executable path\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "# Set up the URL\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "239f8054",
   "metadata": {},
   "outputs": [],
   "source": [
    "### Visit the NASA Mars News Site"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "dc6f2e81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9f57140b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set up the HTML parser:\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "13263ba0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\">NASA's Curiosity Takes Selfie With 'Mary Anning' on the Red Planet</div>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Look for content_title\n",
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "70fbaba5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Curiosity Takes Selfie With 'Mary Anning' on the Red Planet\""
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We want to get the contect_title as text, not with HTML tags or elements combined\n",
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "3147be50",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'The Mars rover has drilled three samples of rock in this clay-enriched region since arriving in July.'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8c9a3361",
   "metadata": {},
   "source": [
    "### JPL Space Images Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "498fc921",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape Mars Data: Featured Image\n",
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "40b2bc09",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "512feff9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "05a73c12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "4a40da2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL. The base URL pops up when finding the relative image url\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3756a1fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 10.3.5 Scrape Mars Data: Mars Facts\n",
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "831bc24e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>Mars</th>\\n      <th>Earth</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Mars - Earth Comparison</th>\\n      <td>Mars</td>\\n      <td>Earth</td>\\n    </tr>\\n    <tr>\\n      <th>Diameter:</th>\\n      <td>6,779 km</td>\\n      <td>12,742 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg</td>\\n      <td>5.97 × 10^24 kg</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2</td>\\n      <td>1</td>\\n    </tr>\\n    <tr>\\n      <th>Distance from Sun:</th>\\n      <td>227,943,824 km</td>\\n      <td>149,598,262 km</td>\\n    </tr>\\n    <tr>\\n      <th>Length of Year:</th>\\n      <td>687 Earth days</td>\\n      <td>365.24 days</td>\\n    </tr>\\n    <tr>\\n      <th>Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n      <td>-88 to 58°C</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert DataFrame into HTML\n",
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c190b152",
   "metadata": {},
   "outputs": [],
   "source": [
    "# End the automated browsing session\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2c92c204",
   "metadata": {},
   "outputs": [],
   "source": [
    "# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "5f943fe1",
   "metadata": {},
   "outputs": [],
   "source": [
    "### Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "102d2d4e",
   "metadata": {},
   "outputs": [
    {
     "ename": "MaxRetryError",
     "evalue": "HTTPConnectionPool(host='127.0.0.1', port=59982): Max retries exceeded with url: /session/53535c4bd23b961cfc8e212e8376a452/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ff2e6ee9670>: Failed to establish a new connection: [Errno 61] Connection refused'))",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mConnectionRefusedError\u001b[0m                    Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    168\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 169\u001b[0;31m             conn = connection.create_connection(\n\u001b[0m\u001b[1;32m    170\u001b[0m                 \u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_dns_host\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mport\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[0;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[1;32m     95\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0merr\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 96\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     97\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[0;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[1;32m     85\u001b[0m                 \u001b[0msock\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msource_address\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 86\u001b[0;31m             \u001b[0msock\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msa\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     87\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0msock\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mConnectionRefusedError\u001b[0m: [Errno 61] Connection refused",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mNewConnectionError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    698\u001b[0m             \u001b[0;31m# Make the request on the httplib connection object.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 699\u001b[0;31m             httplib_response = self._make_request(\n\u001b[0m\u001b[1;32m    700\u001b[0m                 \u001b[0mconn\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[1;32m    393\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 394\u001b[0;31m                 \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mhttplib_request_kw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, body, headers)\u001b[0m\n\u001b[1;32m    233\u001b[0m             \u001b[0mheaders\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"User-Agent\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_get_default_user_agent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 234\u001b[0;31m         \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mHTTPConnection\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    235\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[1;32m   1254\u001b[0m         \u001b[0;34m\"\"\"Send a complete request to the server.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1255\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_send_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1256\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36m_send_request\u001b[0;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[1;32m   1300\u001b[0m             \u001b[0mbody\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_encode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'body'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1301\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mendheaders\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1302\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36mendheaders\u001b[0;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[1;32m   1249\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mCannotSendHeader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_send_output\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage_body\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1251\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36m_send_output\u001b[0;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[1;32m   1009\u001b[0m         \u001b[0;32mdel\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_buffer\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1010\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1011\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, data)\u001b[0m\n\u001b[1;32m    949\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mauto_open\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 950\u001b[0;31m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    951\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    199\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 200\u001b[0;31m         \u001b[0mconn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_new_conn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    201\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_prepare_conn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    180\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mSocketError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 181\u001b[0;31m             raise NewConnectionError(\n\u001b[0m\u001b[1;32m    182\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Failed to establish a new connection: %s\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNewConnectionError\u001b[0m: <urllib3.connection.HTTPConnection object at 0x7ff2e6ee9670>: Failed to establish a new connection: [Errno 61] Connection refused",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mMaxRetryError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-39-5555fa5c68c0>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# 1. Use browser to visit the URL\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0murl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'https://marshemispheres.com/'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36mvisit\u001b[0;34m(self, url)\u001b[0m\n\u001b[1;32m    314\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    315\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mvisit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 316\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    317\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    318\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mback\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mget\u001b[0;34m(self, url)\u001b[0m\n\u001b[1;32m    331\u001b[0m         \u001b[0mLoads\u001b[0m \u001b[0ma\u001b[0m \u001b[0mweb\u001b[0m \u001b[0mpage\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mcurrent\u001b[0m \u001b[0mbrowser\u001b[0m \u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    332\u001b[0m         \"\"\"\n\u001b[0;32m--> 333\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mGET\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m'url'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    334\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    335\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    317\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    318\u001b[0m         \u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_wrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 319\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    321\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/remote_connection.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, command, params)\u001b[0m\n\u001b[1;32m    372\u001b[0m         \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdump_json\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    373\u001b[0m         \u001b[0murl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'%s%s'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_url\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 374\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_info\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    375\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    376\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     26\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_conn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0murllib3\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mPoolManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_timeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 27\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m     21\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mold_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mHTTPException\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mIOError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mOSError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/remote_connection.py\u001b[0m in \u001b[0;36m_request\u001b[0;34m(self, method, url, body)\u001b[0m\n\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkeep_alive\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 397\u001b[0;31m             \u001b[0mresp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_conn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    398\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    399\u001b[0m             \u001b[0mstatuscode\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/request.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, fields, headers, **urlopen_kw)\u001b[0m\n\u001b[1;32m     76\u001b[0m             )\n\u001b[1;32m     77\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 78\u001b[0;31m             return self.request_encode_body(\n\u001b[0m\u001b[1;32m     79\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfields\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfields\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m             )\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/request.py\u001b[0m in \u001b[0;36mrequest_encode_body\u001b[0;34m(self, method, url, fields, headers, encode_multipart, multipart_boundary, **urlopen_kw)\u001b[0m\n\u001b[1;32m    168\u001b[0m         \u001b[0mextra_kw\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    169\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 170\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/poolmanager.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, redirect, **kw)\u001b[0m\n\u001b[1;32m    373\u001b[0m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    374\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 375\u001b[0;31m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mu\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest_uri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    376\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    377\u001b[0m         \u001b[0mredirect_location\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mredirect\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_redirect_location\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    781\u001b[0m                 \u001b[0;34m\"Retrying (%r) after connection broken by '%r': %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mretries\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    782\u001b[0m             )\n\u001b[0;32m--> 783\u001b[0;31m             return self.urlopen(\n\u001b[0m\u001b[1;32m    784\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    785\u001b[0m                 \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    781\u001b[0m                 \u001b[0;34m\"Retrying (%r) after connection broken by '%r': %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mretries\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    782\u001b[0m             )\n\u001b[0;32m--> 783\u001b[0;31m             return self.urlopen(\n\u001b[0m\u001b[1;32m    784\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    785\u001b[0m                 \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    781\u001b[0m                 \u001b[0;34m\"Retrying (%r) after connection broken by '%r': %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mretries\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    782\u001b[0m             )\n\u001b[0;32m--> 783\u001b[0;31m             return self.urlopen(\n\u001b[0m\u001b[1;32m    784\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    785\u001b[0m                 \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    753\u001b[0m                 \u001b[0me\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mProtocolError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Connection aborted.\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    754\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 755\u001b[0;31m             retries = retries.increment(\n\u001b[0m\u001b[1;32m    756\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merror\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_pool\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_stacktrace\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    757\u001b[0m             )\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/retry.py\u001b[0m in \u001b[0;36mincrement\u001b[0;34m(self, method, url, response, error, _pool, _stacktrace)\u001b[0m\n\u001b[1;32m    572\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    573\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_exhausted\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 574\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_pool\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merror\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mResponseError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcause\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    575\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    576\u001b[0m         \u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Incremented Retry for (url='%s'): %r\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mMaxRetryError\u001b[0m: HTTPConnectionPool(host='127.0.0.1', port=59982): Max retries exceeded with url: /session/53535c4bd23b961cfc8e212e8376a452/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ff2e6ee9670>: Failed to establish a new connection: [Errno 61] Connection refused'))"
     ]
    }
   ],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://marshemispheres.com/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "90dad000",
   "metadata": {},
   "outputs": [
    {
     "ename": "MaxRetryError",
     "evalue": "HTTPConnectionPool(host='127.0.0.1', port=59982): Max retries exceeded with url: /session/53535c4bd23b961cfc8e212e8376a452/elements (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ff2e6f2ad00>: Failed to establish a new connection: [Errno 61] Connection refused'))",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mConnectionRefusedError\u001b[0m                    Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    168\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 169\u001b[0;31m             conn = connection.create_connection(\n\u001b[0m\u001b[1;32m    170\u001b[0m                 \u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_dns_host\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mport\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[0;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[1;32m     95\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0merr\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 96\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     97\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[0;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[1;32m     85\u001b[0m                 \u001b[0msock\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msource_address\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 86\u001b[0;31m             \u001b[0msock\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msa\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     87\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0msock\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mConnectionRefusedError\u001b[0m: [Errno 61] Connection refused",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mNewConnectionError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    698\u001b[0m             \u001b[0;31m# Make the request on the httplib connection object.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 699\u001b[0;31m             httplib_response = self._make_request(\n\u001b[0m\u001b[1;32m    700\u001b[0m                 \u001b[0mconn\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[0;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[1;32m    393\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 394\u001b[0;31m                 \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mhttplib_request_kw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, body, headers)\u001b[0m\n\u001b[1;32m    233\u001b[0m             \u001b[0mheaders\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"User-Agent\"\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_get_default_user_agent\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 234\u001b[0;31m         \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mHTTPConnection\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    235\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[1;32m   1254\u001b[0m         \u001b[0;34m\"\"\"Send a complete request to the server.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1255\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_send_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1256\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36m_send_request\u001b[0;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[1;32m   1300\u001b[0m             \u001b[0mbody\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_encode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'body'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1301\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mendheaders\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1302\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36mendheaders\u001b[0;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[1;32m   1249\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mCannotSendHeader\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1250\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_send_output\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage_body\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1251\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36m_send_output\u001b[0;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[1;32m   1009\u001b[0m         \u001b[0;32mdel\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_buffer\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1010\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1011\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/http/client.py\u001b[0m in \u001b[0;36msend\u001b[0;34m(self, data)\u001b[0m\n\u001b[1;32m    949\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mauto_open\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 950\u001b[0;31m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    951\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    199\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 200\u001b[0;31m         \u001b[0mconn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_new_conn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    201\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_prepare_conn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    180\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mSocketError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 181\u001b[0;31m             raise NewConnectionError(\n\u001b[0m\u001b[1;32m    182\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Failed to establish a new connection: %s\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNewConnectionError\u001b[0m: <urllib3.connection.HTTPConnection object at 0x7ff2e6f2ad00>: Failed to establish a new connection: [Errno 61] Connection refused",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mMaxRetryError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-40-87dbcedd359e>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mhemis\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0;31m# Browse through each article\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m     \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlinks\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_by_partial_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Hemisphere'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mhemis\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0;31m# Parse the HTML\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/find_links.py\u001b[0m in \u001b[0;36mfind_by_partial_text\u001b[0;34m(self, partial_text)\u001b[0m\n\u001b[1;32m     27\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_by_partial_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpartial_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 29\u001b[0;31m         return self.parent.find_by_xpath(\n\u001b[0m\u001b[1;32m     30\u001b[0m             \u001b[0;34m'//a[contains(normalize-space(.), \"{}\")]'\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpartial_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m             \u001b[0moriginal_find\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"link by partial text\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36mfind_by_xpath\u001b[0;34m(self, xpath, original_find, original_query, wait_time)\u001b[0m\n\u001b[1;32m    544\u001b[0m         \u001b[0moriginal_find\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moriginal_find\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;34m\"xpath\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    545\u001b[0m         \u001b[0moriginal_query\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0moriginal_query\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mxpath\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 546\u001b[0;31m         return self.find_by(\n\u001b[0m\u001b[1;32m    547\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_elements_by_xpath\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    548\u001b[0m             \u001b[0mxpath\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36mfind_by\u001b[0;34m(self, finder, selector, original_find, original_query, wait_time)\u001b[0m\n\u001b[1;32m    274\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    275\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mend_time\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 276\u001b[0;31m             \u001b[0melem_list\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_find\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mselector\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    277\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    278\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0melem_list\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36m_find\u001b[0;34m(self, finder, selector)\u001b[0m\n\u001b[1;32m    233\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    234\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 235\u001b[0;31m         \u001b[0melements\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfinder\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mselector\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    236\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0melements\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlist\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    237\u001b[0m             \u001b[0melements\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0melements\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_elements_by_xpath\u001b[0;34m(self, xpath)\u001b[0m\n\u001b[1;32m    408\u001b[0m             \u001b[0melements\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_elements_by_xpath\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"//div[contains(@class, 'foo')]\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    409\u001b[0m         \"\"\"\n\u001b[0;32m--> 410\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_elements\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mby\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mXPATH\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mxpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    411\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    412\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_element_by_link_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlink_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mfind_elements\u001b[0;34m(self, by, value)\u001b[0m\n\u001b[1;32m   1003\u001b[0m         \u001b[0;31m# Return empty list if driver returns null\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1004\u001b[0m         \u001b[0;31m# See https://github.com/SeleniumHQ/selenium/issues/4555\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1005\u001b[0;31m         return self.execute(Command.FIND_ELEMENTS, {\n\u001b[0m\u001b[1;32m   1006\u001b[0m             \u001b[0;34m'using'\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1007\u001b[0m             'value': value})['value'] or []\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    317\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    318\u001b[0m         \u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_wrap_value\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 319\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    321\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/remote_connection.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, command, params)\u001b[0m\n\u001b[1;32m    372\u001b[0m         \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdump_json\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    373\u001b[0m         \u001b[0murl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'%s%s'\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_url\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 374\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand_info\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    375\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    376\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     26\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_conn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0murllib3\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mPoolManager\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_timeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 27\u001b[0;31m     \u001b[0;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/splinter/driver/webdriver/remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[0;34m(self, *args, **kwargs)\u001b[0m\n\u001b[1;32m     21\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 23\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mold_request\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mHTTPException\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mIOError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mOSError\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/selenium/webdriver/remote/remote_connection.py\u001b[0m in \u001b[0;36m_request\u001b[0;34m(self, method, url, body)\u001b[0m\n\u001b[1;32m    395\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    396\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkeep_alive\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 397\u001b[0;31m             \u001b[0mresp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_conn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    398\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    399\u001b[0m             \u001b[0mstatuscode\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/request.py\u001b[0m in \u001b[0;36mrequest\u001b[0;34m(self, method, url, fields, headers, **urlopen_kw)\u001b[0m\n\u001b[1;32m     76\u001b[0m             )\n\u001b[1;32m     77\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 78\u001b[0;31m             return self.request_encode_body(\n\u001b[0m\u001b[1;32m     79\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfields\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mfields\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m             )\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/request.py\u001b[0m in \u001b[0;36mrequest_encode_body\u001b[0;34m(self, method, url, fields, headers, encode_multipart, multipart_boundary, **urlopen_kw)\u001b[0m\n\u001b[1;32m    168\u001b[0m         \u001b[0mextra_kw\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    169\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 170\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/poolmanager.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, redirect, **kw)\u001b[0m\n\u001b[1;32m    373\u001b[0m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    374\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 375\u001b[0;31m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mu\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest_uri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    376\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    377\u001b[0m         \u001b[0mredirect_location\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mredirect\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_redirect_location\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    781\u001b[0m                 \u001b[0;34m\"Retrying (%r) after connection broken by '%r': %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mretries\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    782\u001b[0m             )\n\u001b[0;32m--> 783\u001b[0;31m             return self.urlopen(\n\u001b[0m\u001b[1;32m    784\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    785\u001b[0m                 \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    781\u001b[0m                 \u001b[0;34m\"Retrying (%r) after connection broken by '%r': %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mretries\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    782\u001b[0m             )\n\u001b[0;32m--> 783\u001b[0;31m             return self.urlopen(\n\u001b[0m\u001b[1;32m    784\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    785\u001b[0m                 \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    781\u001b[0m                 \u001b[0;34m\"Retrying (%r) after connection broken by '%r': %s\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mretries\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    782\u001b[0m             )\n\u001b[0;32m--> 783\u001b[0;31m             return self.urlopen(\n\u001b[0m\u001b[1;32m    784\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    785\u001b[0m                 \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[1;32m    753\u001b[0m                 \u001b[0me\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mProtocolError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Connection aborted.\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    754\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 755\u001b[0;31m             retries = retries.increment(\n\u001b[0m\u001b[1;32m    756\u001b[0m                 \u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merror\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_pool\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_stacktrace\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    757\u001b[0m             )\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/retry.py\u001b[0m in \u001b[0;36mincrement\u001b[0;34m(self, method, url, response, error, _pool, _stacktrace)\u001b[0m\n\u001b[1;32m    572\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    573\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mis_exhausted\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 574\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_pool\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merror\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mResponseError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcause\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    575\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    576\u001b[0m         \u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Incremented Retry for (url='%s'): %r\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mMaxRetryError\u001b[0m: HTTPConnectionPool(host='127.0.0.1', port=59982): Max retries exceeded with url: /session/53535c4bd23b961cfc8e212e8376a452/elements (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ff2e6f2ad00>: Failed to establish a new connection: [Errno 61] Connection refused'))"
     ]
    }
   ],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "for hemis in range(4):\n",
    "    # Browse through each article\n",
    "    browser.links.find_by_partial_text('Hemisphere')[hemis].click()\n",
    "    \n",
    "    # Parse the HTML\n",
    "    html = browser.html\n",
    "    hemi_soup = soup(html,'html.parser')\n",
    "    \n",
    "    # Scraping\n",
    "    title = hemi_soup.find('h2', class_='title').text\n",
    "    img_url = hemi_soup.find('li').a.get('href')\n",
    "    \n",
    "    # Store findings into a dictionary and append to list\n",
    "    hemispheres = {}\n",
    "    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'\n",
    "    hemispheres['title'] = title\n",
    "    hemisphere_image_urls.append(hemispheres)\n",
    "    \n",
    "    # Browse back to repeat\n",
    "    browser.back()\n",
    "\n",
    "# Quit browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "3387adfa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "726f1c18",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
