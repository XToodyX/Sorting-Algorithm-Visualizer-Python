import tkinter as tk


class AlgorithmVisualizer:
    
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.geometry("900x500")
        self.root.title("Algorithm-Visualizer-Python")
        self.root.resizable(False, False)

        heading = tk.Label(self.root, text="Select the kind of Algorithm you like to visualize:", font=("Arial", 15))
        heading.pack(side="top", anchor="nw", padx=10, pady=10)

        # Defining Grid for Algorithm Option Buttons
        self.optionFrame = tk.Frame(self.root)
        
        # Three columns long
        self.gridSize = 3
    
        for x in range(self.gridSize):
            self.optionFrame.columnconfigure(x, weight=1)

        # Define Buttons for Sorting in frame
        self.sortingAlgorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Heap Sort",
                             "Counting Sort", "Radix Sort", "Merge Sort", "Quick Sort"]

        self.currentRow=0

        for pos in range(len(self.sortingAlgorithms)):
            if pos % self.gridSize == 0: self.currentRow += 1
            tk.Button(self.optionFrame, text=self.sortingAlgorithms[pos], width=50, height=5, 
                    command=self.visualize_algorithm).grid(row=self.currentRow, column=pos%self.gridSize)

        self.optionFrame.pack(side="left", anchor="center",  padx=10, pady=10, fill="x")
        self.root.mainloop()
    
    def visualize_algorithm(self):
        print(f"This is sorting algorithm:")
        self.optionFrame.lift()

if __name__ == "__main__":
    print("Starting program")
    AlgorithmVisualizer()

