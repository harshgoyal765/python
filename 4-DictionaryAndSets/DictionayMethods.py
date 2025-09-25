student = {
  "name" : "rahul",
  "subjects" :{
    "math" : 90,
    "science" : 95,
    "english" : 85
  
  }
}

print(student["subjects"]["math"]) #Accessing nested dictionary

print(student.keys()) #Returns all main keys in the dictionary

print(list(student.keys())) #Returns all main keys in the dictionary as a list

print(student.values()) #Returns all values in the dictionary

print(student.items()) #Returns all key-value pairs in the dictionary as a tuple



#mydictionar.get("key") if key not exist then show an error
#mydictionar.get("key") # Returns the value for the specified key, or None if the key does not exist

mydictionary.update(newDict) #inserts the key-value pairs from newDict into mydictionary, overwriting existing keys
