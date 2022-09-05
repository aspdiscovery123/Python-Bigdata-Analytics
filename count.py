from mrjob.job import MRJob
class count(MRJob):
    
    def mapper(self,_,line):
        for word in line.split():
            yield (word,1)
    def reducer(self,word,counts):
        yield(word,sum(counts))
        
count.run()
