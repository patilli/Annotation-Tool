import json
import random

class AnnotationTool:
    def __init__(self) -> None:
        with open('./data/name_gqa.txt') as f:
            self.objects = f.read().splitlines() 
        with open('./data/attr_gqa.txt') as f:
            self.attributes = f.read().splitlines() 
        with open('./data/rel_gqa.txt') as f:
            self.relations = f.read().splitlines() 
        
        self.obj_to_attr        = json.load(open('./data/obj2attribute.json'))
        self.obj_counts         = json.load(open('./data/obj_counts.json'))
        self.obj_to_attr_counts = json.load(open('./data/obj_to_attr_counts.json'))
        self.pred_to_obj_counts = json.load(open('./data/pred_to_obj_counts.json'))
        self.pred_to_subj_counts = json.load(open('./data/pred_to_subj_counts.json'))

    def get_random_samples(self, k=5):
        print(f'Objects:    {random.choices(self.objects ,k=k)}')
        print(f'Attributes: {random.choices(self.attributes ,k=k)}')
        print(f'Predicates: {random.choices(self.relations ,k=k)}')

    def validate_input(self, input):
        print(f'Input in objects:    {input in self.objects}')
        print(f'Input in attributes: {input in self.attributes}')
        print(f'Input in relations:  {input in self.relations}')
    
    def check_obj_to_attribute(self):
        obj = input("Please insert the object: ")
        attr_list = self.obj_to_attr.get(obj)
        if not attr_list:
            print(f'Object {obj} is not present in the dataset')
        attr = input("Please insert the attribute: ")
        exist = 'exists' if attr in attr_list else 'does not exist'
        print(f'("{obj}", "{attr}") {exist}')
    
    def check_predicate_to_obj(self):
        pred = input("Please insert the predicate: ")
        pred_dict = self.pred_to_obj_counts.get(pred)
        if not pred_dict:
            print(f'Predicate {pred} is not present in the dataset')
            return
        obj  = input("Please insert the object: ")
        exist = 'exists' if obj in list(pred_dict.keys()) else 'does not exist'
        print(f'("{pred}", "{obj}") {exist}')

    def check_predicate_to_subj(self):
        pred = input("Please insert the predicate: ")
        pred_dict = self.pred_to_subj_counts.get(pred)
        if not pred_dict:
            print(f'Predicate {pred} is not present in the dataset')
            return
        subj  = input("Please insert the subject: ")
        exist = 'exists' if subj in list(pred_dict.keys()) else 'does not exist'
        print(f'("{subj}", "{pred}") {exist}')

def main():
    tool = AnnotationTool()
    while True:
        print("Please choose one of the following options: \n1) get random samples \n2) check if a word is inside the dataset \n3) check for an attribute given an object \n4) check for a predicate given an object \n5) check for a predicate given a subject")
        option = input("Option: ")
        if option == '1':
            tool.get_random_samples()
        elif option == '2':
            tool.validate_input()
        elif option == '3':
            tool.check_obj_to_attribute()
        elif option == '4':
            tool.check_predicate_to_obj()
        elif option == '5':
            tool.check_predicate_to_subj()
        else:
            print('Please choose an existing option')
        input("Press any key to start over")
        print('\n\n')

if __name__ == "__main__":
    main()
