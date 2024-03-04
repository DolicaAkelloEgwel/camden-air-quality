import feedparser

url = "https://uk-air.defra.gov.uk/assets/rss/current_site_levels.xml"
CAMDEN_STATION_TITLE = "Camden Kerbside"

feed = feedparser.parse(url)

def get_camden_feed(feed):
    for entry in feed["entries"]:
        if entry["title"] == CAMDEN_STATION_TITLE:
            return entry

camden_feed = get_camden_feed(feed)
summary = f"Current{camden_feed['summary'].split('Current')[1]}"
print(summary)
print(camden_feed["published"])