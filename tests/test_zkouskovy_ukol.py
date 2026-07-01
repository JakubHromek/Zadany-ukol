import os

import xml.etree.ElementTree as ET

from zkouskovy_ukol import save_to_xml_file

def test_xml_file_exists():
    results = [
        {
            "title": "Google",
            "href": "https://google.com",
            "body": "Default google"
        }
    ]
    
    save_to_xml_file(results, "test.xml")

    assert os.path.exists("test.xml")

def test_xml_has_correct_structure():
    results = [
        {
            "title": "Google",
            "href": "https://google.com",
            "body": "Default google"
        }
    ]

    save_to_xml_file(results, "test.xml")

    tree = ET.parse("test.xml")
    root = tree.getroot()

    assert root.tag == "results"
    assert root.find("result/title").text == "Google"
    assert root.find("result/href").text == "https://google.com"
    assert root.find("result/body").text == "Default google"
