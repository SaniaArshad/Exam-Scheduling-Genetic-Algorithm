import random  
 
class Course: 
    def __init__(self, name: str, timeslot: str): 
        self.name = name 
        self.timeslot = timeslot 
class ExamHall: 
    def __init__(self, name, maxTime): 
        self.name = name 
        self.maxTime = maxTime 
 
c1 = Course("Mathematics", "9-10") 
c2 = Course("English", "12-1") 
c3 = Course("History", "1-2") 
c4 = Course("German", "9-10") 
c5 = Course("Chinese", "12-1") 
 
h1 = ExamHall("H1", 6) 
h2 = ExamHall("H2", 6) 
 
courses = [c1, c2, c3, c4, c5] 
timeslots=  ["9-10", "12-1", "1-2"] 
halls= [h1, h2] 
 
conflicts = [(c1, c2, 10), (c1, c4, 5), (c2, c5, 7), (c3, c4, 12), (c4, c5, 8)] 
 
def initializePopulation(courses, timeslots, halls, conflicts, sizeOfSol): 
    population = [] 
    for i in range(sizeOfSol): 
        solutions = [] 
        for course in courses: 
            timeslot = random.choice(timeslots) 
            hall = random.choice(halls) 
            solutions.append((course.name, timeslot, hall.name)) 
        population.append(solutions) 
    return population 
 
def checkFitness(solution, conflicts, halls, maxTime): 
    fitness = 0 
    for conflict in conflicts:    
      course1, course2, students = conflict    
      course1_assigned = False 
      course2_assigned = False 
      for c in solution: 
        if c[0] == course1.name and c[1] == course1.timeslot: 
            course1_assigned = True 
        if c[0] == course2.name and c[1] == course2.timeslot: 
            course2_assigned = True   
      if course1_assigned and course2_assigned: 
        fitness -=  100 
    hall_time = {"H1": 0, "H2": 0} 
    for course, timeslot, hall in solution: 
        hall_time[hall] += 1 
        if hall_time[hall] > maxTime: 
            fitness -= 10    
    return fitness 
 
def rouletteWheelSelection(population, conflicts, halls, maxTime): 
    fitness_values = [] 
    for solution in population: 
        fitness_values.append(checkFitness(solution, conflicts, halls, maxTime)) 
    total_fitness = sum(fitness_values) 
 
    probabilityOfFitness = [] 
    for fitness in fitness_values: 
        probability=fitness/total_fitness 
        probabilityOfFitness.append(probability) 
 
    parents = [] 
    for i in range(2): 
        maxFitnessIndex = probabilityOfFitness.index(max(probabilityOfFitness)) 
        parents.append(population[maxFitnessIndex]) 
        probabilityOfFitness[maxFitnessIndex] = 0 #so that it isnt chosen again  when called 
    return parents 
 
def singlePointCrossover(parent1, parent2): 
   k = random.randint(0, 4) 
   j= parent1[k] 
   parent1[k]=parent2[k] 
   parent2[k]= j 
   return parent1 
 
def mutation(solution, timeslots, halls): 
    k = random.randint(0, 4)  
    course, timeslot, hall = solution[k] 
    new_timeslot = random.choice(timeslots)  
    solution[k] = (course, new_timeslot, hall)  
    return solution 
4 
 
 
def geneticAlgorithm(courses, timeslots, halls, conflicts): 
 
  population = initializePopulation(courses, timeslots, halls, conflicts, 100) 
  parents =rouletteWheelSelection(population, conflicts, halls, 6) 
  parent1=0 
  probabilityOfCrossover= 0.8 
  probabilityOfMutation= 0.1 
  if random.random() < probabilityOfCrossover: 
    parent1= singlePointCrossover(parents[0], parents[1]) 
    if random.random() < probabilityOfMutation: 
        parent1 = mutation(parent1, timeslots, halls) 
  return parents[0] 
 
maxSolutions = 1000 
Sol = 1 
solution = geneticAlgorithm(courses, timeslots, halls, conflicts) 
fitnessCheck = checkFitness(solution, conflicts, halls, 6) 
 
while fitnessCheck != 0 and Sol <= maxSolutions: 
    print(f"Solution {Sol}: Fitness Value = {fitnessCheck}") 
    Sol += 1 
    solution = geneticAlgorithm(courses, timeslots, halls, conflicts) 
    fitnessCheck = checkFitness(solution, conflicts, halls, 6) 
 
if fitnessCheck == 0: 
    print("Best Solution Obtained:") 
    print(solution) 
else: 
    print("The limit for maximum solutions has been reached. Solution is not found")
