#!python
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - - -
#       OS : GNU/Linux 4.18.12-1-ARCH 
# COMPILER : Python 3.7.0
#
#   AUTHOR : Evgeny S. Borisov
# 
#    http://www.mechanoid.kiev.ua
#  e-mail : borisov.e@solarl.ru
# - - - - - - - - - - - - - - - -

class Node:
    def __init__(self,feature,bound,parent,left=None,right=None):
        self._feature = feature
        self._bound = bound
        self._parent = parent
        self._left = left
        self._right = right
        
    @property
    def feature(self): return self._feature

    @property
    def bound(self): return self._bound
    
    @property
    def left(self): return self._left
    @left.setter
    def left(self,value): self._left = value
    
    @property
    def right(self): return self._right
    @right.setter
    def right(self,value): self._right = value
    
    @property
    def parent(self): return self._parent
    @parent.setter
    def parent(self,value): self._parent = value
    
    def __repr__(self): return '%i:%f'%(self.feature, self.bound)



class Leaf:
    def __init__(self,mark,parent):
        self._mark = mark
        self._parent = parent
    
    @property
    def mark(self): return self._mark
    
    @property
    def parent(self): return self._parent
    @parent.setter
    def parent(self,value): self._parent = value
    
    def __repr__(self): return '%i'%(self.mark)
