#include <fstream>
#include <vector>
#include <iostream>

int main()
{
    const int TARGET = 2020;

    std::ifstream fichier { "input2.txt" };
    std::vector<int> numbers;
    int nb;

    while (fichier >> nb)
    {
        numbers.push_back(nb);
    }

    for (int i = 0; i < (int)numbers.size() - 2; i++)
    {
        for (int j = i + 1; j < (int)numbers.size() - 1; j++)
        {
            for (int k = j +  1; k < (int)numbers.size(); k++)
            {
                if (numbers[i] + numbers[j] + numbers[k] == TARGET)
                {
                    std::cout << numbers[i] * numbers[j] * numbers[k] << std::endl;
                    return EXIT_SUCCESS;
                }
            }
        }
    }
}