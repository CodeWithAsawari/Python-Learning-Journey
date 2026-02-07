## PANDAS

"""Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.
"""

#Import Pandas
#Once Pandas is installed, import it in your applications by adding the import keyword:

import pandas
a = {
    'Names': ["Asawari", "Sanjay", "Shraddha"],
    'Marks': [99, 100, 99]
}
b = pandas.DataFrame(a)
print(b)

#Pandas as pd
#Pandas is usually imported under the pd alias.

import pandas as pd
a ={'name':["Asawari","Sanjay"],
    'Marks':[99,100]}
b = pd.DataFrame(a)
print(b)

#Checking Pandas Version
import pandas as pd
print(pd.__version__)

#Series
#It is a one-dimensional array holding data of any type.
import pandas as pd
a = {
    'Names': ["Asawari", "Sanjay"],
}
b = pd.Series(a)
print(b)

#Labels
import pandas as pd
a = ["Asawari", "Sanjay"]
b = pd.Series(a)
print(b[0])

#Create Labels
#With the index argument, you can name your own labels

import pandas as pd
a =[1,2,3]
b=pd.Series(a,index=["a","b","c"])
print(b)
print(b["a"])

#Key/Value Objects as Series
import pandas as pd
a ={"Marks1":99,"Marks2":98,"Marks3":97}
b=pd.Series(a)
print(b)

import pandas as pd
a ={"Marks1":99,"Marks2":98,"Marks3":97}
b=pd.Series(a,index=["Marks1","Marks2"])#use the index argument and specify only the items you want to include in the Series.
print(b)

#DataFrames
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

import pandas
a = {
    'Names': ["Asawari", "Sanjay", "Shraddha"],
    'Marks': [99, 100, 99]
}
b = pandas.DataFrame(a)
print(b)
