from src.annotation_tool import AnnotationTool

def main():
    tool = AnnotationTool()
    while True:
        #print("Please choose one of the following options: \n1) get random samples \n2) check if a word is inside the dataset \n3) check for an attribute given an object \n4) check for a predicate given an object \n5) check for a predicate given a subject")
        print("Please choose one of the following options: \n1) get random samples \n2) check if a word is inside the dataset \n3) check for body parts that should be excluded")
        option = input("Option: ")
        if option == '1':
            tool.get_random_samples()
        elif option == '2':
            tool.validate_input()
        # elif option == '3':
        #     tool.check_obj_to_attribute()
        # elif option == '4':
        #     tool.check_predicate_to_obj()
        # elif option == '5':
        #     tool.check_predicate_to_subj()
        else:
            print('Please choose an existing option')
        input("Press any key to start over")
        print('\n\n')

if __name__ == "__main__":
    main()
