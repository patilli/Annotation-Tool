import json
import random
import pprint

class AnnotationTool:
    def __init__(self) -> None:
        with open('./name_gqa.txt') as f:
            self.objects = f.read().splitlines() 
        with open('./attr_gqa.txt') as f:
            self.attributes = f.read().splitlines() 
        with open('./rel_gqa.txt') as f:
            self.relations = f.read().splitlines() 

    def get_random_samples(self, k=5):
        pprint.pprint(f'Objects:    {random.choices(self.objects ,k=k)}')
        pprint.pprint(f'Attributes: {random.choices(self.attributes ,k=k)}')
        pprint.pprint(f'Predicates: {random.choices(self.relations ,k=k)}')

    def validate_input(self, input):
        pprint.pprint(f'Input in objects:    {input in self.objects}')
        pprint.pprint(f'Input in attributes: {input in self.attributes}')
        pprint.pprint(f'Input in relations:  {input in self.relations}')

def main():
    tool = AnnotationTool()
    while True:
        option = input("Please choose an option: 1) get random samples 2) check if a word is inside the dataset:" )
        if option == '1':
            tool.get_random_samples()
        elif option == '2':
            tool.validate_input(input("Please insert word you want check if it is inside the dataset distribution: "))
        else:
            print('Please input either 1 or 2')

if __name__ == "__main__":
    main()
