#!/usr/local/bin/python
#-*- coding: utf-8 -*-

class tester():
    def __init__(self, name: str = "New Tester") -> None:
        self.__tester: str = name
    @property
    def name(self) -> str:
        """The name property. (GET)"""
        return self.__tester
    def sayHi(self) -> None:
        print(f"Hello World!\n\tI'm {self.__tester}")
