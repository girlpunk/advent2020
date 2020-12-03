using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace _1
{
    class Program
    {
        static async Task Main()
        {
            Console.WriteLine($"First task: {await First()}");
            Console.WriteLine($"Second task: {await Second()}");
        }

        static async Task<int> First()
        {
            var file = await File.ReadAllLinesAsync("input.txt");

            var numbers = file.AsParallel().Select(int.Parse).ToList();

            var match = numbers
                .AsParallel()
                .SelectMany(a => numbers, (a, b) => (a, b))
                .First(tuple => tuple.a + tuple.b == 2020);

            var result = match.a * match.b;

            return result;
        }

        static async Task<int> Second()
        {
            var file = await File.ReadAllLinesAsync("input.txt");

            var numbers = file.AsParallel().Select(int.Parse).ToList();
            var match = numbers
                .AsParallel()
                .SelectMany(a => numbers, (a, b) => (a, b))
                .SelectMany((a, b) => numbers, (a, c) => (a.a, a.b, c))
                .First(tuple => tuple.a + tuple.b + tuple.c == 2020);

            var result = match.a * match.b * match.c;

            return result;
        }
    }
}
