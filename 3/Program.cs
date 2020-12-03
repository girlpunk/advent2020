using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace _3
{
    class Program
    {
        private const char Tree = '#';

        static async Task Main(string[] args)
        {
            Console.WriteLine($"First task: {await First()}");
            Console.WriteLine($"Second task: {await Second()}");
        }

        private static async Task<int> First(int across=3, int down=1)
        {
            var file = await File.ReadAllLinesAsync("input.txt");

            var currentAcross = 0;
            var currentDown = 0;
            var trees = 0;

            while (true)
            {
                currentAcross += across;
                currentDown += down;

                if (currentAcross + 1> file[0].Length)
                    currentAcross -= file[0].Length;

                if (currentDown +1 > file.Length)
                    break;

                if (file[currentDown][currentAcross] == Tree)
                    trees += 1;
            }

            return trees;
        }

        private static async Task<uint> Second()
        {
            uint one = (uint) await First(1, 1);
            uint two = (uint) await First(3, 1);
            uint three = (uint) await First(5, 1);
            uint four = (uint) await First(7, 1);
            uint five = (uint) await First(1, 2);

            return one * two * three * four * five;
        }
    }
}
