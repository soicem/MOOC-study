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
public class PercolationStats {

    int n;
    int trials;

    public PercolationStats(int n, int trials) // perform trials independent experiments on an n-by-n grid
    {
        this.n = n;
        this.trials = trials;
    }

    public double mean() // sample mean of percolation threshold
    {
        return 0.0;
    }

    public double stddev() // sample standard deviation of percolation threshold
    {
        return 0.0;
    }

    public double confidenceLo() // low  endpoint of 95% confidence interval
    {
        return 0.0;
    }

    public double confidenceHi() // high endpoint of 95% confidence interval
    {
        return 0.0;
    }

    public static void main(String[] args) // test client (described below)
    {

    }
}
