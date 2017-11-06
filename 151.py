import MySQLdb

con = MySQLdb.connect(host='localhost',user='root',passwd='password271997',db='sakila')
sql = con.cursor()

add = "add"
view = "view"
search = "search"
delete = "delete"
update = "update"
tables = "Student"

class Student:

	def __init__(self,idnum,course,fname,mname,lname):
		self.idnum = idnum
		self.course = course
		self.fname = fname
		self.mname = mname
		self.lname = lname

def createTable(tables):
	sql.execute("CREATE TABLE IF NOT EXISTS tables(idnum TEXT, course TEXT, fname TEXT, mname TEXT, lname TEXT)")


def add(sdata):
	sql.execute("INSERT INTO tables(idnum,course,fname,mname,lname) VALUES(%s,%s,%s,%s,%s)"
				,(sdata.idnum,sdata.course,sdata.fname,sdata.mname,sdata.lname))

	con.commit()

def prints():
	sql.execute('SELECT * FROM tables ORDER BY idnum ASC')
	for row in sql.fetchall():
		print row

def search():
	idnum1 = raw_input("Enter id number: ")
	sql.execute("SELECT * FROM tables where idnum = %s", (idnum1,))
	for row in sql.fetchall():
		print row

def delete():
	del1 = raw_input("Enter id number: ")
	sql.execute("DELETE from tables where idnum = %s", (del1,))
	con.commit()

def update():
	idnum1 = raw_input("Enter id number: ")
	update3 = 1
	while(update3 == 1):
		print "\nWhat do you want to update?"
		print "1. first name"
		print "2. middle name"
		print "3. last name"
		print "4. course"
		choice = input("Input the corresponding number of your choice: ")

		if choice == 1:
			newfname = raw_input("Enter first name: ")
			con.execute("UPDATE tables set fname = %s where idnum = %s", (newfname,idnum1))
			con.commit()
		elif choice == 2:
			newmname = raw_input("Enter middle name: ")
			con.execute("UPDATE tables set mname = %s where idnum = %s", (newmname,idnum1))
			con.commit()
		elif choice == 3:
			newlname = raw_input("Enter last name: ")
			con.execute("UPDATE tables set lname = %s where idnum = %s", (newlname,idnum1))
			con.commit()
		elif choice == 4:
			newcourse = raw_input("Enter course: ")
			con.execute("UPDATE tables set course = %s where idnum = %s", (newcourse,idnum1))
			con.commit()

		updateAgain = raw_input("\nWant to change another thing from this student?(yes or no): ")
		if updateAgain == "No" or updateAgain == "no" or updateAgain == "NO":
			update3 = 0

def main():
	createTable(tables)
	loop = 1
	while(loop == 1):
		print "\tSTUDENT DATABASE"
		print "\n"
		print "What do you want to do?"
		print "* add"
		print "* view"
		print "* search"
		print "* delete"
		print "* update"
		choice2 = input("Select from the options above: ")
		print "\n"
			
		if choice2 == add:
			add1 = 1
			while(add1 == 1):
				
				idnum1 = raw_input("Enter id number: ")
				course = raw_input("Enter course: ")
				fname = raw_input("Enter first name: ")
				mname = raw_input("Enter middle name: ")
				lname = raw_input("Enter last name: ")
				sdata = Student(idnum1,course,fname,mname,lname)

				add(sdata)
				
				add2 = raw_input("Do you want to add more?(yes or no): ")
				if add2 == "no" or add2 == "NO" or add2 == "No":
					add1 = 0

		elif choice2 == view:
			prints1 = 1
			while (prints1 == 1):
				prints()
				prints2 = raw_input("Do you want to view more?(yes or no): ")
				if prints2 == "no" or prints2 == "NO" or prints2 == "No":
					prints1 = 0

		elif choice2 == search:
			search1 = 1
			while (search1 == 1): 
				search()
				search2 = raw_input("Do you want to search more?(yes or no): ")
				if search2 == "no" or search2 == "NO" or search2 == "No":
					search1 = 0

		elif choice2 == delete:
			delete1 = 1
			while (delete1 == 1):
				delete()
				delete2 = raw_input("Do you want to delete more?(yes or no): ")
				if delete2 == "no" or delete2 == "NO" or delete2 == "No":
					delete1 = 0

		elif choice2 == update:
			update1 = 1
			while (update1 == 1):
				
				update()

				update2 = raw_input("\nDo you want to update more?(yes or no): ")
				if update2 == "no" or update2 == "NO" or update2 == "No":
					update1 = 0

		loop1 = raw_input("\nDo you want to try another option?(yes or no): ")
		if loop1 == "no" or loop1 == "NO" or loop1 == "No":
			loop = 0
		else: 
			loop = 1
	sql.close()
	con.close()

if __name__=='__main__':
	main()




			
			
			






