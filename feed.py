import yaml
import xml.etree.ElementTree as xmlTree

with open('feed.yaml', 'r') as file:
    yamlData = yaml.safe_load(file)

    rssElement = xmlTree.Element('rss', {'version': '2.0',
                                         'xmlns:itunes': 'https://www.itunes.com/dtds/podcast-1.0.dtd',
                                         'xmlns:content': 'https://purl.org/rss/1.0/modules/content/'})

channelElement = xmlTree.SubElement(rssElement, 'channel')

linkPrefix = yamlData['link']

xmlTree.SubElement(channelElement, 'title').text = yamlData['title']
xmlTree.SubElement(channelElement, 'format').text = yamlData['format']
xmlTree.SubElement(channelElement, 'itunes:author').text = yamlData['author']
xmlTree.SubElement(channelElement, 'description').text = yamlData['description']
xmlTree.SubElement(channelElement, 'itunes:image', {'href': linkPrefix + yamlData['image']})
xmlTree.SubElement(channelElement, 'language').text = yamlData['language']
xmlTree.SubElement(channelElement, 'link').text = linkPrefix

xmlTree.SubElement(channelElement, 'itunes:category', {'text': yamlData['category']})

for item in yamlData['item']:
    item_element = xmlTree.SubElement(channelElement, 'item')
    xmlTree.SubElement(item_element, 'title').text = item['title']
    xmlTree.SubElement(item_element, 'itunes:author').text = yamlData['author']
    xmlTree.SubElement(item_element, 'description').text = item['description']
    xmlTree.SubElement(item_element, 'pubDate').text = item['published']
    xmlTree.SubElement(item_element, 'itunes:duration').text = item['duration']

    enclosure = xmlTree.SubElement(item_element, 'enclosure', {
        'url': linkPrefix + item['file'],
        'type': 'audio/mpeg',
        'lenght': item['length']
    })

outputTree = xmlTree.ElementTree(rssElement)
outputTree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
