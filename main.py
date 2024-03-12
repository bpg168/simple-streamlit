import json
import streamlit as st


# File storage

class SimpleFileDB:

    def __init__(self):
        self.myfile = "data.json"

    def add(self, row: str):
        with open(self.myfile, "r") as fp:
            all_data = json.load(fp)
            all_data.append(row)

        with open(self.myfile, "w") as fp:
            json.dump(all_data, fp)

    def search(self, substr: str):
        with open(self.myfile, "r") as fp:
            rows = json.load(fp)

            for row in rows:
                if substr in row:
                    return row

            return "Not Found"

    def printall(self):
        with open(self.myfile, "r") as fp:
            all_data = json.load(fp)
            for row in all_data:
                st.write(row)


# Main app

st.title("Simple string storage app")
mystr = st.text_input("Enter string to storage", key="mystr")
go_button = st.button("Store")

search_substr = st.text_input("Substring to search", key="substr")
search_button = st.button("Search")

db = SimpleFileDB()


if go_button:
    # here you will take care of scrapping permissions etc.
    # store permission info to bigquery directly
    db.add(mystr)
    db.printall()


if search_button:
    res = db.search(search_substr)
    st.write(f"Your result is: {res}")
