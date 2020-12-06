using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace _6
{
    class Program
    {
        static async Task Main()
        {
            Console.WriteLine(await First());
            Console.WriteLine(await Second());
        }

        private static async Task<int> First() =>
            (await File.ReadAllTextAsync("input.txt"))
                .Split("\r\n\r\n")
                .AsParallel()
                .Select(line => new HashSet<char>(line))
            .Select(line =>
            {
                line.Remove('\r');
                line.Remove('\n');
                return line;
            })
                .Select(line => line.Count)
            .Sum();

        private static async Task<int> Second() =>
            (await File.ReadAllTextAsync("input.txt"))
            .Split("\r\n\r\n")
            .AsParallel()
            .Select(group => group
                .Split('\n', ' ')
                .Select(line => new HashSet<char>(line)))
            .Sum(group => group.First().Count(question => group.All(line => line.Contains(question))));
    }
}
