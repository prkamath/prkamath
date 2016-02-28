import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timeproject.settings")
django.setup()
from timeprojectapp.models import School,Student


def funcCreateSchools(schoolList):
    for schoolentry in schoolList:
        res=School.objects.filter(name=schoolentry)
        if res:
            print "Entry for " + schoolentry + " exists"
        else:
            s=School(name=schoolentry)
            s.save()
            print "Saved " + schoolentry+" school in table School1"


'''def deleteSchools(schoolToBeDeleted):
    for victimSchool in schoolToBeDeleted:
        s=School1.objects.get(name=victimSchool)
        print s
        s.delete()'''

def funcCreateStudents(studentList):
    for studentName in studentList:
        s=Student(name=studentName)
        s.save()
        print "Saved " + studentName+" name in table Student"

def funcCreateRelnship(schoolStudentList):
        for relnList in schoolStudentList:
            print "Once"
            schoolsName=relnList[1] #This is a list
            studentName=relnList[0]
            schoolObjectList=[]
            for schoolname in schoolsName:
                s=School.objects.filter(name=schoolname)
                if s:
                    schoolObjectList.append(s[0])
                else:
                    sch=School(name=schoolname)
                    sch.save()
                    schoolObjectList.append(sch)
                    print ("Bad value is {}".format(schoolname))
            studObj=Student.objects.get(name=studentName)
            for schoolObj in schoolObjectList:
                studObj.school.add(schoolObj)

def funcStudentsInSchool(schoolName):
    returnset=[]
    schoolObj=School.objects.filter(name=schoolName)
    if (schoolObj):
        studList=schoolObj[0].student_set.all()
        for stud in studList:
            returnset.append(stud.name)
    return returnset


if __name__=="__main__":
    funcCreateSchools(["KVIIsc","KVHebbal","BGSNPS","BlueBells","sdsssds"])
    #funcCreateStudents(["Abhay","Poorvi"])
    funcCreateRelnship([("Abhay",["KVIISc","KVHebbal","KVJ","jalandhar","bhuj"]),("Poorvi",["KVIISc","KVHebbal"])])
    print funcStudentsInSchool("KVIISsssc")
    print "YAAA"
