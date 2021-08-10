using System;
using System.Linq;

namespace _20
{
    class Tile
    {
        public int Id { get; set; }
        public bool[][] Data { get; set; }

        public Tile(string raw)
        {
            var lines = raw.Split(Environment.NewLine.ToCharArray());

            Id = int.Parse(lines[0].Split("Tile ")[1].Split(":")[0]);

            Data = lines
                .Skip(1)
                .Where(line => line != "")
                .Select(line => 
                    line.Select(c => c == '#')
                        .ToArray())
                .ToArray();
        }

        public bool FitsLeftOf(Tile other) => CheckAllPositions(other, d => d.Select(row => row.Last()).ToArray(), d => d.Select(row => row.First()).ToArray());

        public bool FitsRightOf(Tile other) => CheckAllPositions(other, d => d.Select(row => row.First()).ToArray(), d => d.Select(row => row.Last()).ToArray());

        public bool FitsAbove(Tile other) => CheckAllPositions(other, d => d.Last(), d => d.First());

        public bool FitsBelow(Tile other) => CheckAllPositions(other, d => d.First(), d => d.Last());

        private bool CheckAllPositions(Tile other, Func<bool[][], bool[]> a, Func<bool[][], bool[]> b)
        {
            if (CheckAllRotations(other, a, b))
                return true;

            FlipH();

            if (CheckAllRotations(other, a, b))
                return true;

            FlipV();

            if (CheckAllRotations(other, a, b))
                return true;

            FlipH();

            if (CheckAllRotations(other, a, b))
                return true;

            FlipV();

            return false;
        }

        private bool CheckAllRotations(Tile other, Func<bool[][], bool[]> a, Func<bool[][], bool[]> b)
        {
            for (var i = 0; i < 4; i++)
            {
                if (a(Data).SequenceEqual(b(other.Data)))
                    return true;

                Rotate();
            }

            return false;
        }

        public void Rotate()
        {
            var length = Data[0].Length;

            var retVal = new bool[length][];

            for (var x = 0; x < length; x++)
            {
                retVal[x] = Data.Select(p => p[x]).ToArray();
            }

            Data = retVal;
        }

        public void FlipH()
        {
            for (var x = 0; x < Data.Length; x++)
            {
                Data[x] = Data[x].Reverse().ToArray();
            }
        }

        public void FlipV()
        {
            Data = Data.Reverse().ToArray();
        }
    }

    public static class Utils {
        
    }
}
