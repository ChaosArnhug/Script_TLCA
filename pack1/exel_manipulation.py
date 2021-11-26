from openpyxl import load_workbook, Workbook


def _copy_data(path_file_data: str, sheet_name: str) -> list:
    """
    Function that make a copy of the data within the exel sample
    :param path_file_data: the path of the exel sample
    :param sheet_name: the exel'sheet where the data is
    :return: A list of a list which contain the data per row
    """
    wb = load_workbook(filename=path_file_data)
    all_rows = []
    for i in range(1, 17):
        curr_row = []
        for j in range(1, 10):
            curr_row.append(wb[sheet_name].cell(row=i, column=j).value)
        all_rows.append(curr_row)
    wb.save(path_file_data)
    return all_rows


def _construct_data(list_data: list, student_data: list, d_201: bool, d_203: bool) -> list:
    """
    Function that complete the unfilled data from the sample
    :param list_data: the sample's data
    :param student_data: the list which contains the data of each student
    :param d_201: Activate the validation of the ability DEV-201
    :param d_203: Activate the validation of the ability DEV-203
    :return: A list of a list which contain the complete data per row
    """
    first_row = True
    for i in range(len(list_data)):
        if first_row:
            first_row = False
            continue
        if student_data[i - 1].is_finished:
            list_data[i][4] = "x"
        else:
            list_data[i][4] = ""

        list_data[i][5] = student_data[i - 1].date

        if student_data[i - 1].result is None:
            list_data[i][6] = ""
            list_data[i][7] = ""
            list_data[i][8] = ""
        else:
            score = round(student_data[i - 1].result)
            list_data[i][6] = str(score) + "%"

            if d_201 and score >= 75:
                list_data[i][7] = "x"

            if d_203 and score >= 75:
                list_data[i][8] = "x"
        i += 1
    return list_data


def _write_data(list_data: list, file_name: str, sheet_name: str):
    """
    Function that write on a new exel the complete data from the evaluation
    :param list_data: The complete data
    :param file_name: The exel file's name
    :param sheet_name:The sheet's name within the exel file
    """
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name
    for i in range(1, 17):
        for j in range(1, 10):
            ws.cell(row=i, column=j).value = list_data[i-1][j-1]
    wb.save(file_name)


def manage_exel(path_file_data: str, sheet_name_origin: str, student_data: list, d_201: bool, d_203: bool,
                file_name_end: str, sheet_name_end: str):
    """
    Execute the copy of the data, the completion of it and the writing into a new exel
    :param path_file_data:the path of the exel sample
    :param sheet_name_origin: the exel'sheet where the data is
    :param student_data: the list which contains the data of each student
    :param d_201:Activate the validation of the ability DEV-201
    :param d_203:Activate the validation of the ability DEV-203
    :param file_name_end: The exel file's name which contain the final data
    :param sheet_name_end: The sheet's name within the exel file
    """
    _write_data(_construct_data(_copy_data(path_file_data, sheet_name_origin), student_data, d_201, d_203),
                file_name_end, sheet_name_end)
