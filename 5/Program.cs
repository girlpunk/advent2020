using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace _5
{
    class Program
    {

        static async Task Main(string[] args)
        {
            var lines = await GetLines();

            Console.WriteLine($"First task: {First(lines)}");
            Console.WriteLine($"Second task: {Second(lines)}");
        }

        private static async Task<IEnumerable<int>> GetLines() =>
            (await File.ReadAllLinesAsync("input.txt"))
            .AsParallel()
            .Select(seat => seat.Replace('F', '0').Replace('B', '1').Replace('L', '0').Replace('R', '1'))
            .Select(seat => Convert.ToInt32(seat, 2));

        private static int First(IEnumerable<int> lines) => lines.Max();

        private static int Second(IEnumerable<int> lines)
        {
            var seats = new HashSet<int>(Enumerable.Range(lines.Min(), lines.Max()));
            seats.ExceptWith(lines);
            return seats.First();
        }
    }
}
