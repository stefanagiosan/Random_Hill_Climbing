
class RandomWrite:
    def __init__(self, filename, k):
        self.__filename = filename
        self.__k = k
        self.__exec = []
        self.__solutions = []

    def set_exec(self, exec):
        self.__exec = exec

    def set_solutions(self, solutions):
        self.__solutions = solutions

    @staticmethod
    def write(solution, exec):
        with open("results/res_random.txt", "a") as file:
            file.write(f"{solution}<--->{exec}\n")

    def info(self):
        with open("results/res_random.txt", "a") as file:
            file.write(f"Se foloseste *Cautarea aleatoare* si se citesc datele din fisierul: {self.__filename}\n")
            file.write(f"Valoare lui K = {self.__k} si numarul de executii este: 10\n")

    def rezult(self):
        media_exec = sum(self.__exec) / len(self.__exec)
        media_solution = sum(self.__solutions) / len(self.__solutions)
        max_solution = max(self.__solutions)

        with open("results/res_random.txt", "a") as file:
            file.write(f"Valoarea medie: {media_solution}\n")
            file.write(f"Valoarea maxima: {max_solution}\n")
            file.write(f"Media timpului de executie: {media_exec}\n")