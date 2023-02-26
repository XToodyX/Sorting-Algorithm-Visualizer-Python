import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import time

class AlgorithmVisualizer(tk.Frame):
    
    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
        # heading = tk.Label(self, text="Select the kind of Algorithm you like to visualize:", font=("Arial", 15))
        heading = tk.Label(self, text="Sorting Algorithm Visualizer", font=("Arial", 15))
        heading.pack(side="top", anchor="nw", padx=10, pady=10)

        # Define Buttons for Sorting in frame
        self.sortingAlgorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Heap Sort",
                             "Counting Sort", "Radix Sort", "Merge Sort", "Quick Sort"]
        
        # Creating Container
        buttonFrame = tk.Frame(self)
        container = tk.Frame(self)
        buttonFrame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        # Define Frame for Algorithm Visualizers
        bubbleSort = BubbleSort()
        selectionSort = SelectionSort()
        insertionSort = InsertionSort()

        bubbleSort.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        selectionSort.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        insertionSort.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # Creating Buttons for Algorithm Selection
        bubbleSortButton = tk.Button(buttonFrame, text="Bubble Sort", width=50, height=5, command=lambda: bubbleSort.visualize_bubble_sort(buttonFrame))
        selectionSortButton = tk.Button(buttonFrame, text="Selection Sort", width=50, height=5, command=lambda: selectionSort.visualize_selection_sort(buttonFrame))
        insertionSortButton = tk.Button(buttonFrame, text="Insertion Sort", width=50, height=5, command=lambda: insertionSort.visualize_insertion_sort(buttonFrame))
        
        bubbleSortButton.pack()
        selectionSortButton.pack()
        insertionSortButton.pack()
    
class Page(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
    def show(self, buttonFrame):
        buttonFrame.pack_forget()
        self.lift()

class BubbleSort(Page):
    
    def __init__(self):
        Page.__init__(self)
        # Self instead of root underneath defines that Frame
        # instead of parent class should be used
        label = tk.Label(self, text="This is Bubble Sort")
        label.pack()

        
    def visualize_bubble_sort(self, buttonFrame):
        self.show(buttonFrame)
        print("This is bubble sort")

        values = np.random.randint(0, 100, 15)
        x = np.arange(0, 15, 1) # Get values 0-14

        for i in range(len(values)):
            for j in range(0, len(values)-i-1):
                plt.bar(x, values)
                plt.pause(0.25)
                plt.clf()
                if values[j] > values[j+1]:
                    values[j], values[j+1] = values[j+1], values[j]


class SelectionSort(Page):

    def __init__(self):
        Page.__init__(self)
        selectionSortLabel = tk.Label(self, text="This is Selection Sort")
        selectionSortLabel.pack()
        
    def visualize_selection_sort(self, buttonFrame):
        self.show(buttonFrame)
        print("This is selection Sort")

class InsertionSort(Page):

    def __init__(self):
        Page.__init__(self)
        insertionSortLabel = tk.Label(self, text="This is Insertion Sort")
        insertionSortLabel.pack()

    def visualize_insertion_sort(self, buttonFrame):
        self.show(buttonFrame)
        print("This is insertion sort")

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
    print("Starting program")
    root = tk.Tk()
    root.geometry("900x500")
    root.title("Algorithm-Visualizer-Python")
    root.resizable(False, False)
    main = AlgorithmVisualizer(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()

