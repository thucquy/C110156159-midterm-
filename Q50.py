set1 = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
set1.remove('John')
set1.remove('Tina')
set1.remove('Bert')
set1.remove('Eva')
set1.remove('Bill')
print("英文與數學都及格",set1)
print("數學不及格: {'Bill','John','Tina','Bert'}")

set2 = set(['John','Mary','Fiona','Ben','Bill'])
set2.difference_update(set1)
print("英文及格且數學不及格",set2)




