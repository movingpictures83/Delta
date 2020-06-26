import sys
import numpy
#import PyPluMA


class DeltaPlugin:
   def input(self, filename):
      stuff = open(filename, 'r')
      self.myfile1 = stuff.readline().strip()
      self.myfile2 = stuff.readline().strip()
      

   def run(self):
      #################################################
      # FIRST FILE
      filestuff1 = open(self.myfile1, 'r')
      firstline = filestuff1.readline()
      bacteria1 = firstline.split(',')
      if (bacteria1.count('\"\"') != 0):
         bacteria1.remove('\"\"')
      n = len(bacteria1)
      ADJ1 = []
      m = 0
      samples1 = []
      for line in filestuff1:
         contents = line.split(',')
         ADJ1.append([])
         samples1.append(contents[0])
         for j in range(n):
            value = float(contents[j+1])
            ADJ1[m].append(value)
         m += 1
      #################################################
      
      #################################################
      # SECOND FILE
      filestuff2 = open(self.myfile2, 'r')
      firstline = filestuff2.readline()
      bacteria2 = firstline.split(',')
      if (bacteria2.count('\"\"') != 0):
         bacteria2.remove('\"\"')
      n = len(bacteria2)
      ADJ2= []
      m = 0
      samples2 = []
      for line in filestuff2:
         contents = line.split(',')
         ADJ2.append([])
         samples2.append(contents[0])
         for j in range(n):
            value = float(contents[j+1])
            ADJ2[m].append(value)
         m += 1
      #################################################
      
      #################################################
      # UNIFY
      self.delta = dict()
      for bacteria in bacteria1:
         if (bacteria2.count(bacteria) != 0):
            self.delta[bacteria] = []

      for i2 in range(len(samples2)):
         sample = samples2[i2]
         if (samples1.count(sample) != 0): # Sample in both sets
            i1 = samples1.index(sample)
            for bacteria in self.delta:
               j1 = bacteria1.index(bacteria)
               j2 = bacteria2.index(bacteria)
               self.delta[bacteria].append(round((ADJ2[i2][j2] - ADJ1[i1][j1])*100, 2))
      #################################################


   def output(self, filename):
      means = []
      for bacteria in self.delta:
         means.append((numpy.mean(self.delta[bacteria]), numpy.std(self.delta[bacteria]), bacteria, self.delta[bacteria]))

      means.sort()
      means.reverse()
      print("OTU\tMean\tStd Dev\tAbundances")
      for element in means:
         if (abs(element[0]) >= 1):
           print((element[2]+"\t"), round(element[0], 2), "%\t", round(element[1], 2), "%\t", element[3])

