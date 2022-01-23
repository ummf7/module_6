<<<DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY>>>
Student IO: 1007
First Name: Thorin
Last Name: Fields

doc = db.collection_name.find_one({“student_id”: “1010”})
 
 Student IO: 1010
First Name: Thorin
Last Name: Fields

doc. = db.collection_name.delete_one({"student_id": "1010"})
Student IO: 
First Name: Thorin
Last Name: Fields
