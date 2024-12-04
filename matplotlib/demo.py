# from matplotlib import pyplot as py
# from numpy import *
# from turtle import color
#
# first=arange(1,11)
# second=2*first
#
# print(first)
# print("\n")
# print(second)
#
#
# py.plot(first,second,color='red',linestyle='-',linewidth=2)
# py.xticks(first)
# py.yticks(second)
# py.xlabel("Students")
# py.ylabel("Percentage")
# py.title("Result")
# py.show()


#
# from turtle import color
# from numpy import *
# from matplotlib import pyplot as py
#
# years=arange(2016,2022)
# print("years is\t",years)
# dac_batch=array([100,110,120,115,118,120])
# dbda_batch=array([38,45,48,50,55,60])
# py.plot(years,dac_batch,color='r',linestyle=':',linewidth=2)
# py.plot(years,dbda_batch,color='blue',linestyle='-',linewidth=2)
# py.title("VITA DAC_DBDA Batch Summary for last 5 years")
# py.xlabel("years")
# py.ylabel("DAC and DBDA Total no. of students")
# py.grid(True)
# py.show()

#
# from matplotlib import pyplot as py
#
# students={"Sachin":90,"Rahul":80,"Anil":70}
#
# names=list(students.keys())
# marks=list(students.values())
#
# # py.bar(names,marks)
# py.bar(names,marks)
# py.xlabel("Students names")
# py.ylabel("marks in maths")
# py.show()


# scatter plots
#
# from numpy import *
# from matplotlib import pyplot as py
#
# first=arange(1,11)
# second=2*first
#
# py.scatter(first,second,marker="*",c='black')   #  scatter plot  ,   first and second must have same no. of elements
#
# py.show()


#
# 1) create first array "overs" with 4 elements
# 5,10,15,20
# create another array "runs_scored" with 4 elements and store
# no.of runs scored at the end of each over
# e.g.  40 runs at the end of 5th over , 75 runs at the end of 10th over etc.


# from matplotlib import pyplot as py
# from numpy import *
# from turtle import color
#
# overs=array([5,10,15,20])
# runs_scored=array([40,80,120,180])
#
# first=py.plot(overs,runs_scored,color='red',linewidth=2)
# py.xticks(overs)
# py.yticks(runs_scored)
# py.xlabel("Overs")
# py.ylabel("Runs_Scored")
# py.title("Cricket")
# py.show()


# 2) create a Bar plot to show how many people like "Action","Romance","Comedy" or "Drama" movies.

# from matplotlib import pyplot as py
#
# Genre={'Action':30,'Romance':50,'Comedy':15,'Drama':5}
#
# Type=list(Genre.keys())
# People=list(Genre.values())
#
# genre=py.bar(Type,People,color='pink')
# py.xlabel("Genre")
# py.ylabel("People")
# py.title("Movie_Stats")
# py.show()

# 3) create a piechart to show popularity of various modules (Java,Python etc.)


from matplotlib import pyplot as py

modules=['JAVA','Python','C++','C']
popularity=[65,10,15,10]

py.pie(popularity,labels=modules,colors=['red','blue','yellow','pink'])
py.legend()
py.title("Cources")
py.show()





















