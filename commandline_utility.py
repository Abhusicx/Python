import argparse

parser = argparse.ArgumentParser()

#add command line arguments
parser.add_argument("url",help = "Url of the file to download")
parser.add_argument("output", help="by which name do you want to save your file")

#parse the arguments
args = parser.parse_args()


#use the argument in your code
print(args.url)
print(args.output)