# Bombard-ant 🐜💥
Bombard-ant is an optimization tool that uses a genetic algorithm to strategically place bombs, maximizing the extermination of ants around multiple nests. The program simulates natural selection, crossover, and mutation to discover the most effective bomb locations for maximum impact.

## Features
- **Genetic Algorithm Optimization**: Employs selection, crossover, and mutation to improve bomb placements over generations.
- **Flexible Configuration**: Adjustable population size, mutation rate, crossover rate, and bomb radius.
- **Handles Multiple Nests**: Supports variable numbers and locations of ant nests.
- **Track Best Fitness**: Logs the best fitness (kill count) in each generation.

## How It Works
1. **Initialization**: Random bomb placements are generated as chromosomes.
2. **Fitness Calculation**: Each chromosome is evaluated based on how many ants it kills.
3. **Selection**: Uses roulette wheel selection to choose parent chromosomes.
4. **Crossover and Mutation**: Creates new bomb placements with crossover between parents and mutation.
5. **Evolution**: Advances the population through multiple generations to maximize kills.

## Installation
Clone this repository and ensure you have Python 3 installed.

```bash
git clone https://github.com/yourusername/bombard-ant.git
cd bombard-ant
```

## Usage
To run Bombard-ant, execute the main script:
```bash
python bombard_ant.py
```
The program outputs the best solution for each generation and the final bomb placements.

##Sample Output
Bombard-ant provides output like the following:
```bash
Generation: 0, Best fitness solution: 1030.543, Max kills: 1030.543
Generation: 1, Best fitness solution: 1123.254, Max kills: 1123.254
...
Best solution:
Bomb 1: (24.500, 66.300)
Bomb 2: (95.100, 53.200)
Bomb 3: (66.400, 88.700)
Ants extermination successful.
```

## Customization
Adjust the following parameters in bombard_ant.py to control the optimization:
* POPULATION_SIZE: Number of chromosomes in each generation.
* MAX_GENERATIONS: Maximum number of generations.
* CROSSOVER_RATE: Probability of crossover between chromosomes.
* MUTATION_RATE: Probability of mutation.
* BOMB_RADIUS: Effective radius of each bomb.

## Future Enhancements
* Variable Bomb Counts: Dynamically adjust bomb numbers based on nest density.
* Distance-Based Killing: Improve kill calculations with distance weighting.
* Visualization: Add graphics to show nest locations, bomb placements, and affected areas.

## Contributing
Contributions are welcome! Open issues or submit pull requests for enhancements and fixes.

## License
Licensed under the MIT License. See LICENSE for details.
