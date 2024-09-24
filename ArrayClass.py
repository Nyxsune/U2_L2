"""
Connor Cox
U2 L2
Dynamic Array Class
"""
import ctypes

class DynamicArray:

  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)
  
  # Private Actions

  def __resize(self):
    # Doubles array capacity
    self.__capacity *= 2
    newArray = self.__make_array(self.__capacity)

    index = 0
    for element in self.__A:
      newArray[index] = element
      index += 1

    self.__A = newArray

  def __make_array(self, c):
    """return new array with capacity c"""
    return (c * ctypes.py_object)()

  # Public Actions

  def append(self, item):
    # Adds a new element to the first empty space, doubles capacity if full, and increases number of elements
    if self.__n == self.__capacity:
      self.__resize()
    
    self.__A[self.__n] = item
    self.__n += 1

  def get_cap(self):
    # Returns the capacity of the array
    return self.__capacity

  # Magic Methods

  def __str__(self):
    # Prints the array
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
    return out[:-2] + ']'

  def __getitem__(self, index):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[index]

  def __len__(self):
    # Returns the length of the array
    return self.__n
    

