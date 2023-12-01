import numpy as np
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def calculate_output(self, inputs):
        net_input = np.dot(inputs, self.weights) + self.bias
        return self.sigmoid(net_input)
class FeedForwardNeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
    def forward_propagate(self, inputs):
        for layer in self.layers:
            outputs = []
            for neuron in layer:
                output = neuron.calculate_output(inputs)
                outputs.append(output)
            inputs = outputs
        return outputs
layers = [
    [Neuron(weights=[0.5, 0.8], bias=-0.3), Neuron(weights=[0.2, 0.7], bias=-0.4)],
    [Neuron(weights=[0.3, 0.6], bias=-0.2)]
]
network = FeedForwardNeuralNetwork(layers)
inputs = np.array([0.1, 0.2])
outputs = network.forward_propagate(inputs)
print(outputs)
