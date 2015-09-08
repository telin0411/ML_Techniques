from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array
from pyspark import SparkContext, SparkConf

# Load and parse the data
def parsePoint(line):
    values = [x for x in line.split(' ')]
    features = [float(x.split(':')[1]) for x in values[1:]]
    return LabeledPoint(float(values[0]), features[0:])

conf = SparkConf().setAppName("Pyspark_SVM").set("spark.executor.memory", "4g").setMaster("local[4]")
sc = SparkContext(conf=conf)
data = sc.textFile("albert/train_libsvm0.txt")
parsedData = data.map(parsePoint)

# Build the model
model = LogisticRegressionWithSGD.train(parsedData)

# Evaluating the model on training data
labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())
print("Training Error = " + str(trainErr))