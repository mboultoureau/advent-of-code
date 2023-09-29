#include <fstream>
#include <string>
#include <sstream>
#include <iostream>

int main()
{
    std::ifstream file { "input2.txt" };
    int validPasswords = 0;
    int min, max;
    char letter;
    std::string password;
    std::string skip;

    while (!file.eof())
    {
        file >> min;
        std::getline(file, skip, '-');
        file >> max;
        file >> letter;
        std::getline(file, skip, ':');
        std::getline(file, password);

        // Check password
        int nb = 0;
        int i = 0;
        while (nb <= max && i < (int)password.size())
        {
            if (password[i] == letter)
            {
                nb++;
            }
            i++;
        }

        if (nb >= min && nb <= max)
        {
            validPasswords++;
        }
    }

    std::cout << validPasswords << std::endl;

    file.close();
}