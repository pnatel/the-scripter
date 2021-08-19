# import libarchive # << unable to import????
import requests
import io
import zipfile
from zipfile import ZipFile
import os
from os.path import basename


# https://techoverflow.net/2018/01/16/downloading-reading-a-zip-file-in-memory-using-python/
def download_extract_zip(url):
    """
    Download a ZIP file and extract its contents in memory
    yields (filename, file-like object) pairs
    """
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield zipinfo.filename, thefile


# -----------UNABLE TO IMPORT LIBRARY---------------
# https://dustinoprea.com/2014/04/17/writing-and-reading-7-zip-from-python/
# def archive_list(filename):
#     '''
#         To enumerate the entries in an archive:
#     '''
#     with libarchive.reader(filename) as reader:
#         for e in reader:
#             # (The entry evaluates to a filename.)
#             print("> %s" % (e))
#     return reader


# def archive_extract(filename):
#     '''
#         To extract the entries from an archive to the current directory
#         (like a normal, Unix-based extraction)
#     '''
#     for state in libarchive.pour(filename):
#         if state.pathname == 'dont/write/me':
#             state.set_selected(False)
#             continue

#         # (The state evaluates to a filename.)
#         print("Writing: %s" % (state))


# def archive_create(name, folder_list):
#     '''
#         To build an archive from a collection of files
#         (omit the target for stdout)
#     '''
#     for entry in libarchive.create('7z', folder_list, name):
#         print("Adding: %s" % (entry))
# -------------------


# ---------------------
# https://thispointer.com/python-how-to-create-a-zip-archive-from-multiple-files-or-directory/

# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName, filter):
    # create a ZipFile object
    with ZipFile(dirName + '/' + zipFileName, 'w') as zipObj:
        # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk(dirName):
            for filename in filenames:
                if filter(filename):
                    # create complete filepath of file in directory
                    filePath = os.path.join(folderName, filename)
                    # Add file to zip
                    zipObj.write(filePath, basename(filePath))


def main():
    print('*** Create a zip file from multiple files  ')
    # create a ZipFile object
    zipObj = ZipFile('sample.zip', 'w')
    # Add multiple files to the zip
    zipObj.write('sample_file.csv')
    zipObj.write('test_1.log')
    zipObj.write('test_2.log')
    # close the Zip File
    zipObj.close()
    
    print('*** Create a zip file from multiple files using with ')
    # Create a ZipFile Object
    with ZipFile('sample2.zip', 'w') as zipObj2:
        # Add multiple files to the zip
        zipObj2.write('sample_file.csv')
        zipObj2.write('test_1.log')
        zipObj2.write('test_2.log')
    
    # Name of the Directory to be zipped
    dirName = 'sampleDir'
    # create a ZipFile object
    with ZipFile('sampleDir.zip', 'w') as zipObj:
        # Iterate over all the files in directory
        for folderName, subfolders, filenames in os.walk(dirName):
            for filename in filenames:
                # create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                # Add file to zip
                zipObj.write(filePath)
    
    print('*** Create a zip archive of only csv files form a directory ***')
    zipFilesInDir('sampleDir', 'sampleDir2.zip', lambda name: 'csv' in name)
# ----------------------------

if __name__ == '__main__':
    main()
