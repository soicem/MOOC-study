/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package week1;

/**
 *
 * @author soicem
 */
public class Percolation {

    int n;

    public Percolation(int n) // create n-by-n grid, with all sites blocked
    {
        this.n = n;
    }

    public void open(int i, int j) // open site (row i, column j) if it is not open already
    {

    }

    public boolean isOpen(int i, int j) // is site (row i, column j) open?
    {
        return true;
    }

    public boolean isFull(int i, int j) // is site (row i, column j) full?
    {
        return true;
    }

    public boolean percolates() // does the system percolate?
    {
        return true;
    }
}
