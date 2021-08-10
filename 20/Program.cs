using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

#nullable enable

namespace _20
{
    class Program
    {
        static async Task Main()
        {
            var positions = await First();
            var first = ((double)positions[0, 0].Id) *
                   ((double)positions[0, positions.GetLength(0) - 1].Id) *
                   ((double)positions[positions.GetLength(0) - 1, 0].Id) *
                   ((double)positions[positions.GetLength(0) - 1, positions.GetLength(0) - 1].Id);

            Console.WriteLine($"First task: {first}");
            Console.WriteLine($"Second task: {await Second(positions)}");
        }

        private static async Task<Tile?[,]> First()
        {
            // Parse Tiles
            var tiles = (await File.ReadAllTextAsync("input.txt"))
                .Split("\r\n\r\n")
                .Select(tile => new Tile(tile))
                .ToList();

            var numSides = (int) Math.Sqrt(tiles.Count);

            var foundAll = false;

            Tile?[,] positions = { };

            // Iterate through possible start tiles. This will be slow :(
            foreach (var startTile in tiles)
            {
                Console.WriteLine($"Trying starting tile {startTile.Id}");

                positions = new Tile[numSides, numSides];
                var startPosition = (int) (Math.Round(numSides / 2.0, MidpointRounding.ToPositiveInfinity) - 1);
                positions[startPosition, startPosition] = startTile;

                bool foundSomething;
                var remaining = tiles.Where(t => t != startTile).ToList();

                do
                {
                    foundSomething = false;

                    // Try to place remaining tiles
                    for (var x = 0; x < numSides; x++)
                    {
                        for (var y = 0; y < numSides; y++)
                        {
                            if (positions[x, y] != null)
                                continue;

                            if ((x - 1 > 0 && x - 1 < numSides && positions[x - 1, y] != null) ||
                                (x + 1 > 0 && x + 1 < numSides && positions[x + 1, y] != null) ||
                                (y - 1 > 0 && y - 1 < numSides && positions[x, y - 1] != null) ||
                                (y + 1 > 0 && y + 1 < numSides && positions[x, y + 1] != null))
                                foreach (var tile in remaining)
                                {
                                    var nearbyOk = true;
                                    var hasNearby = false;

                                    // Above
                                    if ((x - 1 > 0) && (x - 1 < numSides) && positions[x - 1, y] != null)
                                    {
                                        hasNearby = true;

                                        if (!tile.FitsBelow(positions[x - 1, y]))
                                            nearbyOk = false;
                                    }

                                    // Left
                                    if ((y - 1 > 0) && (y - 1 < numSides) && positions[x, y - 1] != null)
                                    {
                                        hasNearby = true;

                                        if (!tile.FitsRightOf(positions[x, y - 1]))
                                            nearbyOk = false;
                                    }

                                    // Right
                                    if ((y + 1 > 0) && (y + 1 < numSides) && positions[x, y + 1] != null)
                                    {
                                        hasNearby = true;

                                        if (!tile.FitsLeftOf(positions[x, y + 1]))
                                            nearbyOk = false;
                                    }

                                    // Below
                                    if ((x + 1 > 0) && (x + 1 < numSides) && positions[x + 1, y] != null)
                                    {
                                        hasNearby = true;

                                        if (!tile.FitsAbove(positions[x + 1, y]))
                                            nearbyOk = false;
                                    }

                                    if (hasNearby && nearbyOk)
                                    {
                                        foundSomething = true;
                                        positions[x, y] = tile;
                                        remaining = remaining.Where(t => t != tile).ToList();
                                        break;
                                    }
                                }
                        }
                    }

                    PrintDebug1(positions, startTile.Id, remaining.Count);
                } while (foundSomething);

                if (!positions.Cast<Tile?>().All(t => t != null))
                    continue;

                foundAll = true;
                break;
            }

            if (foundAll)
            {
                Console.WriteLine("Yay!");
                return positions;
                
            }

            throw new Exception("Couldn't find valid tile pattern");
        }

        

        private static async Task<int> Second(Tile?[,] positions)
        {
            var size = positions.GetLength(0)*8;
            bool?[,] image = new bool?[size, size];

            for (var x = 0; x < positions.GetLength(0); x++)
            {
                for (var y = 0; y < positions.GetLength(0); y++)
                {
                    var tile = positions[x, y];

                    for (var tileX = 1; tileX < 9; tileX++)
                    {
                        for (var tileY = 1; tileY < 9; tileY++)
                        {
                            image[(x * 8) + tileX - 1, (y * 8) + tileY - 1] = tile.Data[tileX][tileY];
                        }
                    }
                }
            }

            PrintDebug2(image);

            var (result, image1) = CheckAllRotations(image);
            image = image1;
            if (result)
            {
                PrintDebug2(image);
                return image.Cast<bool?>().Count(b => b is true);
            }

            // FlipV
            image = Rotate(Rotate(Rotate(FlipH(Rotate(image)))));

            (result, image) = CheckAllRotations(image);
            if (result)
            {
                PrintDebug2(image);
                return image.Cast<bool?>().Count(b => b is true);
            }

            image = FlipH(image);

            (result, image) = CheckAllRotations(image);
            if (result)
            {
                PrintDebug2(image);
                return image.Cast<bool?>().Count(b => b is true);
            }

            // FlipV
            image = Rotate(Rotate(Rotate(FlipH(Rotate(image)))));

            (result, image) = CheckAllRotations(image);
            if (result)
            {
                PrintDebug2(image);
                return image.Cast<bool?>().Count(b => b is true);
            }

            image = Rotate(Rotate(Rotate(FlipH(Rotate(image)))));

            return -1;
        }

        private static bool?[,] FlipH(bool?[,] image)
        {
            var size = image.GetLength(0);

            for (var i = 0; i < size; i++)
            { 
                var start = 0;
                var end = size - 1;

                while (start < end)
                {
                    var temp = image[i, start];
                    image[i, start] = image[i, end];
                    image[i, end] = temp;

                    start++;
                    end--;
                }
            }

            return image;
        }

        private static (bool result, bool?[,] image) CheckAllRotations(bool?[,] image)
        {
            for (var i = 0; i < 4; i++)
            {
                var result = LookForMonsters(image);
                if (result.result)
                    return result;

                image = Rotate(result.image);
            }

            return (result: false, image);
        }

        private static (bool result, bool?[,] image) LookForMonsters(bool?[,] image)
        {
            var found = false;
            var size = image.GetLength(0);

            for (var x = 0; x < size; x++)
            {
                for (var y = 0; y < size; y++)
                {
                    //TODO: AAAAAAH
                    if (image[x, y] == false ||
                        BoundsCheck(x + 1, y + 1, size) == false || image[x + 1, y + 1] == false ||
                        BoundsCheck(x + 4, y + 1, size) == false || image[x + 4, y + 1] == false ||
                        BoundsCheck(x + 5, y, size) == false || image[x + 5, y] == false ||
                        BoundsCheck(x + 6, y, size) == false || image[x + 6, y] == false ||
                        BoundsCheck(x + 7, y + 1, size) == false || image[x + 7, y + 1] == false ||
                        BoundsCheck(x + 10, y + 1, size) == false || image[x + 10, y + 1] == false ||
                        BoundsCheck(x + 11, y, size) == false || image[x + 11, y] == false ||
                        BoundsCheck(x + 12, y, size) == false || image[x + 12, y] == false ||
                        BoundsCheck(x + 13, y + 1, size) == false || image[x + 13, y + 1] == false ||
                        BoundsCheck(x + 16, y + 1, size) == false || image[x + 16, y + 1] == false ||
                        BoundsCheck(x + 17, y, size) == false || image[x + 17, y] == false ||
                        BoundsCheck(x + 18, y, size) == false || image[x + 18, y] == false ||
                        BoundsCheck(x + 19, y, size) == false || image[x + 19, y] == false ||
                        BoundsCheck(x + 18, y - 1, size) == false || image[x + 18, y - 1] == false)
                    {
                        continue;
                    }

                    Console.WriteLine($"FOUND ONE: {x}, {y}");
                    image[x, y] = null;
                    image[x + 1, y + 1] = null;
                    image[x + 4, y + 1] = null;
                    image[x + 5, y] = null;
                    image[x + 6, y] = null;
                    image[x + 7, y + 1] = null;
                    image[x + 10, y + 1] = null;
                    image[x + 11, y] = null;
                    image[x + 12, y] = null;
                    image[x + 13, y + 1] = null;
                    image[x + 16, y + 1] = null;
                    image[x + 17, y] = null;
                    image[x + 18, y] = null;
                    image[x + 19, y] = null;
                    image[x + 18, y - 1] = null;
                    found = true;
                }
            }

            return (result: found, image);
        }

        private static bool?[,] Rotate(bool?[,] input)
        {
            var n = input.GetLength(0);
            bool?[,] ret = new bool?[n, n];

            for (var i = 0; i < n; ++i)
            {
                for (var j = 0; j < n; ++j)
                {
                    ret[i, j] = input[n - j - 1, i];
                }
            }

            return ret;
        }

        private static bool BoundsCheck(int x, int y, int size) => x > 0 && y > 0 && x < size && y < size;

        private static void PrintDebug1(Tile?[,] positions, int startTile, int remaining)
        {
            Console.Clear();
            Console.WriteLine($"----- Start: {startTile} --- Remaining: {remaining}");
            for (var i = 0; i < positions.GetLength(0); i++)
            { 
                for (var j = 0; j < positions.GetLength(1); j++) 
                { 
                    var t = positions[i, j]; 
                    var num = t?.Id ?? 0; 
                    Console.Write(num + "\t");
                } 
                Console.WriteLine();
            }
        }

        private static void PrintDebug2(bool?[,] image)
        {
            var size = image.GetLength(0);
            for (var x = 0; x < size; x++)
            {
                for (var y = 0; y < size; y++)
                {
                    var pixel = image[x, y];
                    if (pixel == null)
                    {
                        Console.Write('!');
                    }
                    else if (pixel == true)
                    {
                        Console.Write('#');
                    }
                    else
                    {
                        Console.Write('.');
                    }
                }

                Console.WriteLine();
            }
        }
    }
}
