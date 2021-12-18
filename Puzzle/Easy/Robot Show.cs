using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int L = int.Parse(Console.ReadLine());
        int N = int.Parse(Console.ReadLine());
        string[] inputs = Console.ReadLine().Split(' ');

        int maxi_dist = -1;

        for (int i = 0; i < N; i++)
        {
            int b = int.Parse(inputs[i]);
            int dist_to_start = b - 0;
            int dist_to_end = L - b;

            if (maxi_dist == -1)
            {
                maxi_dist = Math.Max(dist_to_start, dist_to_end);
            }
            else
            {
                maxi_dist = Math.Max(maxi_dist, Math.Max(dist_to_start, dist_to_end));
            }
        }

        Console.WriteLine(maxi_dist);
    }
}