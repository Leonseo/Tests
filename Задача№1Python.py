def array_copy(array):
    new_array = [0] * len(array)

    for i in range(len(array)):
        new_array[i] = array[i]

    return new_array

def array_copy_tests():
    test1 = []
    assert test1 == array_copy(test1), "Проверка пустого массива не удалась"

    test2 = [1, 2, 3]
    assert test2 == array_copy(test2), "Проверка обычного массива не удалась"

    test3 = test2
    test3_copy = array_copy(test2)
    test2[0] = 0
    assert test3_copy != test2, "Проверка копирования не удалась"

    print("Все тесты пройдены")

if __name__ == "__main__":
    array_copy_tests()
