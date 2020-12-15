using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace _7
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var lines = await GetLines();

            await GetLines();

            // Console.WriteLine($"First task: {First(lines)}");
            // Console.WriteLine($"Second task: {Second(lines)}");
        }

        private static async Task<ParallelQuery<(string container, IEnumerable<string> contents)>> GetLines() =>
            (await File.ReadAllLinesAsync("input.txt"))
            .AsParallel()
            .Select(rule =>
            {
                var ruleParts = rule.Split("contain");
                var container = ruleParts[0].Replace("bags", "").Replace("bag", "").Trim();
                var contents = ruleParts[1].Split(',').Select(part => part.Trim().Replace("bags", "").Replace("bag", ""));
                return (container, contents);
            });
    }
}
