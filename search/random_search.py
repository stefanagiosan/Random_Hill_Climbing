import random


class RandomSearch:
    def __init__(self, filename):
        self.__obj = []
        self.__max_weight = 0
        self.__nr_obj = 0
        self.__best_solution = 0
        self.__solutions = []
        self.__file_configuration(filename)

    def __file_configuration(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.__nr_obj = int(lines[0])

            lines = [line.strip() for line in lines if line.strip()]
            for line in lines[1:-1]:
                x = line.split()
                obj_nr = int(x[0])
                weight = int(x[1])
                value = int(x[2])
                self.__obj.append({"nr": obj_nr, "weight": weight, "value": value})

            self.__max_weight = int(lines[-1])

    #this method evaluates the value of a solution for a knapsack problem , each item has a weight and a value
    #and there is a constraint of the maximum weight that can be carried
    def __eval(self, solution):
        total_weight = 0
        total_value = 0
        for i in range(len(solution)):
            if solution[i] == 1:
                total_weight += self.__obj[i]["weight"]
                total_value += self.__obj[i]["value"]

        if total_weight <= self.__max_weight:
            return total_value
        return 0

    #this method generates a random solution, where each item is represented either by '0' or by '1'.
    #0 is not included, 1 is included. The decision the include is made randomly.
    def __generate(self):
        solution = []
        for _ in range(len(self.__obj)):
            choice = random.choice([0, 1])
            solution.append(choice)
        return solution

    #this method performs a random search process where the solutions are evaluated. The best solution found
    #over the specified number of iterations is returned.
    def search(self, iteration):
        for i in range(iteration):
            solution = self.__generate()
            best_solution = self.__eval(solution)
            if best_solution > self.__best_solution:
                self.__best_solution = best_solution

        self.__solutions.append(self.__best_solution)

        return self.__best_solution
