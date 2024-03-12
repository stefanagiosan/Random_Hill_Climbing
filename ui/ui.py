import time

from search.random_search import RandomSearch
from search.rhc import RHC
from write_file.random_write import RandomWrite
from write_file.rhc_write import RHCWrite


class UI:
    def __init__(self, filename):
        self.__k = 35
        self.__p = 5

        self.__filename = filename
        self.__random_search = RandomSearch(filename)
        self.__rhc = RHC(filename)
        self.__exec = []
        self.__solutions = []

        self.__random_write = RandomWrite(filename, self.__k)
        self.__rhc_write = RHCWrite(filename, self.__k, self.__p)

    def menu(self):
        while True:
            print("1. Random Search(Cautare aleatoare)")
            print("2. RHC(Cautare locala)")
            print("3. Iesire")

            choice = input("Dati optiunea: ")

            if choice == "1":
                self.__solutions = []
                self.__exec = []
                self.__random_write.info()

                for i in range(10):
                    start = time.time()
                    solution = self.__random_search.search(self.__k)
                    end = time.time()
                    exec = end - start

                    self.__solutions.append(solution)
                    self.__exec.append(exec)
                    self.__random_write.write(solution, exec)

                self.__random_write.set_solutions(self.__solutions)
                self.__random_write.set_exec(self.__exec)
                self.__random_write.rezult()
            elif choice == "2":
                self.__solutions = []
                self.__exec = []
                self.__rhc_write.info()

                for i in range(10):
                    start = time.time()
                    solution = self.__rhc.search(self.__k, self.__p)
                    end = time.time()
                    exec = end - start

                    self.__solutions.append(solution)
                    self.__exec.append(exec)
                    self.__rhc_write.write(solution, exec)

                self.__rhc_write.set_solutions(self.__solutions)
                self.__rhc_write.set_exec(self.__exec)
                self.__rhc_write.rezult()
            elif choice == "3":
                break
            else:
                print("Invalid input")


