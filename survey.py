import sys
from extract import get_input, file_exists

def get_args():
    try:
        return(sys.argv[1])
    except IndexError:
        print("Please provide only 1 argument!\n")
        print("USAGE: [file name]\n")
        raise IndexError
    except:
        print("Unknown Error! See full details below")
        raise


def main():
    filename = get_args() #Get filename for sys arg
    file_exists(filename) # Check if file exists
    mylist = get_input(filename)
    print(mylist)
    #capitalize_name(mylist)



if __name__ == '__main__':
    sys.exit(main())