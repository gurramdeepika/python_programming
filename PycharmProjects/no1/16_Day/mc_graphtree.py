from sklearn import tree
from sklearn.datasets import load_iris
from IPython.display import Image,display
import pydotplus
import matplotlib.pyplot as plt

def load_data_set():
    iris = load_iris()
    return iris

def train_model(iris):
    lr = tree.DecisionTreeClassifier()
    lr1 = lr.fit(iris.data,iris.target)
    return lr1

def display_image(lr1,iris):
    dot_data = tree.export_graphviz(lr1,out_file=None,feature_names=iris.feature_names,
                                class_names=iris.target_names,filled=True,rounded=True)

    graph = pydotplus.graph_from_dot_data(dot_data)
    display(Image(data=graph.create_png()))

    plt.plot()
    plt.show()

if __name__ == '__main__':
    iris_data = load_data_set()
    decision_tree = train_model(iris_data)
    display_image(iris=iris_data,lr1=decision_tree)
