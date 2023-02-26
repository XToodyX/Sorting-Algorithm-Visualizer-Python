import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

class AlgorithmVisualizer:
    
    def __init__(self):
        root = tk.Tk()
        root.geometry("900x500")
        root.title("Algorithm-Visualizer-Python")
        root.resizable(False, False)

        heading = tk.Label(root, text="Select Sorting Algorithm you like to visualize:", font=("Arial", 15))
        heading.pack(side="top", anchor="nw", padx=10, pady=10)

        # Creating Buttons for Algorithm Selection
        bubbleSortButton = tk.Button(root, text="Bubble Sort", width=50, height=5, command=self.visualize_bubble_sort)
        selectionSortButton = tk.Button(root, text="Selection Sort", width=50, height=5, command=self.visualize_selection_sort)
        insertionSortButton = tk.Button(root, text="Insertion Sort", width=50, height=5, command=self.visualize_insertion_sort)
        
        bubbleSortButton.pack()
        selectionSortButton.pack()
        insertionSortButton.pack()

        root.mainloop()

    def visualize_bubble_sort(self):

        values = np.random.randint(0, 100, 15)
        x = np.arange(0, 15, 1) # Get values 0-14

        for i in range(len(values)):
            for j in range(0, len(values)-i-1):
                plt.bar(x, values)
                plt.pause(0.25)
                plt.clf()
                if values[j] > values[j+1]:
                    values[j], values[j+1] = values[j+1], values[j]
        
    def visualize_selection_sort(self):

        values = np.random.randint(0, 100, 15)
        x = np.arange(0, 15, 1) # Get values 0-14

        for ind in range(len(values)):
            min_index = ind
    
            for j in range(ind + 1, len(values)):
                # select the minimum element in every iteration
                if values[j] < values[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (values[ind], values[min_index]) = (values[min_index], values[ind])

            plt.bar(x, values)
            plt.pause(0.25)
            plt.clf()

    def visualize_insertion_sort(self):

        values = np.random.randint(0, 100, 15)
        x = np.arange(0, 15, 1) # Get values 0-14

        if (n := len(values)) <= 1:
            return
        for i in range(1, n):
            
            key = values[i]
    
            j = i-1
            while j >=0 and key < values[j] :
                    values[j+1] = values[j]
                    j -= 1
            values[j+1] = key

            plt.bar(x, values)
            plt.pause(0.25)
            plt.clf()
                    

if __name__ == "__main__":
    AlgorithmVisualizer()

