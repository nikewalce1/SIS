import numpy
import ga

"""
The y=target is to maximize this equation ASAP:
    y = w1x1+w2x2+w3x3+w4x4+w5x5+6wx6
    where (x1,x2,x3,x4,x5,x6)=(4,-2,3.5,5,-11,-4.7)
    Мы ищем параметры (веса), которые максимизируют такое уравнение.
    What are the best values for the 6 weights w1 to w6?
    We are going to use the genetic algorithm for the best possible values after a number of generations.
"""

# Inputs of the equation.
equation_inputs = [4, -2, 3.5, 5, -11, -4.7]

# Number of the weights we are looking to optimize.
num_weights = 6

"""
Genetic algorithm parameters:
    Mating pool size
    Population size
"""
#кол-во хромосом 8 и у каждого есть 6 генов, по одному на каждый вес
sol_per_pop = 8
num_parents_mating = 4


# Определение численности населения.
# На основе функции пригодности мы выберем лучших людей из текущей популяции в качестве родителей для спаривания.
pop_size = (sol_per_pop,
            num_weights)  # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
# Создание начальной популяции.
new_population = numpy.random.uniform(low=-4.0, high=4.0, size=pop_size)
print(new_population)

#Далее следует применить варианты GA (кроссовер и мутация) для
# получения потомства следующего поколения, создания новой популяции
# путем добавления обоих родителей и потомства и повторения таких шагов для ряда итераций / поколений.
num_generations = 5 # количество поколений
for generation in range(num_generations):
    print("Generation : ", generation)
    # Измерение пригодности каждой хромосомы в популяции.
    fitness = ga.cal_pop_fitness(equation_inputs, new_population)

    # Выбор лучших родителей для спаривания.
    parents = ga.select_mating_pool(new_population, fitness,
                                    num_parents_mating)

    # Создание следующего поколения с использованием кроссовера.
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(pop_size[0] - parents.shape[0], num_weights))

    # Добавление некоторых вариаций к оффсрпингу с использованием мутации.
    offspring_mutation = ga.mutation(offspring_crossover)

    # Создание новой популяции на основе родителей и потомков.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    # Лучший результат в текущей итерации.
    print("Best result : ", numpy.max(numpy.sum(new_population * equation_inputs, axis=1)))

#Получение лучшего решения после итерации доводя все поколения.
# Сначала рассчитывается пригодность для каждого решения в последнем поколении.
fitness = ga.cal_pop_fitness(equation_inputs, new_population)
# Затем верните индекс этого решения, соответствующий наилучшей пригодности.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

print("Best solution (weights): ", new_population[best_match_idx, :])
#значение пригодности
print("Best solution fitness : ", fitness[best_match_idx])
