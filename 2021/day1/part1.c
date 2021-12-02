#include <stdio.h>
#include <stdlib.h>

#define RESET   "\033[0m"
#define BOLDWHITE   "\033[1m\033[37m"

int main()
{
    int previous = 0;
    int current = 0;
    int increase = 0;
    FILE *file = fopen("input.txt", "r");

    // if file doesn't exist
    if (file == NULL)
    {
        fprintf(stderr, "Unable to read the file.");
        exit(EXIT_FAILURE);
    }

    // read the first line
    fscanf(file, "%d", &previous);
    printf("%d (N/A - no previous measurement)\n", previous);

    // read the lines and count
    while (fscanf(file, "%d", &current) != EOF)
    {
        if (current > previous)
        {
            printf("%d " BOLDWHITE "(increased)\n" RESET, current);
            increase++;
        }
        else if (current == previous)
        {
            printf("%d (no change)\n", current);
        }
        else
        {
            printf("%d (descreased)\n", current);
        }

        previous = current;
    }

    // display the number of increases
    printf("There are %d measurements that are larger than the previous measurement.", increase);

    // close the file
    fclose(file);

    return EXIT_SUCCESS;
}