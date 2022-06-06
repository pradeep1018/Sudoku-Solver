from image_processing import extract as extract_img_grid
from digit_Recognition_CNN import run as create_and_save_Model
from predict import extract_number_image as sudoku_extracted
from solve import  ConstarintBacktracking as solve_sudoku
import tkinter as tk

def display_gameboard(sudoku):
    top = tk.Tk()
    top.title("Sudoku Solver")
    canvas = tk.Canvas(top, height=320, width =350)
    createRow(canvas)
    createCol(canvas)
    createlabel(top,sudoku)
    canvas.pack(side = 'top')
    top.mainloop()

def createlabel(top,sudoku):
    p,q=41.4,41.4
    for i in range(9):
        for j in range(9):
            L = tk.Label(top, text = '%s'%(sudoku[i][j]), width=3, font = 'BOLD')
            L.grid(row=i, column=j)
            L.place(x=p, y=q, height=20, width=25)
            p+=30.0
        q+=24.5
        p=41.2
    
def createRow(canvas):
    i,j=40,40
    p=40
    q=260
    for m in range(10):
        if(m%3==0):
            canvas.create_line(i,j,p,q,width=2.5)
        else:
            canvas.create_line(i,j,p,q,width=2)
        i+=30
        p+=30
    
def createCol(canvas):
    i,j=40,40
    p,q=310,40
    for m in range(10):
        canvas.create_line(i,j,p,q,width=2.3)
        j+=24.5
        q+=24.5



def main():

    # Calling the image_processing.py extract function to get a processed np.array of cells
    image_grid = extract_img_grid()
    print("Image Grid extracted")

    # uncomment the below line to train the model
    # create_and_save_Model()

    # Sudoku extract
    sudoku = sudoku_extracted(image_grid)
    display_gameboard(sudoku)

    solvable, solved = solve_sudoku(sudoku)

    if(solvable):
        display_gameboard(solved)

    print("Program End")




if __name__ == '__main__':
    main()