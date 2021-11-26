from datetime import datetime


class InvalidFileExtension(Exception):
    pass


class Student:
    def __init__(self, surname: str, firstname: str, date, is_finished: bool = True, result: float = None):
        """
        The constructor of the class Student
        :param surname: the student' surname
        :param firstname: the student's firstname
        :param date: the date of the evaluation
        :param is_finished: the status of the evaluation
        :param result: the score of the evaluation
        """
        self.__surname = surname
        self.__firstname = firstname
        self.__date = str(date)
        self.__is_finished = is_finished
        self.__result = result

    @property
    def surname(self):
        return self.__surname

    @property
    def firstname(self):
        return self.__firstname

    @property
    def date(self):
        return self.__date

    @property
    def is_finished(self):
        return self.__is_finished

    @property
    def result(self):
        return self.__result

    @date.setter
    def date(self, new_date):
        self.__date = new_date

    @result.setter
    def result(self, new_result):
        self.__result = new_result


def _is_finished(status: str) -> bool:
    """
    Function that check if a test is finished
    :param status: the current state of the evaluation
    :return: true if the test is finished, false otherwise
    """
    return status == "Finished"


def _results(status: bool, total=None):
    """
    Function that manage the student's result
    :param status: the status of the student's test (finished or not)
    :param total: the student score (if he finished)
    :return:
    """
    if status:
        return float(total)*10
    return None


def new_student(list_student: list, surname: str, firstname: str, date, is_finished: bool = True, result: float = None):
    """
    Function that check if a student exist within a list
    :param list_student: the list witch contain all the students
    :param surname: the student' surname
    :param firstname: the student's firstname
    :param date: the date of the evaluation
    :param is_finished: the status of the evaluation
    :param result: the score of the evaluation
    :return: a list with a new student if he didn't exist before or a list with an update on student that was already
    within the list
    """
    for student in list_student:
        if student.surname == surname and student.firstname == firstname and is_finished and student.result < result:
            student.date = str(date)
            student.result = result
            return list_student

    return list_student.append(Student(surname, firstname, date, is_finished, result))


def generate_list_student(path_data_file: str) -> list:
    """
    Function that generate a list of Student object
    :param path_data_file: the file's path which contain the data
    :return: list of Student object
    """
    student_list = []
    try:
        with open(path_data_file) as file:
            first_line = True
            for line in file:
                # Skip first line
                if first_line:
                    first_line = False
                    continue
                # Whole data for each student
                students = line.strip().split(";")
                # separation of the data into a list + adaptation of the raw data to fit the wanted objective
                surname = students[0]
                firstname = students[1]
                state = _is_finished(students[2])
                date = datetime.strptime(students[3], "%d %B %Y %I:%M %p")
                result = _results(state, students[6])
                # add a student if he didn't exist within the list or update the students if the score is better
                new_student(student_list, surname, firstname, date, state, result)
    except FileNotFoundError:
        print("File not found")

    return student_list
