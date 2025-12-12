"""train_model.py
This file contains a simple machine learning training function using Pytorch.
The model learns a single weight (w) to predict solar power from GHI using basic
relationship Power = w * GHI"""
import os
import time

# Allow duplicate OpenMP runtimes (workaround for libiomp5md.dll error)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch

def train_model(data):
    """Trains a simple linear regression model using gradient descent"""



    
    #Defining the parameters, Will be Using GHI and Power from dataset
    x= torch.tensor(data["GHI"].values,dtype = torch.float32).view(-1,1)
    y_true = torch.tensor(data["Power"].values, dtype = torch.float32).view(-1,1)

    w = torch.tensor([[0.1]],requires_grad = True)


    #Setting values
    lr = .000001 # Learning rate (small to avoid scaling issues or numerical issues)
    loss_value = 10000  #initial large loss to enter the loop
    epoch = 0 #training iteration count

    #Training
    #Train until loss is small enough or max epochs are reached
    while loss_value > .01 and epoch < 5000:

        y_pred = x @ w #Forward pass

        loss = ((y_pred - y_true)**2).mean() #Mean Squared Error Loss

        #Computing gradient of loss with respect to w
        loss.backward()

        #Update w
        with torch.no_grad():
            w -= lr * w.grad

        #Rest gradient to zero for next step
        w.grad.zero_()

        #Convert loss to a regular number 
        loss_value = loss.item()

        #Counting steps
        epoch +=1
    #Training Summary
    print("Training Complete!")
    print(f"Final Weight : {w.item()}")
    print(f"Final Loss: {loss_value}")
    print(f"Total Epochs: {epoch}")
    time.sleep(1)  # Pause for 1 second for better user experience

    return w #returns the learned weight