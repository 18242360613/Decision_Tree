import operator
import sys
sys.path.append('E:\MeachineLearn\Decision_Tree\DecisionTree\Trees.py');
sys.path.append('E:\MeachineLearn\Decision_Tree\DecisionTree\treePlotter.py');
import Trees
import treePlotter

#fr = open('E:\machinelearninginaction\Ch03\lenses.txt');
#lenses = [inst.strip().split('\t') for  inst in fr.readlines()]
#lensesLabels = ['age','prescript','astigmatic','tearRate']
#lensesTree = Trees.createTree(lenses,lensesLabels)
#print(lensesTree)
#treePlotter.createPlot(lensesTree);

dataSet,labels = Trees.createDataSet()
print(labels)

mytree = Trees.createtree(dataSet,labels)

label = Trees.classify(mytree,labels,[1,0])

print(label)
