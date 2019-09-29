import copy
class MyMatrix:
    def __init__(self, data: list):
        """
        Create matrix of given data.
        Example of data:
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ]
        Return TypeError if data is not list.
        """
        if type(data) == list:
          self.__data = copy.deepcopy(data)
          pass
        else:
          return TypeError

    def __repr__(self) -> str:
        """
        Return visual presentation of matrix.
        Example:
          1  20   3   4
          5   6 100   8
        NO SPACE before first column.
        E.g.: repr(MyMatrix([[1, 2]])) == '1 2'
        Hint: use '\n' for line break
        """
        a = ""
        for i in self.__data:
          for j in i:
            a += str(j) + " "
          a += "\n"
        return a

    def size(self) -> tuple:
        """
        Return tuple(height, width) for matrix.
        Example: (2, 4)
        """
        if self.__data == []:
            return (0)
        else:
            return (len(self.__data), len(self.__data[0]))

    def flip_up_down(self):
        """
        E.g. modify
        1, 2, 3, 4   to   5, 6, 7, 8
        5, 6, 7, 8        1, 2, 3, 4
        """
        m = MyMatrix(self.__data)
        self.__data = m.flipped_up_down().get_data()
        return self

    def flip_left_right(self):
        """
        E.g. modify
        1, 2, 3, 4   to   4, 3, 2, 1
        5, 6, 7, 8        8, 7, 6, 5
        """
        m = MyMatrix(self.__data)
        self.__data = m.flipped_left_right().get_data()
        return self

    def flipped_up_down(self):
        if self.__data == []:
          return MyMatrix([])
        else:
          a = self.__empty_list()
          for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
              a[len(self.__data) - i - 1][j] = self.__data[i][j]
          return MyMatrix(a)

    def flipped_left_right(self):
        if self.__data == []:
          return MyMatrix([])
        else:
          a = self.__empty_list()
          for i in range(len(self.__data)):
            for j in range(len(self.__data[i])):
              a[i][len(self.__data) - j] = self.__data[i][j]
          return MyMatrix(a)

    def transpose(self):
        """
        E.g. modify
                          1, 5
        1, 2, 3, 4   to   2, 6
        5, 6, 7, 8        3, 7
                          4, 8
        """
        m = MyMatrix(self.__data)
        self.__data = m.transposed().get_data()
        return self

    def transposed(self):
        """
        Return transposed copy of MyMatrix.
        """ 
        D = self.__data
        if D == []:
          return(MyMatrix([]))
        else:
          n = len(self.__data)
          m = len(self.__data[0])
          a  = [[0] * n for i in range(m)]
          for i in range(len(D)):
            for j in range(len(D[0])):
              a[j][i] = D[i][j]
          return MyMatrix(a)

    def get_data(self):
        return self.__data

    def __empty_list(self):
        m = len(self.__data[0])
        n = len(self.__data)
        a  = [[0] * m for i in range(n)]
        return a

    def __add__(self, other):
        """
        Return self + other matrix. Do not modify self and other.
        """
        SD = self.__data
        OD = other.get_data()
        self_m = MyMatrix(SD)
        other_m = MyMatrix(OD)
        new_data = self_m.__empty_list()
        if SD == []:
          return other_m
        elif OD == []:
          return self_m
        else:
            if self_m.size() == other_m.size():
              for i in range(len(SD)):
                for j in range(len(SD[0])):
                  new_data[i][j] = SD[i][j] + OD[i][j]
              return MyMatrix(new_data)
            else:
              print("MatrixError: Matrixs mast have equal size")
                    
    def __sub__(self, other):
        """
        Return self - other matrix. Do not modify self and other.
        """
        SD = self.__data
        OD = other.get_data()
        self_m = MyMatrix(SD)
        other_m = MyMatrix(OD)
        new_data = self_m.__empty_list()
        if SD == []:
          OD *= -1
          return other_m
        elif OD == []:
          return self_m
        else:
            if self_m.size() == other_m.size():
              for i in range(len(SD)):
                for j in range(len(SD[0])):
                  new_data[i][j] = SD[i][j] - OD[i][j]
              return MyMatrix(new_data)
            else:
              return "MatrixError: Matrixs mast have equal size"
            
    def __imul__(self, number: int):
      D = self.__data
      if D == []:
        return self
      else:
        for i in range(len(D)):
          for j in range(len(D[0])):
            D[i][j] = D[i][j] * number
        return self

    def __iadd__(self, other):
        SD = self.__data
        OD = other.get_data()
        self_m = MyMatrix(SD)
        other_m = MyMatrix(OD)
        SD = (self_m + other_m).get_data()
        return self

    def __isub__(self, other):
        """self -= other."""
        SD = self.__data
        self_m = MyMatrix(SD)
        other_m = MyMatrix(OD)
        SD = (self_m - other_m).get_data()
        return self