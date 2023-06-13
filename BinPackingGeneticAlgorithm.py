from Gene import Gene
import random;
import math;
from copy import deepcopy
def BinarySearch(population, number_rand,population_size):
    low=0; high=population_size; search=int(population_size/2);
    number_rand=random.uniform(0.001,1)
    while(number_rand < population[search].lower_probability or number_rand > population[search].upper_probability):
        if(number_rand < population[search].lower_probability):
            high=search;
            search=(int((search-low)/2));
        else:
            low=search;
            search+=(int((high-search)/2));
    return search;

n = int(input("Enter amount of items to pack : "));
iteration_number = int(input("Enter amount of iterations to do : "));
input_list=[];
sum_of_items=0;
for x in range(0,n):
    number_rand=random.uniform(0.001,1)
    input_list.append(number_rand);
    sum_of_items+=number_rand;
population_size=int(input("Enter population size : "));
population=[];
for x in range(0,population_size): #create the genes and insert to population list
    population.append(Gene(input_list,len(input_list)))
opt=math.ceil(sum_of_items);
best_gene_solution=Gene(input_list,len(input_list));
#fields for construction an iteration and next wave
next_wave_population=[];
chosen_index_of_gene=-1; chosen_second_index_of_gene=-1;
#The algorithm
for k in range(0,iteration_number):
    sum_of_probability=0;
    #Evaluation process of the genes
    for gene in population:
        gene.evaluate_gene_by_bins_num_and_utilization(opt);
        if(gene.evaluation>1):
            best_gene_solution=gene;
            k=iteration_number;
            break;
        sum_of_probability+=gene.evaluation;
    if(k==iteration_number):
        break;
        
    #Setting up probabilities for each gene based on evaluation
    for gene in population:
        gene.probability=(gene.evaluation/sum_of_probability);
        #print(gene.probability);
    #Setting up intervals for each gene to allow Binary search instead of linear search
    run_number=0;
    for gene in population:
        gene.lower_probability=run_number;
        gene.upper_probability=(run_number+gene.probability);
        run_number+=gene.probability;
    #Setting up switching of genes and search by binary search
    for x in range(0,int(population_size/2)):
        low=0; high=population_size; search=int(population_size/2);
        number_rand=random.uniform(0.001,1)
        chosen_index_of_gene=BinarySearch(population,number_rand,population_size);
        number_rand=random.uniform(0.001,1)
        while(number_rand>=population[chosen_index_of_gene].lower_probability and number_rand<=population[chosen_index_of_gene].upper_probability):
            number_rand=random.uniform(0.001,1)
        chosen_second_index_of_gene=BinarySearch(population,number_rand,population_size);
        next_wave_population.insert(0,deepcopy(population[chosen_second_index_of_gene]));
        next_wave_population.insert(0,deepcopy(population[chosen_index_of_gene]));
        next_wave_population[0].switch_genes(next_wave_population[1],input_list);
    #Finished switching procedure
    population.clear();
    population=deepcopy(next_wave_population.copy());
    next_wave_population.clear();
    if(k%20==0):
        print("Iteration number " + str(k));

print("\n\nPrinting best solution :");
best_gene_solution.print_Bins(input_list);
print("OPT is bound by " + str(opt));
#for gene in population:
    #gene.print_Bins(input_list);


