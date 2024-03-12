import copy
import random

class RHC:
    def __init__(self, filename):
        self.__obj = []
        self.__weight = 0
        self.__nr_objects = 0
        self.__best_solution = 0
        self.__solutions = []
        self.__file_configuration(filename)

    def __file_configuration(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.__nr_objects = int(lines[0])

            lines = [line.strip() for line in lines if line.strip()]
            for line in lines[1:-1]:
                obj = line.split()
                obj_nr = int(obj[0])
                weight = int(obj[1])
                value = int(obj[2])
                self.__obj.append({"nr": obj_nr, "weight": weight, "value": value})

            self.__max_weight = int(lines[-1])

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

    def __generate(self):
        solution = []
        for _ in range(len(self.__obj)):
            choice = random.choice([0,1])
            solution.append(choice)
        return solution

    @staticmethod
    def __generate_neighbours(solution):
        neighbours = []
        for i in range(len(solution)):
            sol_copy = copy.deepcopy(solution)
            sol_copy[i] = 1 - sol_copy[i]
            neighbours.append(sol_copy)
        return neighbours

    def __random_neighbours(self, neighbours):
        return random.choice(neighbours)

    def search(self, iteration, max_iteration):
        solution = self.__generate()
        best_solution = self.__eval(solution)

        nr = 0
        for i in range(iteration):
            neighbours = self.__generate_neighbours(solution)
            random_neighbour = self.__random_neighbours(neighbours)
            best_neighbour = self.__eval(random_neighbour)

            if best_neighbour > best_solution:
                nr = 1
                solution = random_neighbour
                best_solution = best_neighbour
                break

            if i == max_iteration - 1 and nr == 0:
                solution = self.__generate()
                best_solution = self.__eval(solution)

        self.__best_solution = best_solution
        self.__solutions.append(self.__best_solution)

        return self.__best_solution

