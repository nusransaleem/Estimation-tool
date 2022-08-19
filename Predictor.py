import pickle
from IP_Model.DataHandler import DataHandler as dHandler
from numpy import exp, array, random, dot


# The training set. We have 4 examples, each consisting of 3 input values
# and 1 output value.


class NeuralNetwork:
    dh = dHandler()
    dh.GetTrainingDataSets()
    training_set_inputs = array(dh.training_inputs)
    training_set_outputs = array([dh.training_outputs]).T

    def __init__(self):
        # Seed the random number generator, so it generated the same numbers
        # every time the program runs.
        random.seed(1)
        # as assign random weights to a 3 * 1 matrix, with values in the range -1 to 1 and mean 0.
        self.synaptic_weights = 2 * random.random((5, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through our Neural network (a single neuron).
            output = self.think(training_set_inputs)

            # Calculate the error( THe difference between the desired output and the predicted output
            error = training_set_outputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.

            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # THe neural network thinks.
    def think(self, inputs):
        # Pass inputs through our neural network (our sigle neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

    def Predict(self, data):
        # Initialize a single neuron neural network.
        neural_network = NeuralNetwork()

        print("Random starting synaptic weights: ")
        print(neural_network.synaptic_weights)

        # Train the neural network using a training set.
        # Do it 10,000 times and make small adjustments each time.

        neural_network.train(self.training_set_inputs, self.training_set_outputs, 10000)

        print("New synaptic weights after training: \n{}".format(neural_network.synaptic_weights))

        print("Considering new situation [13,3,30,10,25] -> ?:")
        print(neural_network.think(data))

    def predicting(self):
        lst = [144.987456387,42.96595599, 64.987456387, ]
        return lst
