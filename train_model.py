import os
import time

# Allow duplicate OpenMP runtimes (workaround for libiomp5md.dll error)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import torch

def train_model(data):
    #Defining the parameters, Will be Using GHI and Power from dataset
    x= torch.tensor(data["GHI"].values,dtype = torch.float32).view(-1,1)
    y_true = torch.tensor(data["Power"].values, dtype = torch.float32).view(-1,1)

    w = torch.tensor([[0.1]],requires_grad = True)


    #Setting values
    lr = .000001
    loss_value = 10000
    epoch = 0

    #Training
    while loss_value > .01 and epoch < 5000:

        y_pred = x @ w

        loss = ((y_pred - y_true)**2).mean()

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

    print("Training Complete!")
    print(f"Final Weight : {w.item()}")
    print(f"Final Loss: {loss_value}")
    print(f"Total Epochs: {epoch}")
    time.sleep(1)  # Pause for 1 second for better user experience

    return w