using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace _2
{
    class Program
    {
        static async Task Main()
        {
            Console.WriteLine($"First task: {await First()}");
            Console.WriteLine($"Second task: {await Second()}");
        }

        private static async Task<int> First() =>
            (await File.ReadAllLinesAsync("input.txt"))
            .AsParallel()
            .Select(line => line.Split('-', ' ', ':'))
            .Select(inp => new UL(int.Parse(inp[0]), int.Parse(inp[1]), inp[2][0], inp[4]))
            .Select(ul => new PL(ul, ul.Password.Count(c => c == ul.Character)))
            .Count(pl => pl.Min <= pl.Count && pl.Count <= pl.Max);

        private static async Task<int> Second() =>
            (await File.ReadAllLinesAsync("input.txt")).AsParallel()
            .Select(line => line.Split(new[] {'-', ' ', ':'}))
            .Select(inp => new UL(int.Parse(inp[0]), int.Parse(inp[1]), inp[2][0], inp[4]))
            .Count(inp => (inp.Password[inp.Min - 1] == inp.Character) != (inp.Password[inp.Max - 1] == inp.Character));
    }

    public class UL {
        public UL(int min, int max, char character, string password)
        {
            this.Min = min;
            Max = max;
            Character = character;
            Password = password;
        }

        public int Min { get; set; }
        public int Max { get; set; }
        public char Character { get; set; }
        public string Password { get; set; }
    }

    public class PL
    {
        public PL(UL ul, int count)
        {
            Min = ul.Min;
            Max = ul.Max;
            Character = ul.Character;
            Password = ul.Password;

            Count = count;
        }

        public int Min { get; set; }
        public int Max { get; set; }
        public char Character { get; set; }
        public string Password { get; set; }
        public int Count { get; set; }
    }

    public static class Extensions
    {
        public static void Deconstruct<T>(this IList<T> list, out T first, out T second, out T third, out T fourth, out T fith)
        {
            first = list.Count > 0 ? list[0] : default(T);
            second = list.Count > 1 ? list[1] : default(T);
            third = list.Count > 2 ? list[2] : default(T);
            fourth = list.Count > 3 ? list[3] : default(T);
            fith = list.Count > 4 ? list[4] : default(T);
        }
    }
}
