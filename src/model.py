import numpy as np
import tensorflow as tf

class FFNN(object):
    def __init__(self, nvars):
        super(FFNN, self).__init__()
        self.nvars = nvars

    def build(self):
        ##############
        ### TASK 1 ###
        # Define your network! Hint: Look at the model code in
        # src/example_network/network.py. The same network can be used here,
        # as long as you get the layer sizes right.
        #
        # The network will model whether or not a passenger survived Titanic.
        # We will use a single output neuron to signal this.
        # The number of input variables is stored in self.nvars.
        #
        # Some properties need to be set, in order for the code to work:
        # self.input: placeholder for input data
        # self.output: the output layer
        # self.loss: the loss (some sort of difference between actual and ideal output)
        # self.train: an operation for training the network (aka. optimizer)
        # self.ideal: placeholder for ideal data
        # A property can be set like so: self.some_number = 123
        #
        # Want to verify that your implementation works?
        # Try running the test: python -m unittest discover <src-directory>
        # The test tries to learn from the AND and XOR operators.
        # Any network should ideally be able to learn AND.
        # Only networks with one or more hidden layers are able to learn XOR.

        ##############
        ### TASK 2 ###
        # With a working network in place, try getting the XOR-test to run by
        # adding a hidden layer. Adding a hidden layer is created the same way
        # as the output layer, with it's own weights and bias. The data should
        # then flow from the input layer, through the hidden,
        # before reaching the output layer.
        # The hidden layer network should perform similarly to the regular one,
        # when applied to the Titanic dataset.

        ##############
        ### TASK 3 ###
        # Try adjusting the learning rate, and see how it impacts learning.
        # Because neural nets are initialized randomly, you should probably
        # train about 10 models and take the average accuracy for it to mean
        # something.

        ##############
        ### TASK 4 ###
        # What input variables does the model pick up on? Are there some that
        # don't matter? Try to comment out one variable at a time, to see
        # how it affects the networks ability to learn. The variables can be
        # found in src/data.py, around line 24.

        ##############
        ### TASK 5 ###
        # What does your network think of your own chances of surviving Titanic?
        # Enter your own details in test/custom.csv.
        # Add as many rows as you wish.
        # In src/main.py, uncomment lines 75 through 82.
        # Start training the model, and read your survival chances!
        # 1.0 = live to tell the tale, 0.0 = dead as a dodo.
