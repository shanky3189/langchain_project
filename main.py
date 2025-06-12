import pandas as pd
import os,sys
import numpy as np

print("Hello World..!")
print("This is my branch1..!")
print("I have added this new line in branch1")

#Read a text file and fetch the content into a string variable
def read_file(file_path):
    """Reads a text file and returns its content as a string."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content


file_path=r'C:\Users\Shash\MyStudy\Langchain_git_learning\langchain_project\data\MyData.txt'
content=read_file(file_path)
print(content)