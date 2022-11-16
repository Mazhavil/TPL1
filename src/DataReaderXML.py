# -*- coding: utf-8 -*-
from lxml import etree

from Types import DataType
from DataReader import DataReader


class DataReaderXML(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as fobj:
            xml = bytes(bytearray(fobj.read(), encoding='utf-8'))
            root = etree.fromstring(xml)
            for student in root.getchildren():
                self.students[student.tag] = []
                for element in student.getchildren():
                    self.students[student.tag].\
                        append((element.tag, int(element.text)))

        return self.students
