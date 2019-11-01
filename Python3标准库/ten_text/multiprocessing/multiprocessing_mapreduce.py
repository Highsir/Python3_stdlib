import collections
import itertools
import multiprocessing

class SimpleMapReduce:

    def __init__(self,map_func,reduce_func,num_worker = None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_worker)

    def partition(self,mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key,value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(
            self.map_func,
            inputs,
            chunksize = chunksize,
        )
        parttioned_data = self.partition(
            itertools.chain(*map_responses)
        )
        reduced_values = self.pool.map(
            self.reduce_func,
            parttioned_data,
        )
        return reduced_values