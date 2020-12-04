using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace _4
{
    class Program
    {
        private static readonly List<string> EyeColours = new List<string>() {"amb", "blu", "brn", "gry", "grn", "hzl", "oth" };

        static async Task Main()
        {
            var watch1 = System.Diagnostics.Stopwatch.StartNew();
            await First();
            await First();
            await First();
            await First();
            await First();
            await Second();
            await Second();
            await Second();
            await Second();
            await Second();
            watch1.Stop();

            Console.WriteLine($"Both tasks: {watch1.ElapsedMilliseconds/5}");
        }

        private static async Task<int> First() =>
            (await File.ReadAllTextAsync("input.txt"))
                .Split("\r\n\r\n")
                .AsParallel()
                .Select(line => line.Split('\n', ' ').Select(pair => pair.Split(':')))
                .Where(line => line.Count(pair => pair[0] == "byr") == 1)
                .Where(line => line.Count(pair => pair[0] == "iyr") == 1)
                .Where(line => line.Count(pair => pair[0] == "eyr") == 1)
                .Where(line => line.Count(pair => pair[0] == "hgt") == 1)
                .Where(line => line.Count(pair => pair[0] == "hcl") == 1)
                .Where(line => line.Count(pair => pair[0] == "ecl") == 1)
                .Count(line => line.Count(pair => pair[0] == "pid") == 1);

        private static async Task<int> Second() =>
            (await File.ReadAllTextAsync("input.txt"))
            .Split("\r\n\r\n")
            .AsParallel()
            .Select(line => line
                .Split('\n', ' ')
                .ToArray()
                .Select(pair => pair
                    .Split(':')
                    .Select(part => part.Trim())
                    .ToArray()))
            .Where(line => line.Count(pair =>
                pair[0] == "byr" && pair[1].Length == 4 && int.Parse(pair[1]) >= 1920 && int.Parse(pair[1]) <= 2002) == 1)
            .Where(line => line.Count(pair =>
                pair[0] == "iyr" && pair[1].Length == 4 && int.Parse(pair[1]) >= 2010 && int.Parse(pair[1]) <= 2020) == 1)
            .Where(line => line.Count(pair =>
                pair[0] == "eyr" && pair[1].Length == 4 && int.Parse(pair[1]) >= 2020 && int.Parse(pair[1]) <= 2030) == 1)
            .Where(line => line.Count(pair => pair[0] == "hgt" && (
                (pair[1].Contains("cm") && pair[1].Length == 5 && int.Parse(pair[1].Substring(0, 3)) >= 150 && int.Parse(pair[1].Substring(0, 3)) <= 193) ||
                (pair[1].Contains("in") && pair[1].Length == 4 && int.Parse(pair[1].Substring(0, 2)) >= 59  && int.Parse(pair[1].Substring(0, 2)) <= 76))) == 1)
            .Where(line =>
                line.Count(pair => pair[0] == "hcl" && Regex.IsMatch(pair[1], "^#[0-9a-f]{6}\r?$")) == 1)
            .Where(line => line.Count(pair => pair[0] == "ecl" && EyeColours.Contains(pair[1])) == 1)
            .Count(line => line.Count(pair => pair[0] == "pid" && pair[1].Length == 9) == 1);
    }
}
