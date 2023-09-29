#include <fstream>
#include <string>
#include <sstream>
#include <iostream>

int main()
{
    std::ifstream file { "input2.txt" };
    int validPasswords = 0;
    int position1, position2;
    char letter;
    std::string password;
    std::string skip;

    while (!file.eof())
    {
        file >> position1;
        std::getline(file, skip, '-');
        file >> position2;
        file >> letter;
        std::getline(file, skip, ' ');
        std::getline(file, password);

        // Check password
        bool position1ContainsLetter = false;
        bool position2ContainsLetter = false;

        if ((int)password.size() > position1 - 1 && password[position1 - 1] == letter)
        {
            position1ContainsLetter = true;
        }

        if ((int)password.size() > position2 - 1 && password[position2 - 1] == letter)
        {
            position2ContainsLetter = true;
        }

        if ((position1ContainsLetter && !position2ContainsLetter) || (!position1ContainsLetter && position2ContainsLetter))
        {
            validPasswords++;
        }
    }

    std::cout << validPasswords << std::endl;

    file.close();
}