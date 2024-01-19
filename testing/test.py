import argparse
import os

from .tools import IOManager, read_file_as_string

parser = argparse.ArgumentParser()
parser.add_argument("--project", type=str, default=None)
parser.add_argument("--save", type=str, default=None)

args = parser.parse_args()

input_path = os.path.abspath(f"{__file__}/../../{args.project}/stream/input.txt")
output_path = os.path.abspath(f"{__file__}/../../{args.project}/stream/{args.save}.txt")
main_path = os.path.abspath(f"{__file__}/../../{args.project}/index.py")
test_file_path = os.path.abspath(f"{__file__}/../{args.project}.test.py")

test_case = IOManager(input_path, output_path)
input = test_case.mock_input()

def build_test_file():
    with open(test_file_path, "w") as file:
        file.write("from .test import input\n\n")
        file.write(read_file_as_string(main_path))
        file.close()

if __name__ == "__main__":
    build_test_file()
    if args.save:
        test_case.toggle_ouput()
        exec(open(test_file_path).read())
        print("\n")
        print(read_file_as_string(main_path))
        test_case.toggle_ouput()
        print(f"Output Printed on {output_path}")
    else:
        exec(open(test_file_path).read())