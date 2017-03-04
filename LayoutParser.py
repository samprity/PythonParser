import xml.etree.ElementTree as etree
import os
from Type import Activity
from Type import Element

ELEMENT_FILTER = ['Button']

name_space = {
    'android': '{http://schemas.android.com/apk/res/android}',
    'tools': '{http://schemas.android.com/tools}'
}

attrib_info = {
    'id': name_space['android'] + 'id',
    'context': name_space['tools'] + 'context',
    'onClick': name_space['android'] + 'onClick'
}


class LayoutParser:
    def __ParseActivityFile(self, file):
        Activity_TREE = etree.parse(file)
        Activity_ROOT = Activity_TREE.getroot()
        activity_id = Activity_ROOT.attrib.get(attrib_info['id'])
        activity_name = Activity_ROOT.attrib.get(attrib_info['context'])
        activity = Activity(activity_name, activity_id)
        for element in Activity_ROOT:
            if element.tag in ELEMENT_FILTER:
                element_name = element.tag
                element_id = element.attrib.get(attrib_info['id'])
                single_element = Element(id=element_id, name=element_name)
                if attrib_info['onClick'] in element.attrib:
                    single_element.set_callback(element.attrib.get(attrib_info['onClick']))
                activity.add_element(single_element)
        self.Layout.append(activity)

    def GenerateLayoutInfo(self):
        for subdir, dirs, files in os.walk(self.Layout_FOLDER):
            for file in files:
                file_path = subdir + os.sep + file
                if file_path.endswith(".xml"):
                    self.__ParseActivityFile(file_path)
        else:
            return self.Layout

    def __init__(self, Layout_FOLDER):
        self.Layout_FOLDER = Layout_FOLDER
        self.Layout = []
