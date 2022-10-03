SELECT Name,Gender,Weight,Height FROM Student 
LEFT OUTER JOIN StudentHealthRecord ON Student.StudentID = StudentHealthRecord.StudentID
ORDER BY Gender ASC,Name DESC 

