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

    for (int i = 0; i < (int)numbers.size(); i++)
    {
        for (int j = i + 1; j < (int)numbers.size(); j++)
        {
            if (numbers[i] + numbers[j] == TARGET)
            {
                std::cout << numbers[i] * numbers[j] << std::endl;
                return EXIT_SUCCESS;
            }
        }
    }
}