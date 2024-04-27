class Array:

    def __init__(self, capacity: int):
        self._n = capacity
        self._count = 0
        self._data = [0 for i in range(capacity)]


    def find(self, index: int) -> int:
        if index < 0 or index >= self._count:
            return -1
        return self._data[index]

    def insert(self, index: int, value: int) -> bool:
        if self._count == self._n:
            print("没有可插入的位置")
            return False

        if index < 0 or index > self._count:
            print("位置不合法")
            return False

        for i in range(self._n, index, -1):
            self._data[i - 1] = self._data[i - 2]

        self._data[index] = value
        self._count += 1
        return True

    def delete(self, index: int) -> bool:
        if index < 0 or index >= self._count:
            return False

        for i in range(index, self._n, -1):
            self._data[i - 1] = self._data[i]

        self._count -= 1
        return True

    def print_all(self):
        #print(self._count)
        for i in range(self._count):
            print(self._data[i], end=' ')
            print(type(self._data[i]), end=',')
        print()

def test_array():
    array = Array(5)
    array.print_all()

    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    #array.insert(3, 11)
    array.print_all()

if __name__ == "__main__":
    test_array()