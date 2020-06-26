#!/usr/bin/env python3
# encoding: utf-8

from pornhub_api import PornhubApi
import npyscreen as np

api = PornhubApi()

def search(text):
    data = api.search.search(
    text,
    ordering="mostviewed",
    period="weekly",)
    for vid in data.videos:
        print(vid.title, vid.url)

class ResultForm(np.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        self.add(np.TitleText, name = "Name:",)
        self.add(np.TitleText, name = "Dept:")
        self.add(np.TitleText, name = "Employed:")


    def on_cancel(self):
        self.parentApp.switchFormPrevious()


class SearchForm(np.Form):
    def create(self):
        self,self.add(np.TitleText, name = "Search:" , value = self.parentApp.search)
        self.add(np.TitleSelectOne, max_height=4, value = [1,], name="Period:",
                values = ["monthly","alltimes"], scroll_exit=True)

    def afterEditing(self):
        self.parentApp.setNextForm("RESULT")

class MyTestApp(np.NPSAppManaged):

    search = None

    def onStart(self):
        self.addForm('MAIN', SearchForm, name='Search PornHub')
        self.addForm('RESULT', ResultForm, name='Result PornHub')

# This form class defines the display that will be presented to the user.



if __name__ == '__main__':
    MyTestApp().run()

