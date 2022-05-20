from datasets import load_dataset

from txtai.app import Application

# Load sample dataset
ds = load_dataset("ag_news", split="train")

# Load txtai application
app = Application("app.yml")

# Index data
for _ in app.workflow("index", ds["text"][0:10000]):
    pass

while True:
    query = input("Enter query: ")
    if query == 'q':
        break

    for result in app.workflow("search", [query]):
        print(result)
        print("------------------------------------------------------------------------------------------------")
        print("-----------------------------------Most similar text -------------------------------------------")
        print(result['data']['Get']['Post'][0]['content'])
        print("------------------------------------------------------------------------------------------------")
