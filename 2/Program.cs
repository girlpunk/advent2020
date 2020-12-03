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

        private static async Task<int> First()
        {
            var file = await File.ReadAllLinesAsync("input.txt");

            return file.AsParallel()
                .Select(line => 
                { 
                    var (min, max, character, _, password) = line.Split(new[] {'-', ' ', ':'}); 
                    return (min, max, character: character[0], password);
                })
                .Select(inp => (min: int.Parse(inp.min), max: int.Parse(inp.max), inp.character, inp.password))
                .Count(inp =>
                {
                    var count = inp.password.Count(c => c == inp.character);
                    return (inp.min <= count) && (count <= inp.max);
                });
        }

        private static async Task<int> Second()
        {
            var file = await File.ReadAllLinesAsync("input.txt");

            return file.AsParallel()
                .Select(line =>
                {
                    var (p1, p2, character, _, password) = line.Split(new[] {'-', ' ', ':'});
                    return (p1, p2, character: character[0], password);
                })
                .Select(inp => (p1: int.Parse(inp.p1), p2: int.Parse(inp.p2), inp.character, inp.password))
                .Count(inp =>
                    (inp.password[inp.p1 - 1] == inp.character && inp.password[inp.p2 - 1] != inp.character) ||
                    (inp.password[inp.p1 - 1] != inp.character && inp.password[inp.p2 - 1] == inp.character));
        }
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
