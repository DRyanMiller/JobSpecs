!pip install PyPDF2
import PyPDF2
import re
import json

pdf = '/Users/dryanmiller/Desktop/Account Consultant.pdf'

class Iowa():
    state = 'Iowa'
    

    def __init__(self, file_path):
        self.filename = self.get_FileName(file_path)
        self.text = self.extract_text()
        self.id = self.get_ID()
        self.title = self.get_Title()
        self.description = self.get_Description()
        self.competencies = self.get_Competencies()
        self.education = self.get_Education()
        self.effective_date = self.get_EffectiveDate()
    

    def get_FileName(self, file_path):
        filename = re.split('/', file_path)
        filename = filename[-1]
        filename = re.search('(.*).pdf$', filename).group(1).strip()
        return filename


    def extract_text(self):
        pdfFileObj = open(pdf, 'rb') 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        pageObj = pdfReader.getPage(0) 
        pageObj.extractText()
        full_text = []
        for i in range(pdfReader.getNumPages()):
                pageObj = pdfReader.getPage(i)
                text = pageObj.extractText()
                text = text.replace('\n', '', -1)
                full_text.append(text)
        text = ' '.join(full_text).lower()
        return text


    def get_ID(self):
        ID = re.search('[0-9][/0-9]*', self.text).group(0).strip()
        return ID


    def get_Title(self):
        Title_string = re.search('human resources enterprise(.*)definition', self.text)
        Title = Title_string.group(1).strip()
        return Title


    def get_Description(self):
        Description_string = re.search('definition(.*)(the work examples)', self.text)
        Description = Description_string.group(1).strip()
        return Description


    def get_Competencies(self):
        Competencies_string = re.search('competencies required(.*)education, experience', self.text)
        Competencies = Competencies_string.group(1).strip()
        Competencies_list = Competencies.split('.')
        return Competencies_list


    def get_Education(self):
        Education_string = re.search('education, experience, and special requirements(.*)effective date', self.text)
        if Education_string == None:
                Education_string = re.search('minimum qualification requirements(.*)effective date', self.text)
                Education = Education_string.group(1).strip()
        else:
                Education = Education_string.group(1).strip()
        return Education


    def get_EffectiveDate(self):
        EffectiveDate_string = re.search('effective date(.*)([0-9][0-9]/[0-9]+)', self.text)
        EffectiveDate = EffectiveDate_string.group(2).strip()
        return EffectiveDate

test = Iowa(pdf)

test.__dict__

s = json.dumps(test.__dict__)

type(s)