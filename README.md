#### Project Name: Exam Scheduler Genetic Algorithm

---

#### Description

The Exam Scheduler GA project uses a Genetic Algorithm to find an optimal and feasible solution for scheduling exams. The algorithm ensures that there are no conflicts between courses with common students and that the maximum allotted time for each exam hall is not exceeded.

#### Contents

1. **genetic_algorithm.py**: The main script containing the genetic algorithm code.
2. **test_data.py**: Contains sample test data for running the algorithm.
3. **README.md**: Documentation and explanation of the project.

---

#### Prerequisites

- Python 3.x
- `random` library (standard library, no need for separate installation)

#### Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ExamSchedulerGA.git
   cd ExamSchedulerGA
   ```

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

3. No additional dependencies are required as the project uses the standard `random` library.

---

#### Usage

1. **Run the genetic algorithm:**
   ```bash
   python genetic_algorithm.py
   ```

2. The algorithm will initialize a population, select parents using the roulette wheel selection method, perform crossover and mutation to generate new solutions, and check for the best solution based on fitness value.

3. **Sample Output:**
   ```
   Solution 1: Fitness Value = -220
   Solution 2: Fitness Value = -180
   ...
   Best Solution Obtained:
   [('Mathematics', '9-10', 'H1'), ('English', '12-1', 'H2'), ('History', '1-2', 'H1'), ('German', '9-10', 'H2'), ('Chinese', '12-1', 'H1')]
   ```

#### Code Explanation

- **Classes:**
  - `Course`: Represents a course with a name and a timeslot.
  - `ExamHall`: Represents an exam hall with a name and a maximum time it can be used.

- **Functions:**
  - `initializePopulation()`: Initializes a population of potential solutions.
  - `checkFitness()`: Evaluates the fitness of a solution by checking for conflicts and hall time constraints.
  - `rouletteWheelSelection()`: Selects two parent solutions based on their fitness values.
  - `singlePointCrossover()`: Performs crossover between two parent solutions to generate a child solution.
  - `mutation()`: Applies mutation to a solution to introduce diversity.
  - `geneticAlgorithm()`: The main function that runs the genetic algorithm.

---

#### Testing

Three sets of test data are used to evaluate the algorithm's performance:

1. **Test Data 1:**
   - 5 courses, 2 exam halls, 3 time slots.
   - Conflict information between courses.
   - Result: Optimal solution found in 0.2 seconds.

2. **Test Data 2:**
   - 10 courses, 3 exam halls, 3 time slots.
   - Increased number of conflicts.
   - Result: Optimal solution found in 0.813 seconds.

3. **Test Data 3:**
   - 10 courses, 5 exam halls, 8 time slots.
   - More complex conflicts.
   - Result: Optimal solution found in 1.002 seconds.

