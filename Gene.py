from random import randint
class Gene(object):
    """Contains the encoding of each gene in the algorithm"""
    def __init__(self,items,amount_of_items):
        self.encoding_of_gene=[];
        self.status_of_bins=[];
        self.sum_in_each_bin=[];
        self.amount_of_items=amount_of_items;
        self.evaluation=0;
        self.lower_probability=0;
        self.upper_probability=0;
        self.probability=0;
        for x in range(0,amount_of_items):
            self.encoding_of_gene.append(-1);
            self.status_of_bins.insert(0,{});
            self.sum_in_each_bin.append(0);
        for x in range(0,amount_of_items):
            flag=True;
            while(flag):
                index_randomized=randint(0,amount_of_items-1);
                if(self.sum_in_each_bin[index_randomized]+items[x]<=1):
                    self.sum_in_each_bin[index_randomized]+=items[x];
                    self.encoding_of_gene[x]=index_randomized;
                    flag=False;

    def evaluate_gene_by_bins_num_and_utilization(self,opt):
        """Evaluate the gene by the function : 1/(X-Y) where X= number of bins used and Y= optimal bound on number of bins used"""
        number_of_bins_used=0;
        for x in range(0,self.amount_of_items):
            if(self.sum_in_each_bin[x]>0):
                number_of_bins_used+=1;
        if (number_of_bins_used != opt):
            self.evaluation=(1/(number_of_bins_used-opt));
        else:
            self.evaluation=999999;
        #print("Number of bins used {} and evaluation is {} ".format(number_of_bins_used,self.evaluation))
    
    def switch_genes(self,second_gene,items):
        random_first_index=randint(1,((self.amount_of_items)/2)-1);
        random_second_index=randint(self.amount_of_items/2,self.amount_of_items-1);
        """ Incase you want to print how the genes switched between themselves.
        #Before the switch
        print("chosen first index is " + str(random_first_index) + " and the second index " + str(random_second_index+1));
        check_string="\nThe gene before switching : "
        for x in self.encoding_of_gene:
            check_string+= str(x);
        check_string+=" and the second : ";
        for x in second_gene.encoding_of_gene:
            check_string+= str(x);
        print(check_string);
        del check_string;
        check_string="The gene after switching : ";
        """
        for x in range(0,self.amount_of_items): #change the genes till index random_first_index and after random_second_index if possible.
           if(x<=random_first_index or x>=random_second_index):
                if(self.sum_in_each_bin[second_gene.encoding_of_gene[x]]+items[x]<=1 and second_gene.sum_in_each_bin[self.encoding_of_gene[x]]+items[x]<=1):
                    self.sum_in_each_bin[self.encoding_of_gene[x]]-=items[x];
                    second_gene.sum_in_each_bin[self.encoding_of_gene[x]]+=items[x];
                    self.sum_in_each_bin[second_gene.encoding_of_gene[x]]+=items[x];
                    second_gene.sum_in_each_bin[second_gene.encoding_of_gene[x]]-=items[x];
                    temp=self.encoding_of_gene[x];
                    self.encoding_of_gene[x]=second_gene.encoding_of_gene[x];
                    second_gene.encoding_of_gene[x]=temp;
        """print after the switch
        for x in self.encoding_of_gene:
            check_string+= str(x);
        check_string+=" and the second : ";
        for x in second_gene.encoding_of_gene:
            check_string+= str(x);
        print(check_string);
        del check_string;
        """

    def print_encoding_of_gene(self):
        output=''
        for x in self.encoding_of_gene:
            output+= str(x);
        print(output);

    def print_Bins(self,items):
        total_number_of_bins=0;
        for x in range(0,self.amount_of_items):
            self.status_of_bins[self.encoding_of_gene[x]][x]=items[x];
        for x in range(0,self.amount_of_items):
            if(self.sum_in_each_bin[x]>0):
                total_number_of_bins+=1;
                print(self.status_of_bins[x])
                print("Summation of the items on this bin " + str(self.sum_in_each_bin[x]) + "\n");
        print("Total amount of bins created for this gene " + str(total_number_of_bins));





