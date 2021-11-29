import argparse
from pathlib import Path
from pack1.etudiant import *
from pack1.exel_manipulation import *


def argument():
    """Function that manage all the arguments' script"""
    parser = argparse.ArgumentParser()
    parser.add_argument("moodle_CSV_path", help="CSV file with the result")
    parser.add_argument("model_file_path", help="XLSX file which is the model for the final file ")
    parser.add_argument("name_file", help="Name of the final file")
    parser.add_argument("competences_actives", nargs="+", help="Activation of the ability DEV-201")
    return parser.parse_args()


def is_file_extension(path_file: str, extension: str):
    """
    Function that check if the extension of the file is the one we want
    :param path_file: the file's path
    :param extension: the wanted extension
    """
    if not Path(path_file).suffix == extension:
        raise InvalidFileExtension(f"Invalid extension for {path_file}")


if __name__ == "__main__":
    # Activate the argument
    args = argument()
    # Check the extension
    is_file_extension(args.moodle_CSV_path, ".csv")
    is_file_extension(args.model_file_path, ".xlsx")
    # Create the student's list
    student = generate_list_student(args.moodle_CSV_path)
    # Generate the final exel
    manage_exel(args.model_file_path, "Evaluations", student, args.competences_actives, args.name_file, "Evaluations")
