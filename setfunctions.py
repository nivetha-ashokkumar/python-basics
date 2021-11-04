thisset = {"python", "c language","c++"}
thisset.add("datastructure")
print(thisset)

thisset = {"python", "c language"}
thisset.remove("python")
print(thisset)

thisset = {"python", "c language"}
newset = {"c++ language"}
thisset.update(newset)
print(thisset)




thisset = {"python", "c language"}
newlist = ["c++ language"]
thisset.update(newlist)
print(thisset)

thisset = {"python", "c language"}
newset = {"c++ language"}
thisset1 = thisset.union(newset)
print(thisset1)

thisset = {"python", "c language"}
newset = {"c++ language","python"}
thisset1 = thisset.intersection(newset)
print(thisset1)
