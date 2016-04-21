import numpy as np 
from PyQt4 import QtCore, QtGui


class ClassName(object):
	"""docstring for ClassName"""
	

	"""
	The first def in a class is the __init__, which is the initial properties given
	to an instance of the called class.  These properties will then be associated 
	with a specific instance rather than the entire class, as would be the case 
	using the following definitions not in the __init__ def. 


	The most common use of super is in the declaration of __init__ of base classes
	
	example:
	
	class Child(Parent):
		def __init__(self, stuff):
			self.stuff = stuff
			super(Child, self).__init__


		"""
	def __init__(self, arg):
		super(ClassName, self).__init__()	#call super (class) with argument (className) and (self), then call the function .__init__
											#super is used to control multiple inheritance
		self.arg = argument 				
		self.arg2 = []						#Instantiate a list which can be ammended for each instance of the class using the following def
	
	def functionAmmendArg2(self, trait):
		self.arg2.append(trait)
		#pass								#Pass is used as a code completion filler to pass on to the next def if nothing has been defined

	def function():
		pass


"""
Inheritance is defined by the Parent-child or "is-a" relationship.

Composition is defined by the use of a "has-a" relationship, where one class simply 
uses another class to do work, rather than having inherited from said class.  

Composition is considered to be a more robust method of coding since multiple 
inheritance can become complicated and result in code which is not readily 
reusable (as copy-paste modules/tools, for example).
"""


"""
A comment on doc flow control:

use the __name__ property of the document to test wether 
the file is being executed on its own or if it has been imported from another module

example:
"""
if __name__ == '__main__':
	print 'This program is being run by itself'
else:
	print 'I am being imported from another module'




"""
The following is auto completed when one types property
"""

def foo():
    doc = "The foo property."
    def fget(self):
        return self._foo
    def fset(self, value):
        self._foo = value
    def fdel(self):
        del self._foo
    return locals()
foo = property(**foo())



""""
Autocompletion of the try, except, else, finally function:
"""

try:
	pass
except Exception, e:
	raise
else:
	pass
finally:
	pass