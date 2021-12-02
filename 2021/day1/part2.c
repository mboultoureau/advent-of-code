#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#define RESET   "\033[0m"
#define BOLDWHITE   "\033[1m\033[37m"

int main()
{
    int numbers[3];
    int previousSum = 0;
    int currentSum = 0;
    int increase = 0;
    FILE *file = fopen("input.txt", "r");

    // if file doesn't exist
    if (file == NULL)
    {
        fprintf(stderr, "Unable to read the file.");
        exit(EXIT_FAILURE);
    }

    // read the first line
    fscanf(file, "%d", &numbers[0]);
    fscanf(file, "%d", &numbers[1]);
    fscanf(file, "%d", &numbers[2]);

    previousSum = numbers[0] + numbers[1] + numbers[2];
    printf("%d (N/A - no previous sum)\n", previousSum);

    numbers[0] = numbers[1];
    numbers[1] = numbers[2];

    // read the lines, make sum and increase the counter
    while (fscanf(file, "%d", &numbers[2]) != EOF)
    {
        currentSum = numbers[0] + numbers[1] + numbers[2];

        if (currentSum > previousSum)
        {
            printf("%d " BOLDWHITE "(increased)\n" RESET, currentSum);
            increase++;
        }
        else if (currentSum == previousSum)
        {
            printf("%d (no change)\n", currentSum);
        }
        else
        {
            printf("%d (descreased)\n", currentSum);
        }

        numbers[0] = numbers[1];
        numbers[1] = numbers[2];

        previousSum = currentSum;
    }

    // display the number of increases
    printf("There are %d sums that are larger than the previous sum.", increase);

    // close the file
    fclose(file);

    return EXIT_SUCCESS;
}