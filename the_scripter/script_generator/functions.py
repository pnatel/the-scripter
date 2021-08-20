import re
import os
from ..archiver import zipFilesInDir




def load_file_2_list(fname, mode='r') -> list:
    """
        Open SQL script file.

        Args:
            fname (str): File name to open.
        Returns:
            list[str]: List of lines containing substr.

        -----------
        Function selftests:
        >>> len(tty2list('./samples/RAID.Slot.1-1.log'))
        6981
        >>> type((tty2list('./samples/RAID.Slot.1-1.log')))
        <class 'list'>

    """
    with open(fname, mode) as file:
        f_contents = []
        f_contents = file.readlines()  #.decode('utf-16')
        # clean = []
        # for line in f_contents:
        #     clean += line.replace('0xff', 'n')
        #     # print (len(clean), line)
        return f_contents  # clean


def get_lines_with(input_list, substr) -> list:
    """
        Get all lines containing a substring.
        Args:
            input_list [str]: List of string to get lines from.
            substr (str): Substring to look for in lines.
        Returns:
            lines [str]: List of lines containing substr.

        -----------
        Function selftests:
        >>> len(get_lines_with(tty2list('./samples/RAID.Slot.1-1.log'), '11/15/19'))
        746
        >>> type(get_lines_with(tty2list('./samples/RAID.Slot.1-1.log'), '11/15/19'))
        <class 'list'>
    """
    # print (input_list)
    lines = []
    for line in input_list:
        # print ('testing line: ', line)
        if re.search(substr, line, re.IGNORECASE):
            lines.append(line)
            # print ('Line added. size of result: ', len(lines))
    return lines


def get_variables(_list, _except='', var='key_') -> set:
    """
    get_variables AI is creating summary for get_variables

    Parameters
    ----------
    _list : [type]
        [description]
    _except : [type]
        [description]
    var : str, optional
        [description], by default 'key_'

    Returns
    -------
    [type]
        [description]
    """

    res = []
    for item in _list:
        # print("testing item:", item)
        for word in item.split():
            # print("testing word:", word)
            if re.search(var, word, re.IGNORECASE):
                # print(f"word with {var}:", word)
                if _except == '' or _except not in word:
                    res.append(word.replace("'", ""))
                    # print(f'word tested {word}. size of result: ', len(res))
                else:
                    pass
        #  res.append(idx for idx in item.split() if var in idx)  # [0].lower() == var.lower()]
    # remove duplicates before record
    # print(res)
    res.sort()
    res2 = set(res)
    # print(res2)
    return list(res2)


def generateReplacementDict(folder, var='key_', exception="") -> dict:
    values = []
    replacementDict = {}
    for filename in os.listdir(folder):
        if 'output' not in filename:
            fileAsList = load_file_2_list(folder + '/' + filename)
            values = values + get_variables(fileAsList, exception, var)
    for value in values:
        # replacementDict[value[len(var):]] = f'StringField("{value[len(var):]}", [DataRequired()])'
        replacementDict[value.replace(var, "")] = value
    return replacementDict


def script_creation(replacements, template_folder, output_folder,
                    script_suffix):
    # dir_path = os.path.dirname(os.path.realpath(__file__))

    # templateDir = dirPath(dir_path, suffix=template_folder)

    # outDir = dirPath(dir_path, suffix=output_folder)
    # print(templateDir, outDir, outDir.split('/')[-2])

    # for filename in os.listdir(templateDir):
    for filename in os.listdir(template_folder):
        print(filename)
        generateSQLscript(filename, template_folder, output_folder,
                          replacements, script_suffix)
    zipFilesInDir(output_folder, output_folder.split('/')[-2] + '.zip',
                  lambda name: 'sql' in name)
    return output_folder.split('/')[-2] + '.zip'


def generateSQLscript(filename, in_path, out_path, replacement_list,
                      suffix_code):

    if filename.endswith(".sql"):
        # Windows
        # f = open(in_path + '\\' + filename)
        # Linux
        f = open(in_path + '/' + filename)
        query = f.read()
        f.close()

        for key, value in replacement_list.items():
            query = query.replace(key, value)

        os.makedirs(out_path, exist_ok=True)

        fname, file_extension = os.path.splitext(filename)

        f = open(out_path + '/' + fname + '_' + suffix_code + file_extension, 'w')
        f.write(query)
        f.close()


if __name__ == "__main__":
    print(generateReplacementDict("/mnt/c/Users/Paulo.Silva/Nextcloud/Coding/dominos/the-scripter/static/upload_folder/sql12/", var='key_'))
